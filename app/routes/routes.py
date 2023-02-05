from flask import Blueprint, render_template, request,redirect

from app import db
from app.data.alumno_dao import AlumnoDao
from app.data.notas_dao import NotasDao
from app.data.modelo.alumno import Alumno
from app.data.modelo.notas import Notas

rutas_usuarios = Blueprint("routes", __name__)

@rutas_usuarios.route('/')
def alumnos():
    alumnoDao = AlumnoDao()
    alumnos = alumnoDao.select_all(db)
    return render_template('index.html', alumnos=alumnos)

@rutas_usuarios.route('/insertar', methods=['POST'])
def insert_user():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    alumnoDao = AlumnoDao()
    alumnoDao.insert_user(db,nombre,apellido)
    return redirect('/')

@rutas_usuarios.route('/delete',methods=['POST'])
def del_user():
    id = request.form['id']
    alumnoDao = AlumnoDao()
    alumnoDao.del_user(db,id)
    return redirect('/')

@rutas_usuarios.route('/edit',methods=['POST'])
def edit_user():
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    alumnoDao = AlumnoDao()
    alumnoDao.edit_user(db,id,nombre,apellido)
    return redirect('/')

@rutas_usuarios.route('/notas')
def notas():
    notasDao = NotasDao()
    notasDao = notasDao.select_all(db)
    return render_template('notas.html', notas= notasDao)
   
@rutas_usuarios.route('/insertar_nota', methods=['POST'])
def insert_nota():
    id_alumno = request.form['id_alumno']
    seguridad = request.form['seguridad']
    implantacion = request.form['implantacion']
    redes = request.form['redes']
    ingles = request.form['ingles']
    notasDao = NotasDao()
    notasDao.insert_nota(db,id_alumno,seguridad,implantacion,redes,ingles)
    return redirect('/notas')

@rutas_usuarios.route('/delete_nota',methods=['POST'])
def del_nota():
    id_alumno = request.form['id_alumno']
    notasDao = NotasDao()
    notasDao.del_nota(db,id_alumno)
    return redirect('/notas')

@rutas_usuarios.route('/edit_nota',methods=['POST'])
def edit_nota():
    id_alumno = request.form['id_alumno']
    seguridad = request.form['seguridad']
    implantacion = request.form['implantacion']
    redes = request.form['redes']
    ingles = request.form['ingles']
    notasDao = NotasDao()
    notasDao.edit_nota(db,id_alumno,seguridad,implantacion,redes,ingles)
    return redirect('/notas')






