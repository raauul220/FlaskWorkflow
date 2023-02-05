
from app import db

from app.data.modelo.alumno import Alumno

class AlumnoDao:

    def select_all(self,db) -> list[Alumno]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM alumnos')
        alumnos_en_db = cursor.fetchall()
        alumnos : list[Alumno]= list()
        for alumno_en_db in alumnos_en_db:
            alumnos.append(Alumno(alumno_en_db[0], alumno_en_db[1], alumno_en_db[2]))
        cursor.close()
        return alumnos

    def insert_user(self, db,nombre,apellido) -> bool:
        cursor = db.cursor()
        sql = "INSERT INTO alumnos (nombre,apellido) VALUES (%s, %s)" 
        data = (nombre,apellido) 
        cursor.execute(sql,data) 
        db.commit() 
        return True
   
    def del_user(self,db,id):
        cursor = db.cursor() 
        sql = "DELETE FROM alumnos WHERE id=%s"
        data = list() 
        data.append(id)
        cursor.execute(sql,data) 
        db.commit() 
        return True

    def edit_user(self,db,id,nombre,apellido) -> bool:
        cursor = db.cursor() 
        sql = "UPDATE alumnos SET nombre=%s, apellido=%s WHERE id=%s"
        data = (nombre,apellido,id) 
        cursor.execute(sql,data) 
        db.commit() 
        return True
