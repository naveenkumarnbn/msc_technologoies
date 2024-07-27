import requests

res_obj= requests.post("https://reqres.in/api/users",json ={
    "name": "morpheus",
    "job": "leader"
})
print(res_obj.status_code)

assert res_obj.status_code == 201,"status code is not correct"
assert res_obj.json()["name"] == "morpheus","response data is not correct"