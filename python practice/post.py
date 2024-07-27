import requests 

res_obj = requests.post("https://reqres.in/api/register",json={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
})

print(res_obj.status_code)

assert res_obj.status_code == 200 ," status_code is not excepeted"
assert res_obj.json()["id"] == 4,"the id is  correct"



