import json
from bottle import route, run
import pandas as pd

df = pd.read_csv('test.csv',sep='\t')

@route('/search/<name>', method='GET')
def search(name='No Name'):
    outJson= []
    for index,result in df[df.Name == name].iterrows():
	outJson.append(result.to_json())
    return json.dumps(outJson)

run(host='localhost', port=8080, debug=True)

