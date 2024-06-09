from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
host        = "postgre-server-peshh.postgres.database.azure.com" # hostname of the PostgreSQL Database Server
username    = f"admUser@{host}"     # hostname of the PostgreSQL Database Server
password    = "adm!nPassw0rd"       # hostname of the PostgreSQL Database Server
port        = "5432"                # hostname of the PostgreSQL Database Server
database    = "postgre-database"    # hostname of the PostgreSQL Database Server
full_string = f"{username}:{password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{full_string}'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbtest.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        task.date_created = datetime.utcnow() # update the date & time

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    db.metadata.reflect(bind=db.engine)

    if not db.engine.has_table(Todo.__tablename__):
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port='80')
