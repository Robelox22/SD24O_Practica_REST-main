import orm.modelos as modelos
from sqlalchemy.orm import Session
import orm.esquemas as esquemas
from sqlalchemy import and_


# Esta función es llamada por api.py
# para atender GET '/alumnos/{id}'
# select * from app.alumnos where id = id_alumno
def alumno_por_id(sesion:Session,id_alumno:int):
    print("select * from app.alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()

def calificacion_por_id(sesion:Session,id_alumno:int):
    print("select * from app.calificaciones where id = ", id_alumno )
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_alumno).first()

def borra_alumno_por_id(sesion:Session,id_alumno:int):
    print("delete from app.alumnos where id=,id_alumno")
    #1.Select para ver si existe el alumno borar
    usr=alumno_por_id(sesion, id_alumno)
    #borramoe
    if usr is not None:
        #borramos alumno
        sesion.delete(usr)
        #confirmamos cambios
        sesion.commit()
        respuesta={
            "mensaje": "alumno eliminado"
        }
        return respuesta
    
def fotos_por_id_alumno(sesion:Session, id_alumno:int):
    print("select * from app.fotos where=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all()

def borra_fotos_por_id(sesion:Session,id_alumno:int):
    print("delete from app.fotos where id=,id_alumno")
    #1.Select para ver si existe el alumno borar
    fotos_usr=fotos_por_id_alumno(sesion, id_alumno)
    #borramoe
    if fotos_usr is not None:
        for foto_alumno in fotos_usr:
            #borramos alumno
            sesion.delete(foto_alumno)
        #confirmamos cambios
        sesion.commit()
        respuesta={
            "mensaje": "foto eliminado"
        }
        return respuesta

def calificaciones_por_id_alumno(sesion:Session, id_alumno:int):
    print("select * from app.fotos where", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all()

def borra_calificaciones_por_id(sesion:Session,id_alumno:int):
    print("delete from app.fotos where id=",id_alumno)
    #1.Select para ver si existe el alumno borar
    calificaciones_usr=calificaciones_por_id_alumno(sesion, id_alumno)
    #borramoe
    if calificaciones_usr is not None:
        for calificaciones_alumno in calificaciones_usr:
            #borramos alumno
            sesion.delete(calificaciones_alumno)
        #confirmamos cambios
        sesion.commit()
        respuesta={
            "mensaje": "foto eliminado"
        }
        return respuesta

def borra_alumno_por_id_calif(sesion:Session,id_alumno:int):
    print("delete from app.calif where id=", id_alumno)
    # Borrar las calificaciones del alumno
    calificaciones_usr = calificaciones_por_id_alumno(sesion, id_alumno)
    if calificaciones_usr:
        for calificacion in calificaciones_usr:
            sesion.delete(calificacion)
        sesion.commit()
        respuesta = {"mensaje": "Calificaciones eliminadas"}

    return respuesta

def borra_alumno_por_id_foto(sesion: Session, id_alumno: int):
    print("delete from app.calif where id=", id_alumno)
    # Borrar las fotos del alumno
    fotos_usr = fotos_por_id_alumno(sesion, id_alumno)
    if fotos_usr:
        for foto in fotos_usr:
            sesion.delete(foto)
        sesion.commit()
        respuesta = {"mensaje": "Fotos eliminadas"}
  
    return respuesta

def foto_por_id(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id = ", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_alumno).first()

def devuelve_alumnos(session:Session):
    print("select * from app.alumnos")
    return session.query(modelos.Alumno).all()

def devuelve_calificaciones(session:Session):
    print("select * from app.calificaciones")
    return session.query(modelos.Calificacion).all()

def devuelve_fotos(session:Session):
    print("select * from app.fotos")
    return session.query(modelos.Foto).all()

#POST '/alumnos'
def guardar_Alumno(sesion:Session, usr_nuevo:esquemas.AlumnoBase):
    #1.- Crear un nuevo objeto de la clase modelo alumno
    usr_bd = modelos.Alumno()
    #2.- Llenamos el nuevo objeto con los parámetros que nos paso el alumno
    usr_bd.nombre = usr_nuevo.nombre
    usr_bd.edad = usr_nuevo.edad
    usr_bd.domicilio = usr_nuevo.domicilio
    usr_bd.carrera =usr_nuevo.carrera
    usr_bd.trimestre =usr_nuevo.trimestre
    usr_bd.email = usr_nuevo.email
    usr_bd.password = usr_nuevo.password
    #3.- Insertar el nuevo objeto a la BD
    sesion.add(usr_bd)
    #4.- Confirmamos el cambio
    sesion.commit()
    #5.- Hacemos un refresh
    sesion.refresh(usr_bd)
    return usr_bd

#POST '/calificacion'
def guardar_calificiacion(sesion:Session, usr_nuevo:esquemas.CalificacionBase):
    #1.- Crear un nuevo objeto de la clase modelo alumno
    usr_bd = modelos.Calificacion()
    #2.- Llenamos el nuevo objeto con los parámetros que nos paso el alumno
    usr_bd.id_alumno = usr_nuevo.id_alumno
    usr_bd.uea = usr_nuevo.uea
    usr_bd.calificacion = usr_nuevo.calificacion
   
    #3.- Insertar el nuevo objeto a la BD
    sesion.add(usr_bd)
    #4.- Confirmamos el cambio
    sesion.commit()
    #5.- Hacemos un refresh
    sesion.refresh(usr_bd)
    return usr_bd
#POST '/calificacion'

def guardar_fotos(sesion:Session, usr_nuevo:esquemas.FotoBase):
    #1.- Crear un nuevo objeto de la clase modelo alumno
    usr_bd = modelos.Foto()
    #2.- Llenamos el nuevo objeto con los parámetros que nos paso el alumno
    usr_bd.id_alumno = usr_nuevo.id_alumno
    usr_bd.titulo = usr_nuevo.titulo
    usr_bd.descripcion= usr_nuevo.descripcion
    usr_bd.ruta = usr_nuevo.ruta
   
    #3.- Insertar el nuevo objeto a la BD
    sesion.add(usr_bd)
    #4.- Confirmamos el cambio
    sesion.commit()
    #5.- Hacemos un refresh
    sesion.refresh(usr_bd)
    return usr_bd


def actualiza_alumno(sesion:Session,id_alumno:int,usr_esquema:esquemas.AlumnoBase):
    #1.-Verificar que el alumno existe
    usr_bd = alumno_por_id(sesion,id_alumno)
    if usr_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        usr_bd.nombre = usr_esquema.nombre
        usr_bd.edad = usr_esquema.edad
        usr_bd.domicilio = usr_esquema.domicilio
        usr_bd.carrera =usr_esquema.carrera
        usr_bd.trimestre =usr_esquema.trimestre
        usr_bd.email = usr_esquema.email
        usr_bd.password = usr_esquema.password
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(usr_bd)
        #5.-Imprimir los datos nuevos
        print(usr_esquema)
        return usr_esquema
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
def actualiza_calificacion(sesion:Session,id_alumno:int,usr_esquema:esquemas.CalificacionBase):
    #1.-Verificar que el alumno existe
    usr_bd = alumno_por_id(sesion,id_alumno)
    if usr_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        usr_bd.id_alumno= usr_esquema.id_alumno
        usr_bd.uea = usr_esquema.uea
        usr_bd.calificacion = usr_esquema.calificacion  
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(usr_bd)
        #5.-Imprimir los datos nuevos
        print(usr_esquema)
        return usr_esquema
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
def actualiza_foto(sesion:Session,id_alumno:int,usr_esquema:esquemas.FotoBase):
    #1.-Verificar que el alumno existe
    usr_bd = alumno_por_id(sesion,id_alumno)
    if usr_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        usr_bd.id_alumno= usr_esquema.id_alumno
        usr_bd.uea = usr_esquema.titulo
        usr_bd.descripcion= usr_esquema.descripcion
        usr_bd.ruta = usr_esquema.ruta
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(usr_bd)
        #5.-Imprimir los datos nuevos
        print(usr_esquema)
        return usr_esquema
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
