from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

items = []
idc = 1

@app.get("/items")
def get_items():
    return jsonify(items)

@app.post("/items")
def add():
    global idc
    data = request.json
    item = {"id": idc, "name": data["name"], "qty": data["qty"]}
    items.append(item)
    idc += 1
    return item

@app.delete("/items/<int:i>")
def delete(i):
    for x in items:
        if x["id"] == i:
            items.remove(x)
            return {"msg": "deleted"}
    return {"error": "not found"}

@app.get("/product/<barcode>")
def product(barcode):
    return requests.get(
        f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    ).json()

if __name__ == "__main__":
    app.run(debug=True)