# 🧩 Assignment: Aggregation – Department and Employee

## 🎯 Objective
Create a class `Department` and a class `Employee`. Use **aggregation** by having a `Department` object store a reference to an `Employee` object that exists independently of it.

---

## ✅ Python Code (`app.py`)

```python
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"


class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: storing a reference

    def show_department_info(self):
        return f"Department: {self.department_name} | {self.employee.get_details()}"


# Example usage
emp1 = Employee("Ali", 101)
dept1 = Department("IT", emp1)

print(dept1.show_department_info())

🧠 Explanation
Aggregation means a class (e.g., Department) contains a reference to another class (Employee), but that referenced object can exist independently.

The Employee instance is created first and then passed to the Department.

If the Department is deleted, the Employee can still exist.

🖥️ Output
Department: IT | Employee Name: Ali, ID: 101
