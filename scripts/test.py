import os
import json,sys,time,urllib.request
SP=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','system_prompt.md')).read()
VS='vs_6ac368acbc64819186fb0a0b0b2e3864'
def ask(model,q,prev=None,effort='low'):
    p={'model':model,'instructions':SP,'input':[{'role':'user','content':q}],'tools':[{'type':'file_search','vector_store_ids':[VS],'max_num_results':6}],'store':True}
    if effort and not model.startswith('gpt-4'): p['reasoning']={'effort':effort}
    if prev: p['previous_response_id']=prev
    t=time.time()
    r=urllib.request.Request(os.environ['MANUEL_WEBHOOK_URL'],data=json.dumps({'payload':p}).encode(),headers={'Content-Type':'application/json'})
    j=json.loads(urllib.request.urlopen(r,timeout=180).read())
    j['wall']=round(time.time()-t,1); return j
if __name__=='__main__':
    model=sys.argv[1]
    for q in sys.argv[2:]:
        j=ask(model,q); print(f"\n### [{model}] {q}\n wall={j['wall']}s usage={j.get('usage')} err={j.get('error')} searches={j.get('searches')} cites={j.get('cites')}\n{j.get('text')}")
