#import pyodbc
#import cx_Oracle;       
import oracledb

#conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
#conn=pyodbc.connect(connstring=conn_string)
#cursor=conn.cursor()

def insert_animal(a_id,status,birth_year,s_id,b_id,en_id):
    # conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    # conn=pyodbc.connect(connstring=conn_string)
    # cursor=conn.cursor()
    # cursor.execute('')
    # conn.commit()
    # conn.close()
    #connection = cx_Oracle.connect('prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345')
    #cur = connection.cursor()
    #queary = 'select * animal;'
    #cur.execute(queary)
    #for result in cur:
    #    print(result)
    #cur.close()
    #connection.close()

    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ANIMAL')

    # Fetch the results
    results = cursor.fetchall()
    print(results)
    #print(conn)
    #print(cursor)
    for row in results:
        print(row)

    conn.close()


def update_animal(a_id,status,birth_year,s_id,b_id,en_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_animals():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ANIMAL')
    rows=cursor.fetchall()

    conn.close()
    return rows


def insert_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_employeesasset():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM EMPLOYEE')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_attraction(atr_id,attraction_name,b_id,building_name,number_of_shows_per_day,child_ticket_price,adult_ticket_price,senior_ticket_price,a_id,number_of_animals):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_attraction(atr_id,attraction_name,b_id,building_name,number_of_shows_per_day,child_ticket_price,adult_ticket_price,senior_ticket_price,a_id,number_of_animals):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_attractions():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_building(b_id,b_name,building_type):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_building(b_id,b_name,building_type):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_buildings():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BUILDING')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_hourly_rate(h_id,rate):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_hourly_rate(h_id,rate):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_hourly_rate():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM HOURLY_RATE')
    rows=cursor.fetchall()
    conn.close()
    return rows

