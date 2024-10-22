from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = {"name": name, "attendance": False}
            return True
        return False

    def mark_attendance(self, student_id):
        if student_id in self.students:
            if not self.students[student_id]["attendance"]:
                self.students[student_id]["attendance"] = True
                return True
        return False

attendance_system = AttendanceSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    success = attendance_system.add_student(data['id'], data['name'])
    return jsonify({"success": success})

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    success = attendance_system.mark_attendance(data['id'])
    return jsonify({"success": success})

if __name__ == '__main__':
    app.run(debug=True)