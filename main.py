from fastapi import FastAPI
from models import Hero, Ability, AbilityType, Relationship, RelationshipType
from sqlalchemy import select
from enum import Enum

from routes import heroes


app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def root():
    return {"msg": "hello world"}

########################------------------------------------------------

# from fastapi import FastAPI #imported fast api
# from enum import Enum

# app = FastAPI() #instance of fastapi class named it app

# class ModelName(str, Enum):
#         alexnet = "alexnet"
#         resnet = "resnet"
#         lenet = "lenet"

# # @app.get("/") #decorator - above our functions to do our CRUD operations
# # async def root():
# #     return {"message": "Hello World"}

# @app.get("/") #slash means root directory - HAVE TO HAVE @ SYMBOL in front of decorator
#               #path operation decorator
# async def read_root(): #path operation function
#     return {"msg": "Hello World"} #this needs to match the msg in the test fastapi file

# @app.get("/items/{item_id}") #a url path used for this operation - aka function below
# async def read_item(item_id: int): #item_id as an argument...?
#     return {"item_id": item_id} #return this object


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenat":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}
