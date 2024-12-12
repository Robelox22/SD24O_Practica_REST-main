from pydantic import BaseModel

#Definir el esquema usuario
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

class CalificacionBase(BaseModel):
    id_alumno:int
    uea:int
    calificacion:str

class FotoBase(BaseModel):
    id_alumno:int
    titulo: str
    descripcion: str
    ruta: str