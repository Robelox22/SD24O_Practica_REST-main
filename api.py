from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
import orm.esquemas as esquemas
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

@app.post("/alumnos")
def guardar_alumno(alumno:AlumnoBase, parametro1:str):
    print("alumno a guardar:", alumno, ", parametro1:", parametro1)
    #simulamos guardado en la base.
    
    usr_nuevo = {}
    usr_nuevo["id"] = len(alumnos)
    usr_nuevo["nombre"] = alumno.nombre
    usr_nuevo["edad"] = alumno.edad
    usr_nuevo["domicilio"] = alumno.domicilio

    alumnos.append(alumno)

    return usr_nuevo
#----

@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    print(alumno)
    #guardado en la base.
    return repo.guardar_Alumno(sesion,alumno)

@app.post("/alumnos/{id}/fotos")
def guardar_alumno(alumno:AlumnoBase, parametro1:str):
    print("alumno a guardar:", alumno, ", parametro1:", parametro1)
    #simulamos guardado en la base.
    
    usr_nuevo = {}
    usr_nuevo["id"] = len(alumnos)
    usr_nuevo["nombre"] = alumno.nombre
    usr_nuevo["edad"] = alumno.edad
    usr_nuevo["domicilio"] = alumno.domicilio

    alumnos.append(alumno)

    return usr_nuevo



@app.put("/alumno/{id}")
def actualiza_alumno(id:int,info_alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_alumno(sesion,id,info_alumno)


@app.delete("/alumno/{id}")
def borrar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}

 

#--------------------calificaciones---------------------------



@app.get("/calificaciones/{id}")
def calificacion_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por id")
    return repo.calificacion_por_id(sesion, id)
@app.get("/fotos/{id}")
def foto_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos por id")
    return repo.foto_por_id(sesion, id)

@app.delete("/calificaciones/{id}")
def borrar_calificaciones(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id (sesion,id)
    return {"alumno_borrado", "ok"}

@app.delete("/alumno/{id}/calificaciones")
def borrar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id_calif(sesion,id)
    return {"alumno_borrado", "ok"}


@app.put("/calificaciones/{id}")
def actualiza_calificacion(id:int,info_alumno:esquemas.CalificacionBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_calificacion(sesion,id,info_alumno)
#----------Fotos----------------------------------------

@app.delete("/fotos/{id}")
def borrar_foto(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_fotos_por_id(sesion,id)
    return {"alumno_borrado", "ok"}



@app.delete("/alumno/{id}/fotos")
def borrar_alumno(id:int,sesion:Session=Depends(generador_sesion)):
    repo.borra_alumno_por_id_foto(sesion,id)
    return {"alumno_borrado", "ok"}

@app.put("/fotos/{id}")
def actualiza_foto(id:int,info_alumno:esquemas.FotoBase,sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_foto(sesion,id,info_alumno)



