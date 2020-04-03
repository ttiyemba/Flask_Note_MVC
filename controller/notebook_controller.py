from controller import app, AlchemyEncoder
from flask import request, render_template, redirect, url_for
from model import db
from model.note import Note
from model.notebook import Notebook
import json

@app.route("/notebook/<notebook_id>", methods=["GET"])
def view__single_notebook(notebook_id):
    notebook = db.session.query(Note).filter(Note.notebook_id == notebook_id).all()
    notebook_title = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    
    
    
    return render_template("notebook.html", title=notebook_title.title, notebook = notebook, current_notebook = notebook_title, test=notebook_id)


@app.route("/notebook", methods=["POST"])
def add_notebook():
    notebook_data = request.form
    notebook = Notebook(**notebook_data)
    db.session.add(notebook)
    db.session.commit()
    return redirect("/notebook")

@app.route("/notebook",methods=["GET"])
def get_all_notebooks():
    notebooks = db.session.query(Notebook).all()
    
    return render_template("notebooks.html", title="Notebooks", notebooks=notebooks)

@app.route("/notebook/<notebook_id>",)
def view_single_notebook(notebook_id):
    notebook = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    return render_template("notebook.html", title=notebook.title, notebook = notebook)



@app.route("/notebook/remove/<notebook_id>", methods=["POST"])
def note_delete(notebook_id):
    note = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    db.session.delete(note)
    db.session.commit()
    return redirect("/notebook")

@app.route("/notebook/edit/<notebook_id>", methods=["GET"])
def notebook_edit(notebook_id):
    notebook = db.session.query(Notebook).filter(Notebook.id == notebook_id).first()
    test = notebook_id
    
    return render_template("editnotebook.html", title="Edit Notebook", notebook=notebook, test=test)

@app.route("/notebook/update", methods=["POST"])
def notebook_update():
    note_data = request.form
    notebook = db.session.query(Notebook).filter(Notebook.id == note_data["id"]).first()
    notebook.title = note_data["title"]
    db.session.commit()
    return redirect( "/notebook")  

     




