from tkinter import * 
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt


class Employee:
    def __init__(self, emp_id, name, salary, department, email):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department
        self.email = email

# Employee Management System class
class EmployeeManagementSystem:
    def __init__(self):
        self.create_database()
        self.create_main_window()

    def create_database(self):
        self.conn = sqlite3.connect("employee.db")
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def create_main_window(self):
        self.root = Tk()
        self.root.title("Employee Management System")
        self.root.geometry("800x600+50+50")
        f = ("Times New Roman" , 25 , "bold")
        f0 = ("Times New Roman" , 25 , "bold" , "underline" )
        photo = PhotoImage(file = 'D:\MIRA Advanced Engineering\Task-5\water.png.png')
        self.root.iconphoto(False , photo) 
        # # # Add image file
        # bg = PhotoImage(file = 'D:\MIRA Advanced Engineering\Task-5\')
  
        # # # Show image using label
        # label1 = Label( self.root, image = bg)
        # label1.place(x = 0, y = 0)

        label_signup = Label( self.root, text= "Employee Management System" , font=f0 , fg="darkblue")
        label_signup.pack(pady=20)
        
        # Signup button
        signup_btn = Button(self.root, border=8, font=f , bg = "lightblue" ,fg="black", text="Signup",width=12, command=self.signup)
        signup_btn.pack(pady=15)

        # Login button
        login_btn = Button(self.root, border=8, font=f , bg = "lightblue" ,fg="black",width=12, text="Login", command=self.login)
        login_btn.pack(pady=15)

        # Admin Login button
        admin_login_btn = Button(self.root, border=8, font=f , bg = "lightblue" ,width=12 ,fg="black", text="Admin Login", command=self.admin_login)
        admin_login_btn.pack(pady=15)

    def signup(self):
        self.signup_window = Toplevel(self.root)
        self.signup_window.title("Signup")
        self.signup_window.geometry("500x600+50+50")
        self.signup_window.configure(bg = "lightblue")
        f1= ("Times New Roman" , 15 )
        # # Add image file
        # bg = PhotoImage(file = "employee.png")
  
        # # Show image using label
        # label1 = Label( self.signup_window, image = bg)
        # label1.place(x = 0, y = 0)

        email_label = Label(self.signup_window,font=f1 ,bg="lightblue", text="Email:")
        email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.signup_window ,font=f1 )
        self.email_entry.grid(row=0, column=1)

        password_label = Label(self.signup_window,font=f1 , bg="lightblue", text="Password:")
        password_label.grid(row=1, column=0)
        self.password_entry = Entry(self.signup_window,font=f1 , show="*")
        self.password_entry.grid(row=1, column=1)

        signup_btn = Button(self.signup_window, text="Signup",border=5, bg="lightblue",font=f1 , command=self.add_user)
        signup_btn.grid(row=2, columnspan=2, pady=10)

    def add_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email and password:
            try:
                self.cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
                self.conn.commit()
                messagebox.showinfo("Signup Successful", "User created successfully!")
                self.logged_in_user = email
                self.create_employee_window()
                self.signup_window.destroy() #terminates the main loop process 
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "User with this email already exists.")
        else:
            messagebox.showerror("Error", "Please enter valid email and password.")

    def login(self):
        self.login_window = Toplevel(self.root)
        self.login_window.title("Login")
        self.login_window.geometry("500x600+50+50")
        self.login_window.configure(bg = "lightblue")
        f2= ("Times New Roman" , 15 )

        email_label = Label(self.login_window,bg="lightblue" ,fg="black",font=f2 ,height=1, text="Email:")
        email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.login_window , font=f2)
        self.email_entry.grid(row=0, column=1)

        password_label = Label(self.login_window,bg="lightblue" ,fg="black",font=f2 ,height=1, text="Password:")
        password_label.grid(row=1, column=0)
        self.password_entry = Entry(self.login_window,font=f2, show="*")
        self.password_entry.grid(row=1, column=1)

        login_btn = Button(self.login_window, text="Login",font=f2,border=4 , bg="lightblue", command=self.authenticate_user)
        login_btn.grid(row=2, columnspan=2, pady=10)

    def authenticate_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email and password:
            self.cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = self.cursor.fetchone()
            if user:
                messagebox.showinfo("Login Successful", "User authenticated successfully!")
                self.logged_in_user = email
                self.create_employee_window()
                self.login_window.destroy()
            else:
                messagebox.showerror("Authentication Error", "Invalid email or password.")
        else:
            messagebox.showerror("Error", "Please enter email and password.")

    def admin_login(self):
        self.admin_login_window = Toplevel(self.root)
        self.admin_login_window.title("Admin Login")
        self.admin_login_window.geometry("500x600+50+50")
        self.admin_login_window.configure(bg = "lightblue")
        f3= ("Times New Roman" , 15 )

        email_label = Label(self.admin_login_window,bg="lightblue" ,fg="black",font=f3 ,height=1, text="Email:")
        email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.admin_login_window, font=f3)
        self.email_entry.grid(row=0, column=1)

        password_label = Label(self.admin_login_window,bg="lightblue" ,fg="black",font=f3 ,height=1, text="Password:")
        password_label.grid(row=1, column=0)
        self.password_entry = Entry(self.admin_login_window,font=f3, show="*")
        self.password_entry.grid(row=1, column=1)

        login_btn = Button(self.admin_login_window,font=f3,border=4 , bg="lightblue", text="Login", command=self.authenticate_admin)
        login_btn.grid(row=2, columnspan=2, pady=10)

    def authenticate_admin(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email and password:
            self.cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = self.cursor.fetchone()
            if user:
                messagebox.showinfo("Admin Login Successful", "Admin authenticated successfully!")
                self.logged_in_user = email
                self.create_admin_window()
                self.admin_login_window.destroy()
            else:
                messagebox.showerror("Authentication Error", "Invalid email or password.")
        else:
            messagebox.showerror("Error", "Please enter email and password.")

    def create_employee_window(self):
        self.employee_window = Toplevel(self.root)
        self.employee_window.title("Employee Data")
        self.employee_window.geometry("500x600+50+50")
        self.employee_window.configure(bg = "lightblue")
        f4 = ("Times New Roman" , 15 )

        id_label = Label(self.employee_window,bg="lightblue" ,fg="black",font=f4 ,height=1, text="ID:")
        id_label.grid(row=0, column=0)
        self.id_entry = Entry(self.employee_window, font=f4)
        self.id_entry.grid(row=0, column=1)

        name_label = Label(self.employee_window,bg="lightblue" ,fg="black",font=f4 ,height=1, text="Name:")
        name_label.grid(row=1, column=0)
        self.name_entry = Entry(self.employee_window, font=f4)
        self.name_entry.grid(row=1, column=1)

        salary_label = Label(self.employee_window,bg="lightblue" ,fg="black",font=4 ,height=1, text="Salary:")
        salary_label.grid(row=2, column=0)
        self.salary_entry = Entry(self.employee_window, font=f4)
        self.salary_entry.grid(row=2, column=1)

        department_label = Label(self.employee_window,bg="lightblue" ,fg="black",font=f4 ,height=1, text="Department:")
        department_label.grid(row=3, column=0)
        self.department_entry = Entry(self.employee_window, font=f4)
        self.department_entry.grid(row=3, column=1)

        email_label = Label(self.employee_window,bg="lightblue" ,fg="black",font=f4 ,height=1, text="Email:")
        email_label.grid(row=4, column=0)
        self.email_entry = Entry(self.employee_window, font=f4)
        self.email_entry.grid(row=4, column=1)

        add_btn = Button(self.employee_window,font=f4,border=4 , bg="lightblue", text="Add Employee", command=self.add_employee)
        add_btn.grid(row=5, columnspan=2, pady=10)

        update_btn = Button(self.employee_window,font=f4,border=4 , bg="lightblue", text="Update Employee", command=self.update_employee)
        update_btn.grid(row=6, columnspan=2, pady=10)

        delete_btn = Button(self.employee_window,font=f4,border=4 , bg="lightblue", text="Delete Employee", command=self.delete_employee)
        delete_btn.grid(row=7, columnspan=2, pady=10)

    def add_employee(self):
        emp_id = self.id_entry.get()
        name = self.name_entry.get()
        salary = self.salary_entry.get()
        department = self.department_entry.get()
        email = self.email_entry.get()
        if emp_id and name and salary and department and email:
            try:
                self.cursor.execute(
                    "INSERT INTO employees (emp_id, name, salary, department, email) VALUES (?, ?, ?, ?, ?)",
                    (emp_id, name, salary, department, email),
                )
                self.conn.commit()
                messagebox.showinfo("Employee Added", "Employee added successfully!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Employee with this ID already exists.")
        else:
            messagebox.showerror("Error", "Please enter all employee details.")

    def update_employee(self):
        emp_id = self.id_entry.get()
        name = self.name_entry.get()
        salary = self.salary_entry.get()
        department = self.department_entry.get()
        email = self.email_entry.get()
        if emp_id and name and salary and department and email:
            self.cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
            employee = self.cursor.fetchone()
            if employee:
                self.cursor.execute(
                    "UPDATE employees SET name=?, salary=?, department=?, email=? WHERE emp_id=?",
                    (name, salary, department, email, emp_id),
                )
                self.conn.commit()
                messagebox.showinfo("Employee Updated", "Employee updated successfully!")
            else:
                messagebox.showerror("Error", "Employee not found.")
        else:
            messagebox.showerror("Error", "Please enter all employee details.")

    def delete_employee(self):
        emp_id = self.id_entry.get()
        if emp_id:
            self.cursor.execute("SELECT * FROM employees WHERE emp_id=?", (emp_id,))
            employee = self.cursor.fetchone()
            if employee:
                self.cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
                self.conn.commit()
                messagebox.showinfo("Employee Deleted", "Employee deleted successfully!")
            else:
                messagebox.showerror("Error", "Employee not found.")
        else:
            messagebox.showerror("Error", "Please enter employee ID.")

    def create_admin_window(self):
        self.admin_window = Toplevel(self.root)
        self.admin_window.title("Admin Panel")
        self.admin_window.geometry("500x600+50+50")
        self.admin_window.configure(bg="lightblue")
        f5 = ("Times New Roman",15 )

        view_data_btn = Button(self.admin_window,font=f5,border=4 , bg="lightblue", text="View Employee Data", command=self.view_employee_data)
        view_data_btn.pack(pady=10)

        view_chart_btn = Button(self.admin_window,font=5,border=4 , bg="lightblue", text="View Top 5 Employees by Salary Chart", command=self.view_top_employees_chart)
        view_chart_btn.pack(pady=10)

        logout_btn = Button(self.admin_window,font=f5,border=4 , bg="lightblue", text="Logout", command=self.logout)
        logout_btn.pack(pady=10)

    def view_employee_data(self):
        self.cursor.execute("SELECT * FROM employees")
        employees = self.cursor.fetchall()
        if employees:
            data = ""
            for employee in employees:
                data += f"ID: {employee[1]}\tName: {employee[2]}\tSalary: {employee[3]}\tDepartment: {employee[4]}\tEmail: {employee[5]}\n"
            messagebox.showinfo("Employee Data", data)
        else:
            messagebox.showinfo("Employee Data", "No employees found.")

    def view_top_employees_chart(self):
        self.cursor.execute("SELECT * FROM employees ORDER BY salary DESC LIMIT 5")
        employees = self.cursor.fetchall()
        if employees:
            names = [employee[2] for employee in employees]
            salaries = [employee[3] for employee in employees]
            plt.bar(names, salaries)
            plt.xlabel("Employee Name")
            plt.ylabel("Salary")
            plt.title("Top 5 Employees by Salary")
            plt.show()
        else:
            messagebox.showinfo("Employee Data", "No employees found.")

    def logout(self):
        self.admin_window.destroy()
        self.create_main_window()

    def run(self):
        self.root.mainloop()


ems = EmployeeManagementSystem()
ems.run()
