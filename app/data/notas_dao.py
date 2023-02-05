from app import db

from app.data.modelo.notas import Notas

class NotasDao:

    def select_all(self,db) -> list[Notas]:
        cursor = db.cursor()
        cursor.execute('SELECT n.id_alumno,i.nombre,n.seguridad,n.implantacion,n.redes,n.ingles FROM notas n INNER JOIN alumnos i ON n.id_alumno = i.id')
        notas_en_db = cursor.fetchall()
        notas : list[Notas]= list()
        for nota_en_db in notas_en_db:
            notas.append(Notas(nota_en_db[0], nota_en_db[1], nota_en_db[2],nota_en_db[3],nota_en_db[4],nota_en_db[5]))
        cursor.close()
        return notas

    def insert_nota(self, db,id_alumno,seguridad,implantacion,redes,ingles) -> bool:
        cursor = db.cursor()
        sql = "INSERT INTO notas (id_alumno,seguridad,implantacion,redes,ingles) VALUES (%s, %s, %s, %s, %s)" 
        data = (id_alumno,seguridad,implantacion,redes,ingles) 
        cursor.execute(sql,data) 
        db.commit() 
        return True
   
    def del_nota(self,db,id_alumno) -> bool:
        cursor = db.cursor() 
        sql = "DELETE FROM notas WHERE id_alumno=%s"
        data = list() 
        data.append(id_alumno)
        cursor.execute(sql,data) 
        db.commit() 
        return True
    def edit_nota(self,db,id_alumno,seguridad,implantacion,redes,ingles) -> bool:
        cursor = db.cursor() 
        sql = "UPDATE notas SET seguridad=%s, implantacion=%s, redes=%s, ingles=%s WHERE id_alumno=%s"
        data = (seguridad,implantacion,redes,ingles,id_alumno) 
        cursor.execute(sql,data) 
        db.commit() 
        return True