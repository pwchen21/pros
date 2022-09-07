import requests


# GET
r = requests.get("https://swapi.dev/api/people/1", verify=False)
print(r.status_code)
print(r.ok) # Check Status Code
print(r.text, "\n") # HTML

list_of_dicts = r.json()
#print(type(r))
#print(list_of_dicts)
for i in list_of_dicts:
    print(i, ":", list_of_dicts[i])

# PUT

# DELETE

# POST

