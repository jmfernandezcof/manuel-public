import os
import json,base64,sys,urllib.request
SP=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','system_prompt.md')).read()
VS='vs_6ac368acbc64819186fb0a0b0b2e3864'
img='data:image/jpeg;base64,'+base64.b64encode(open(sys.argv[1],'rb').read()).decode()
for txt in sys.argv[2:]:
    content=[{'type':'input_text','text':txt},{'type':'input_image','image_url':img,'detail':'auto'}]
    p={'model':'gpt-5.5','instructions':SP+'\n\n# Current user\nFirst name: Tony','input':[{'role':'user','content':content}],
       'tools':[{'type':'file_search','vector_store_ids':[VS],'max_num_results':6}],'reasoning':{'effort':'low'},'truncation':'auto','store':True,'include':['file_search_call.results']}
    r=urllib.request.Request(os.environ['MANUEL_WEBHOOK_URL'],data=json.dumps({'payload':p}).encode(),headers={'Content-Type':'application/json'})
    j=json.loads(urllib.request.urlopen(r,timeout=150).read())
    print(f"\n👤 [📷] {txt}\n🤖 [{j.get('secs')}s src={j.get('src')} err={j.get('error')}]\n{j.get('text')}")
