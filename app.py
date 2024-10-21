from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = {}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        student_name = request.form.get('student_name')
        if student_id and student_name and student_id not in students:
            students[student_id] = {"name": student_name, "attendance": False}
        return redirect(url_for('admin'))
    return render_template('admin.html', students=students)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    user_id = request.form.get('user_id')
    if user_id in students and not students[user_id]["attendance"]:
        students[user_id]["attendance"] = True
    return redirect(url_for('admin'))

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)
