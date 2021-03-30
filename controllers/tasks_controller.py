# Import Flask and render_template
from flask import Flask, render_template
from repositories import task_repository # NEW

# Import Blueprint class from flask
from flask import Blueprint

# Create a new instance of Blueprint called "tasks"
tasks_blueprint = Blueprint("tasks", __name__)

# Declare a route for the list of tasks
# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@tasks_blueprint.route("/tasks")
def tasks():
    # return render_template("tasks/index.html")
    tasks = task_repository.select_all() # NEW
    return render_template("tasks/index.html", all_tasks = tasks) # NEW

# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'