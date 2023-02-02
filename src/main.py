# -*- coding: utf-8 -*-
#
from typing import Union, List
from fastapi import FastAPI, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from pymongo import MongoClient
from models import Tema, Item

config = dotenv_values(".env")

ATLAS_URI='mongodb+srv://root:juana99@cluster0.zf9fl.mongodb.net/?retryWrites=true&w=majority'
DB_NAME='fastapi'

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#sudo pip3 install transformers
#sudo pip3 install  torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(ATLAS_URI)
    app.database = app.mongodb_client[DB_NAME]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get('/pregunta/{name}')
async def geeter(name,request: Request):
    salida =nlp = pipeline(
    'question-answering', 
    model='dracero/autotrain-preguntas-1711860065',
    tokenizer=(
        'dracero/autotrain-preguntas-1711860065',  
        {"use_fast": False}
     )
    )
    classifier = pipeline("text-classification", 
                        model="dracero/autotrain-dracero-fine-tuned-physics-2123168626")
    output = classifier(name)
    #Tiene que volver solo cuando estén bien los datos de clasificación
    #if float(output[0]['score'])<0.6:
    #    return [False,output[0]['score']]
    temas = request.app.database["temas"].find_one({"title": output[0]['label']})
    contex = temas["description"]
    salida = nlp(
        {
        'question': name,
        'context': contex
       }
      )
    
    return { "name":salida, "class": output[0]['label']}   

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=int(os.environ['PORT']))
# Esta es la pregunta que responde
# que hay que hacer para hallar la velocidad de un movil que se desplaza en linea recta