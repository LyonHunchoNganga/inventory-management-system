import requests

url = "http://127.0.0.1:5000"

print("1-view 2-add 3-del")

c = input("> ")

if c == "1":
    print(requests.get(url+"/items").json())

if c == "2":
    n = input("name:")
    q = input("qty:")
    print(requests.post(url+"/items", json={"name": n, "qty": q}).json())

if c == "3":
    i = input("id:")
    print(requests.delete(url+"/items/"+i).json())