'''from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Task Manager API Running"

if __name__ == "__main__":
    app.run(debug=True)'''


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean, default=False)

# Create Database
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def home():
    return "Database Connected"

# CREATE TASK
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    task = Task(
        title=data['title']
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "message": "Task Created"
    }), 201

# GET ALL TASKS
@app.route('/tasks', methods=['GET'])
def get_tasks():

    tasks = Task.query.all()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        })

    return jsonify(task_list)

# GET SINGLE TASK
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):

    task = Task.query.get_or_404(id)

    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    })

# UPDATE TASK
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = Task.query.get_or_404(id)

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.completed = data.get('completed', task.completed)

    db.session.commit()

    return jsonify({
        "message": "Task Updated"
    })

# DELETE TASK
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task Deleted"
    })

if __name__ == "__main__":
    app.run(debug=True)