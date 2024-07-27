import requests

res_obj=requests.put("https://reqres.in/api/users/2",json={
    "name": "morpheus",
    "job": "zion resident"
})

print(res_obj.status_code)

assert res_obj.status_code == 200 ,"status_code is not excepeted"
assert res_obj.json()["name"] == "morpheus","the message is in correct"