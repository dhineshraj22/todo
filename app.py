from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
        flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
        flash('Congratulations! Task completed!', 'done')
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>')
def remove(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        flash('Oops! Task removed!', 'removed')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
