import requests

res_obj =  requests.put("https://reqres.in/api/users/2",json={
    "name": "morpheus",
    "job": "zion resident"
})
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is not correct"
assert res_obj.json()["job"] == "zion resident","response data is not correct"