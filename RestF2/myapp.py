
import requests
import json
URL = "http://127.0.0.1:8000/stuapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data=json.dumps(data)
    print(json_data)
    headers = {'content-type':'application/json'}
    r = requests.get(url= URL,headers= headers,data = json_data)
    data = r.json()
    print(data)

get_data()

def post_data():
    data = {
    'name':'ramesh',
    'roll':104,
    'city':'rajkot'
    }
    headers = {'content-type':'application/json'}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.post(url = URL , headers= headers,data = json_data)
    data = r.json
    print(data)

#post_data()

def update_data():
    data = {
    'id':4,
    'name':'umesh ',
    'city':'sk'
    }
    headers = {'content-type':'application/json'}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.put(url = URL , headers= headers,data = json_data)
    data = r.json
    print(data)

#update_data()

def delete_data():
    data = {'id':4}
    headers = {'content-type':'application/json'}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.delete(url = URL ,headers= headers, data = json_data)
    data = r.json
    print(data)

#delete_data()


