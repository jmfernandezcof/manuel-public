import os
import json,time,urllib.request,concurrent.futures as cf
SP=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','system_prompt.md')).read()
VS='vs_6ac368acbc64819186fb0a0b0b2e3864'
URL=os.environ['MANUEL_WEBHOOK_URL']
def turn(q,prev,name):
    p={'model':'gpt-5.5','instructions':SP+'\n\n# Current user\nFirst name: '+name,'input':[{'role':'user','content':q}],
       'tools':[{'type':'file_search','vector_store_ids':[VS],'max_num_results':6}],'reasoning':{'effort':'low'},'store':True,'include':['file_search_call.results']}
    if prev: p['previous_response_id']=prev
    r=urllib.request.Request(URL,data=json.dumps({'payload':p}).encode(),headers={'Content-Type':'application/json'})
    return json.loads(urllib.request.urlopen(r,timeout=150).read())
def convo(title,name,msgs):
    prev=None; log=[f"\n================ {title} ================"]
    for m in msgs:
        try:
            j=turn(m,prev,name); prev=j.get('id') or prev
        except Exception as e:
            j={'text':'!!! '+repr(e)}
        log.append(f"\n👤 {m}\n🤖 [{j.get('secs')}s src={','.join(s.replace('.pdf','') for s in j.get('src') or [])}{' ERR '+str(j.get('error')) if j.get('error') else ''}]\n{j.get('text')}")
    return '\n'.join(log)
S=json.load(open('scenarios.json'))
with cf.ThreadPoolExecutor(3) as ex:
    for out in ex.map(lambda s: convo(*s), S): print(out, flush=True)
