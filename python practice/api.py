import requests

res_obj = requests.get(" https://reqres.in/api/users?page=2")
print(res_obj.status_code)

assert res_obj.status_code == 200 ,"status code is not corret"

res_obj = requests.post("https://reqres.in/api/users",json={"Name": "SRIRAM", "Mobile": 9738274425})
print(res_obj.status_code)

assert res_obj.status_code == 201,"status code is not correct"
assert res_obj.json()[ "Name"] == "SRIRAM","response code is not correct"

res_obj = requests.put("https://reqres.in/api/users/2", json={"Name": "SRIRAM", "Mobile": 9738274425})
print(res_obj.status_code)

assert res_obj.status_code == 200,"status_code is not correct"
assert res_obj.json()["Name"] == "SRIRAM","response code is not correct"

res_obj = requests.delete("https://reqres.in/api/users/2")
print(res_obj.status_code)

assert res_obj.status_code == 204,"status_code is not correct"
