# -*- coding: utf-8 -*-
from typing import Union
from transformers import pipeline
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

#Esta función debe aceptar dos valores, uno es la clase y otro la pregunta. Primero usando Pymongo busca el context a partir de la clase y luego 
#busca la pregunta en el context.


@app.get('/pregunta/{name}/class/{classtype}')
async def geeter(name,classtype):
    salida =nlp = pipeline(
    'question-answering', 
    model='dracero/autotrain-preguntas-1711860065',
    tokenizer=(
        'dracero/autotrain-preguntas-1711860065',  
        {"use_fast": False}
     )
    )   
    
    #Este es el contexto que hay que ir a buscarlo a una base de datos
    context = 'El primer término es la velocidad del punto P, el segundo la velocidad del centro demasas y el tercero es la velocidad del punto P respecto del centro de masas.Como el vector R tiene módulo constante, el único movimiento posible de P respecto de C es una rotación con velocidad angular ω alrededor de un eje instantáneo que pase por C, tal como se ve en la figura de la derecha. Por tanto, el movimiento de un punto P del sólido se puede considerar como la suma de un movimiento de traslación del centro de masas más una rotación alrededor de un eje instantáneo que pasa por el centro de masas. Los cuerpos rígidos tienen como movimiento general una composición de un movimiento de traslación más otro de rotación. Siempre es posible encontrar un sistema de referencia en traslación pero no rotante respecto del cual el movimiento del cuerpo parezca solo de rotación. Para un cuerpo rígido, si se conoce dónde está en un momento determinado una partícula y el ángulo θ de rotación del cuerpo respecto a la posición original, conocemos el resto de las posiciones de los puntos.	El movimiento general de un sólido rígido es la composición de un movimiento de traslación del centro de masas y de un movimiento de rotación alrededor de un eje que pasa por el centro de masas. En el movimiento de traslación, todos los puntos del sólido se mueven en trayectorias paralelas. La velocidad de un punto del sólido es la misma que la velocidad del centro de masas. En el movimiento de rotación alrededor de un eje que pasa por el centro de masas, la velocidad de ununto del sólido es proporcional la radio de la circunferencia que describe, y su dirección es tangente a dicha circunferencia.'

    salida = nlp(
        {
        'question': name,
        'context': context
       }
      )
    
    return { "name":salida,"class": classtype}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ['PORT']))
