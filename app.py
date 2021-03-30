from flask import Flask, render_template
from controllers.tasks_controller import tasks_blueprint # NEW

app = Flask(__name__)

# Register the blueprint with the Flask app
app.register_blueprint(tasks_blueprint) # NEW

@app.route('/')
def home():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)
