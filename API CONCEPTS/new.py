import requests

rep=requests.get(r'https://reqres.in/api/users?page=2')
print(rep.status_code)

rep =requests.post('https://reqres.in/api/users')
print(rep.status_code)

rep =requests.put("https://reqres.in/api/users/2")
print(rep.status_code)

rep =requests.delete('https://reqres.in/api/users/2')
print(rep.status_code)

