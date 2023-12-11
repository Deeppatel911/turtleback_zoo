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
    cursor.execute(f"INSERT INTO ANIMAL (AID, STATUS, BIRTHYEAR, SID, BID, EN_ID) VALUES ('{a_id}', '{status}', '{birth_year}', '{s_id}', '{b_id}', '{en_id}')")
    conn.commit()
    print('Animal inserted')
    conn.close()


def update_animal(a_id,status,birth_year,s_id,b_id,en_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    s = 'UPDATE ANIMAL SET STATUS =' + "'" + str(status) + "', BIRTHYEAR =" + "TO_DATE('" + str(birth_year) + "'," + "'YYYY-MM-DD')" + "', SID = '" + str(s_id) + "', BID = '" + str(b_id) + "', EN_ID = '" + str(en_id) + "' WHERE AID = '" + str(a_id) + "'"
    print(s)
    cursor.execute(s)
    conn.commit()
    print('Animal updated')
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
    cursor.execute("INSERT INTO EMPLOYEE (EID, STARTDATE, JOBTYPE, FIRST, MINIT, LAST, STREET, CITY, STATE, ZIP, SUPER_ID, HID, RID) VALUES ('{0}', TO_DATE('{1}','YYYY-MM-DD'), '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', {9}, '{10}', '{11}', '{12}')".format(e_id,start_date,job_type,fname,minit,lname,street,city,state,zip_val,super_id, h_id,r_id))
    conn.commit()
    print('Employee inserted')
    conn.close()


def update_employee(e_id,fname,minit,lname,street,city,state,zip_val,job_type,start_date,super_id,h_id,r_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    s = "UPDATE EMPLOYEE SET STARTDATE = TO_DATE('{0}','YYYY-MM-DD'), JOBTYPE='{1}', FIRST='{2}', MINIT='{3}', LAST='{4}', STREET='{5}', CITY='{6}', STATE='{7}', ZIP={8}, SUPER_ID='{9}', HID='{10}', RID='{11}' WHERE EID = '{11}'".format(start_date,job_type,fname,minit,lname,street,city,state,zip_val,super_id,h_id,r_id,e_id)
    print(s)
    cursor.execute(s)
    conn.commit()
    print('Employee Updated')
    conn.close()


def view_employees():
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
    cursor.execute(f"INSERT INTO BUILDING (BID, NAME, TYPE) VALUES ('{b_id}','{b_name}','{building_type}')")
    conn.commit()
    print('Building inserted')
    conn.close()


def update_building(b_id,b_name,building_type):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    s = f"UPDATE BUILDING SET NAME = '{b_name}', TYPE = '{building_type}' WHERE BID = '{b_id}'"
    print(s)
    cursor.execute(s)
    conn.commit()
    print('Building updated')
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
    cursor.execute(f"INSERT INTO HOURLY_RATE (HID, RATE) VALUES ('{h_id}','{rate}')")
    conn.commit()
    print('Hourly Rate inserted')
    conn.close()


def update_hourly_rate(h_id,rate):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    s = f"UPDATE HOURLY_RATE SET RATE = '{rate}' WHERE HID = '{h_id}'"
    print(s)
    cursor.execute(s)
    conn.commit()
    print('Hourly Rate updated')
    conn.close()


def view_hourly_rate():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM HOURLY_RATE')
    rows=cursor.fetchall()
    conn.close()
    return rows

