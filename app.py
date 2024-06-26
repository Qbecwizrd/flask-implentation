from flask import Flask,request
#create app
app=Flask(__name__)
#create store
stores=[
    {
        "name":"My Store",
        "items":[
            {
                "name":"chair",
                "price":15.99
            }
        ]
    }
]
#create get method to get the stores 
@app.get("/store")
def get_stores():
    return {"store":stores}

#create post method
@app.post("/store")
def create_stores():
    request_data=request.get_json()
    new_store={"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201
#create method to enter items in store
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item,201
    return {"message":"Store not found"},404
#get the store 
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"]==name:
            return store
    return {"message":"Store not found"},404
#get the items in the store
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"]==name:
            return {"items":store["items"]} 
    return {"message":"Store not found"},404

