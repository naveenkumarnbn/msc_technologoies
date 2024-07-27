import requests

res_obj= requests.get("https://reqres.in/api/users")
print(res_obj.status_code)
assert  res_obj.status_code == 200 ,"status_code is not excepeted"
assert res_obj.json()['page'] == 1 ,"the page is not correct "

res_obj = requests.get("https://reqres.in/api/users/23")
print(res_obj.status_code)

assert res_obj.status_code == 404 ,"status_code is not excepeted"

res_obj = requests.get("https://reqres.in/api/unknown")
print(res_obj.status_code)

assert res_obj.status_code == 200 ,"status_code is not excepeted"
assert res_obj.json()["total"] == 12,"the page is not correct "



