import requests
import json

files1 = {
    'package': ('service-chain1.son', open('service-chain1.son', 'rb')),
}
files2 = {
    'package': ('service-chain2.son', open('service-chain2.son', 'rb')),
}
files3 = {
    'package': ('service-chain3.son', open('service-chain3.son', 'rb')),
}
files4 = {
    'package': ('loadbalancer-service.son', open('loadbalancer-service.son', 'rb')),
}

response = requests.post('http://127.0.0.1:5000/packages', files=files1)
response = requests.post('http://127.0.0.1:5000/packages', files=files2)
response = requests.post('http://127.0.0.1:5000/packages', files=files3)
response = requests.post('http://127.0.0.1:5000/packages', files=files4)

response = requests.get('http://127.0.0.1:5000/packages')
json = json.loads(response.text)

for service in json['service_uuid_list']:
    data = '{"service_uuid":"%s"}' % service
    response = requests.post('http://127.0.0.1:5000/instantiations', data=data)
