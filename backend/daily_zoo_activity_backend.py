#import pyodbc
import oracledb


def insert_attractions_attendance_and_revenue(attractions_id,attractions_name,attraction_show,attendance,revenue):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BUILDING')
    conn.close()


def view_attractions_attendance_and_revenue():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BUILDING')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_concessions_daily_revenue(r_id,product,daily_revenue):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO CONCESSION (RID, PRODUCT) VALUES ('{r_id}', '{product}')".format(r_id,product))
    conn.commit()
    print('Concession inserted')
    conn.close()


def view_concessions_daily_revenue():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM CONCESSION')
    rows=cursor.fetchall()
    conn.close()
    return rows


def insert_attendance_numbers_and_revenue(attendance_id,attendance_type,numbers,revenue):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BUILDING')
    conn.close()


def view_attendance_numbers_and_revenue():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM BUILDING')
    rows=cursor.fetchall()
    conn.close()
    return rows

