import requests

res_obj = requests.get("https://reqres.in/api/users?page=2")
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is not correct"
assert res_obj.json()["data"][0]["last_name"] == "Lawson","response data is not correct"