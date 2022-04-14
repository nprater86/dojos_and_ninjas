from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all();
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/<int:dojo_id>')
def dojo(dojo_id):
    data = {'id': dojo_id}
    target_dojo = Dojo.get_dojo_by_id(data)
    dojo = Dojo.get_ninjas_at_dojo(data)
    return render_template('dojo.html', dojo=target_dojo, ninjas = dojo.ninjas)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {"name": request.form['name']}
    Dojo.save(data)
    
    return redirect('/dojos')
