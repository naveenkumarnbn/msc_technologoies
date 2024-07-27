import requests

res_obj=requests.get("https://reqres.in/api/users?page=2")
print(res_obj.status_code)

assert res_obj.status_code == 200,"res_obj.status_code expected"

res_obj=requests.post("https://reqres.in/api/users/2")
print(res_obj.status_code)

assert res_obj.status_code ==201 ,"res_obj.status_code is not expected" 
assert res_obj.json()
