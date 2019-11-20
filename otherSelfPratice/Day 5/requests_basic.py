import request

payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

r = request.post("https://reqres.in/api/login/", data=payload)

print(r.status_code)
# print (r.json())
#
# print (r.headers)

print(request.codes.values())
