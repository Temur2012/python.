# 1
import sqlite3
from contextlib import closing

def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def create_employee(database_path, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id))
        connection.commit()
        return cursor.lastrowid


def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
        return cursor.fetchone()


def update_employee(database_path, employee_id, name=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if name:
            cursor.execute("UPDATE employees SET first_name=? WHERE employee_id=?", (name, employee_id))
        connection.commit()


def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))
        connection.commit()

db_path = "sample-database.db"

# employess_create = create_employee(db_path, "Ali", "Valiyev", "ali@gmail.com", "123456789", "2023-01-01", "1", 1000, 1, 1)
# print(employess_create)

# get_employee = get_employee(db_path,207)
# print(get_employee)

# employee_update = update_employee(db_path,207, 'Begzod')
# print(employee_update)

# employee_delete = delete_employee(db_path, 207)






import sqlite3
from contextlib import closing

class BaseCRUD:
    def __init__(self, database_path, table_name):
        self.database_path = database_path
        self.table_name = table_name

    def get_connection(self):
        return closing(sqlite3.connect(self.database_path))


    def insert(self, **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(kwargs.values()))
            connection.commit()
            return cursor.lastrowid


    def get(self, row_id, id_column="employee_id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (row_id,))
            return cursor.fetchone()


    def update(self, row_id, id_column="employee_id", **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(f"{key}=?" for key in kwargs)
            query = f"UPDATE {self.table_name} SET {columns} WHERE {id_column}=?"
            cursor.execute(query, (*kwargs.values(), row_id))
            connection.commit()
            return cursor.rowcount

    def delete(self, row_id, id_column="employee_id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (row_id,))
            connection.commit()
            return cursor.rowcount


db = BaseCRUD(db_path, table_name="employees")

# Insert
# new_id = db.insert(
#     last_name="Aliyev",
#     email="t.aliyev@example.com",
#     hire_date="2026-04-06",
#     job_id=9,
#     salary=4500.0,
#     department_id=6
# )
# print(f"Qo'shilgan ID: {new_id}")



# Get
# print("Yangilangan holat:", db.get(new_id))


# Update
# db.update(new_id, last_name="Valiyev", salary=5000.0)
# print(f"ID {new_id} bo'lgan xodim ma'lumotlari yangilandi.")


# Delete
# db.delete(new_id)
# print(f"ID {new_id} o'chirildi.")