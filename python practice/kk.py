import requests

res_obj =requests.delete("https://reqres.in/api/users/2")
print(res_obj.status_code)

assert res_obj.status_code == 204,"status code is not correct"