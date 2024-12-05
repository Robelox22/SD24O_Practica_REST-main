from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

# creación del servidor
app = FastAPI()

#definición de la base del alumno
class AlumnoBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str    
    
alumnos = [{
    "id": 0,
    "nombre": "Rosa Gonzáles",
    "edad": 36,
    "domicilio": "Av. 102, 53"
}, {
    "id": 1,
    "nombre": "Irene Rojas",
    "edad": 38,
    "domicilio": "Calle 33, 10"
}, {
    "id": 2,
    "nombre": "Israel Ortíz",
    "edad": 8,
    "domicilio": "Av. Reforma, 122"
}, {
    "id": 3,
    "nombre": "Ximena Ramírez",
    "edad": 10,
    "domicilio": "Av. Constituyentes, 41"
}]


# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola Alumno!"
    }

    return respuesta



#---------------alumnos--------------------------------
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("api consultando todas las calificaciones")
    return repo.devuelve_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando ")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_usr(id:int,sesion:Session=Depends(generador_sesion)):
    print("api consultando")
    return repo.calificaciones_por_id_alumno(sesion,id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_id_usr(id:int,sesion:Session=Depends(generador_sesion)):
    print("api consultando todas las fotos")
    return repo.fotos_por_id_alumno(sesion,id)





#--------------------calificaciones---------------------------



@app.get("/calificaciones/{id}")
def calificacion_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id")
    return repo.calificacion_por_id(sesion, id)
@app.get("/fotos/{id}")
def foto_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por id")
    return repo.foto_por_id(sesion, id)

#----------Fotos----------------------------------------

@app.delete("/fotos/{id}")
def borrar_foto(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_fotos_por_id(sesion,id)
    return {"alumno_borrado", "ok"}

@app.delete("/calificaciones/{id}")
def borrar_calificaciones(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id (sesion,id)
    return {"alumno_borrado", "ok"}

@app.delete("/alumno/{id}/calificaciones")
def borrar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id_calif(sesion,id)
    return {"alumno_borrado", "ok"}

@app.delete("/alumno/{id}/fotos")
def borrar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id_foto(sesion,id)
    return {"alumno_borrado", "ok"}

@app.delete("/alumno/{id}")
def borrar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}


