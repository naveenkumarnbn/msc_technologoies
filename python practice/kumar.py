import req
res_obj = requests.get("https://reqres.in/api/users?page=2")

assert res_obj.status_code == 200 ,"status code is  not correct"
assert res_obj.json()["data"][5]["first_name"] == "Rachel","respose data is not correct"


res_obj = requests.get("https://reqres.in/api/users/2")

assert res_obj.status_code == 200,"status code is  not correct"
assert res_obj.json()["data"]['last_name'] == 'Weaver',"respose data is not correct"

res_obj = requests.get("https://reqres.in/api/unknown")
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is  not correct"
assert res_obj.json()["data"][4]["year"] == 2004,"respose data is not correct"

res_obj = requests.get("https://reqres.in/api/unknown/2")
    

assert res_obj.status_code == 200, "status code is  not correct"
assert res_obj.json()["support"]["url"] == "https://reqres.in/#support-heading","respose data is not correct"

res_obj = requests.get("https://reqres.in/api/users")
print(res_obj.status_code)

assert res_obj.status_code == 200,"status code is  not correct"
assert res_obj.json()["data"][5]["last_name"] == "Ramos","respose data is not correct"