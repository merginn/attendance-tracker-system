from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to hold student information
students = []

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        admin_id = request.form['admin_id']
        password = request.form['password']
        # Validate admin credentials (this is just an example)
        if admin_id == 'admin' and password == 'password':
            return redirect(url_for('admin_panel'))
        else:
            return "Invalid credentials", 403  # Return error if credentials are wrong
    return render_template('admin_login.html')

@app.route('/admin_panel')
def admin_panel():
    return render_template('admin_panel.html', students=students)

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    global students
    # Delete the student by filtering out the student with the matching ID
    students = [student for student in students if student['id'] != student_id]
    return redirect(url_for('admin_panel'))

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        surname = request.form['surname']
        group_id = request.form['group_id']
        subject = request.form['subject']

        # Save the details, including an ID
        new_student = {
            'id': len(students) + 1,  # Simple ID generation; consider UUID for production
            'first_name': first_name,
            'surname': surname,
            'group_id': group_id,
            'subject': subject
        }
        students.append(new_student)
        return redirect(url_for('student_panel'))
    return render_template('student_panel.html')

@app.route('/student_panel')
def student_panel():
    return render_template('student_panel.html')

if __name__ == '__main__':
    app.run(debug=True)
