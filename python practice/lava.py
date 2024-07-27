import requests

res_obj = requests.get("https://reqres.in/api/users?page=2")
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is matched"

res_obj = requests.post("https://reqres.in/api/users",json={
    "name": "morpheus",
    "job": "leader"
})

print(res_obj.status_code)

assert res_obj.status_code == 201,"status_code is not matched"
assert res_obj.json()[  "name"] == "morpheus","response data is not matched"

res_obj = requests.post("https://reqres.in/api/register",json={
    "email": "sydney@fife"
})
print(res_obj.status_code)

assert res_obj.status_code == 400,"status_code is not matched"
assert res_obj.json()["error"] == "Missing password","response_data is not matched"

