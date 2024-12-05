import orm.modelos as modelos
from sqlalchemy.orm import Session
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

