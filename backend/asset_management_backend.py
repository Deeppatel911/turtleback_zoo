import pyodbc

#conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
#conn=pyodbc.connect(connstring=conn_string)
#cursor=conn.cursor()

def insert_animal(a_id,status,birth_year,s_id,b_id,en_id):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_animal(a_id,status,birth_year,s_id,b_id,en_id):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_animals():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_employeesasset():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_attraction(atr_id,attraction_name,b_id,building_name,number_of_shows_per_day,child_ticket_price,adult_ticket_price,senior_ticket_price,a_id,number_of_animals):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_attraction(atr_id,attraction_name,b_id,building_name,number_of_shows_per_day,child_ticket_price,adult_ticket_price,senior_ticket_price,a_id,number_of_animals):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_attractions():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_building(b_id,b_name,building_type):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_building(b_id,b_name,building_type):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_buildings():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_hourly_rate(h_id,rate):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_hourly_rate(h_id,rate):
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_hourly_rate():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows
