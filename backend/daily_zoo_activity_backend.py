import pyodbc


def insert_attractions_attendance_and_revenue(attractions_id,attractions_name,attraction_show,attendance,revenue):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()

def view_attractions_attendance_and_revenue():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_concessions_daily_revenue(r_id,product,daily_revenue):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_concessions_daily_revenue():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_attendance_numbers_and_revenue(attendance_id,attendance_type,numbers,revenue):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_attendance_numbers_and_revenue():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows

