from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninja_form():
    dojos = Dojo.get_all();
    return render_template('ninja_form.html', dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect(f"/dojos/{request.form['dojo_id']}")