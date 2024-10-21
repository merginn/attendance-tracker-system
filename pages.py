import customtkinter as ctk

class welcome_page(ctk.CTkFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Welcome to the Attendance Tracker System Application")
        label.grid(row=0, column=0, padx=20, pady=20)

        admin_button = ctk.CTkButton(self, text="Go to Admin Page", command=lambda: controller.up_frame(admin_page))
        admin_button.grid(row=1, column=0, padx=20, pady=20)

class admin_page(ctk.CTkFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        self.students = {}

        label = ctk.CTkLabel(self, text="Admin Page")
        label.grid(row=0, column=0, padx=20, pady=10)

        add_student_label = ctk.CTkLabel(self, text="Add Student")
        add_student_label.grid(row=1, column=0, padx=20, pady=10)

        self.student_id_entry = ctk.CTkEntry(self, placeholder_text="Enter Student ID")
        self.student_id_entry.grid(row=2, column=0, padx=20, pady=5)

        self.student_name_entry = ctk.CTkEntry(self, placeholder_text="Enter Student Name")
        self.student_name_entry.grid(row=3, column=0, padx=20, pady=5)

        add_student_button = ctk.CTkButton(self, text="Add Student", command=self.add_student)
        add_student_button.grid(row=4, column=0, padx=20, pady=5)

        attendance_label = ctk.CTkLabel(self, text="Attendance Taker")
        attendance_label.grid(row=5, column=0, padx=20, pady=10)

        self.user_id_entry = ctk.CTkEntry(self, placeholder_text="Enter User ID to Mark Attendance")
        self.user_id_entry.grid(row=6, column=0, padx=20, pady=10)

        mark_attendance_button = ctk.CTkButton(self, text="Mark Attendance", command=self.mark_attendance)
        mark_attendance_button.grid(row=7, column=0, padx=20, pady=10)

        welcome_button = ctk.CTkButton(self, text="Back to Welcome Page", command=lambda: controller.up_frame(welcome_page))
        welcome_button.grid(row=8, column=0, padx=20, pady=20)

        self.attendance_status = ctk.CTkLabel(self, text="")
        self.attendance_status.grid(row=9, column=0, padx=20, pady=10)

        self.marked_students_frame = ctk.CTkFrame(self)
        self.marked_students_frame.grid(row=10, column=0, padx=20, pady=10, sticky="nsew")

        marked_students_label = ctk.CTkLabel(self.marked_students_frame, text="Marked Attendance")
        marked_students_label.pack(pady=5)

        self.marked_students_scrollable = ctk.CTkScrollableFrame(self.marked_students_frame, width=300, height=200)
        self.marked_students_scrollable.pack(pady=5, fill="both", expand=True)

        self.marked_students_list = []

    def add_student(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()

        if student_id and student_name:
            if student_id not in self.students:
                self.students[student_id] = {"name": student_name, "attendance": False}
                self.attendance_status.configure(text=f"Added student: {student_name} (ID: {student_id})")
                self.student_id_entry.delete(0, ctk.END)
                self.student_name_entry.delete(0, ctk.END)
            else:
                self.attendance_status.configure(text="Student ID already exists.")
        else:
            self.attendance_status.configure(text="Please enter both ID and name.")

    def mark_attendance(self):
        user_id = self.user_id_entry.get()
        if user_id in self.students:
            if not self.students[user_id]["attendance"]:
                self.students[user_id]["attendance"] = True
                self.attendance_status.configure(text=f"Attendance marked for {self.students[user_id]['name']} (ID: {user_id})")
                self.update_marked_students_panel(user_id)
            else:
                self.attendance_status.configure(text=f"Attendance already marked for {self.students[user_id]['name']} (ID: {user_id})")
        else:
            self.attendance_status.configure(text="Invalid User ID")
        self.user_id_entry.delete(0, ctk.END)

    def update_marked_students_panel(self, user_id):
        student_info = f"{self.students[user_id]['name']} (ID: {user_id})"
        if student_info not in self.marked_students_list:
            label = ctk.CTkLabel(self.marked_students_scrollable, text=student_info)
            label.pack(anchor="w")
            self.marked_students_list.append(student_info)

class user_page(ctk.CTkFrame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        label = ctk.CTkLabel(self, text="User Page")
        label.grid(row=0, column=0, padx=20, pady=20)

        welcome_button = ctk.CTkButton(self, text="Back to Welcome Page", command=lambda: controller.up_frame(welcome_page))
        welcome_button.grid(row=1, column=0, padx=20, pady=20)

class AttendanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Attendance Management System")
        self.geometry("400x600")

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (welcome_page, admin_page, user_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.up_frame(welcome_page)

    def up_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()