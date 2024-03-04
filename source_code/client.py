import requests


#设置需要发送的数据
user_info={'name':'Marveric','password':'123456','hobbies':['code','fitting']}


#向url发送post请求

r=requests.post('http://127.0.0.1:5000/register',data=user_info)


print(r.text)

