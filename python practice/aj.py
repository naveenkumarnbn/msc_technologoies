import requests
res_obj = requests.post("https://reqres.in/api/users",json ={
    "name": "morpheus",
    "job": "leader"
})

print(res_obj.status_code)

assert res_obj.status_code == 201,"status code is not correct"
assert res_obj.json()[ "name"] ==  "morpheus","response code is not matched"

res_obj = requests.post("https://reqres.in/api/register",json ={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
})

print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is not corrcet"
assert res_obj.json()["token"] == "QpwL5tke4Pnpja7X4","response data is not correct"

res_obj = requests.post("https://reqres.in/api/register",json={
    "email": "sydney@fife"
})
print(res_obj.status_code)

assert res_obj.status_code == 400,"status code is not correct"
assert res_obj.json()[  "error"] == "Missing password","response data is not correct"

res_obj = requests.post("https://reqres.in/api/login",json ={
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})
print(res_obj.status_code)
assert res_obj.status_code == 200,"status code is not correct"
assert res_obj.json()["token"] == "QpwL5tke4Pnpja7X4","response data is not correct"

res_obj = requests.post("https://reqres.in/api/login",json ={
    "email": "peter@klaven"
})
print(res_obj.status_code)
assert res_obj.status_code == 400,"status code is not correct"
assert res_obj.json()["error"] == "Missing password","response data is not correct"

#HTTP METHOD[PUT]

res_obj= requests.put("https://reqres.in/api/users/2",json ={
    "name": "morpheus",
    "job": "zion resident"
})
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is not correct"
assert res_obj.json()["job"] == "zion resident","response data is not correct"

# HTTP delete method

res_obj = requests.delete("https://reqres.in/api/users/2")
print(res_obj.status_code)

assert res_obj.status_code == 204,"status code is not correct"

#HTTP patch method

res_obj = requests.patch("https://reqres.in/api/users/2",json ={
    "name": "morpheus",
    "job": "zion resident"
})
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is not correct"
assert res_obj.json()["name"] == "morpheus","response data is not correct"





