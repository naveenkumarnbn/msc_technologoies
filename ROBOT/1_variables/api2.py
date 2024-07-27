import requests
from requests.auth import HTTPBasicAuth

res_obj = requests.get('https://restful-booker.herokuapp.com/booking', auth=HTTPBasicAuth("admin","password123"))
print(res_obj.status_code)
print(res_obj.json())n