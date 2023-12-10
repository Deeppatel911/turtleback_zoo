import oracledb


def insert_animal(a_id, status, birth_year, s_id, b_id, en_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    s = 'INSERT INTO ANIMAL (AID, STATUS, BIRTHYEAR, SID, BID, EN_ID) VALUES (' + "'" +str(a_id) + "','" + str(
        status) + "'," + "TO_DATE('" + str(birth_year) + "'," + "'YYYY-MM-DD')" + "','" + str(s_id) + "','" + str(b_id) + "','" + str(en_id) + "')"
    cursor.execute(s)
    conn.commit()
    conn.close()


def update_animal(a_id, status, birth_year, s_id, b_id, en_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    s = 'UPDATE ANIMAL SET STATUS =' + "'" + str(status) + "', BIRTHYEAR =" + "TO_DATE('" + str(birth_year) + "'," + "'YYYY-MM-DD')" + "', SID = '" + str(s_id) + "', BID = '" + str(b_id) + "', EN_ID = '" + str(en_id) + "' WHERE AID = '" + str(a_id) + "'"
    print(s)
    cursor.execute(s)
    conn.commit()
    conn.close()


def view_animals():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ANIMAL')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_employee(e_id, fname, minit, lname, street, city, state, zip_val, job_type, start_date, super_id, h_id,
                    r_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    s = "INSERT INTO EMPLOYEE (EID, STARTDATE, JOBTYPE, FIRST, MINIT, LAST, STREET, CITY, STATE, ZIP, SUPER_ID, HID, RID) VALUES ('{0}', TO_DATE('{1}','YYYY-MM-DD'), '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', {9}, '{10}', '{11}', '{12}')".format(e_id,start_date,job_type,fname,minit,lname,street,city,state,zip_val,super_id, h_id,r_id)

    cursor.execute(s)
    conn.commit()
    conn.close()


def update_employee(e_id, fname, minit, lname, street, city, state, zip_val, job_type, start_date, super_id, h_id,
                    r_id):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    s = "UPDATE EMPLOYEE SET STARTDATE = TO_DATE('{0}','YYYY-MM-DD'), JOBTYPE='{1}', FIRST='{2}', MINIT='{3}', LAST='{4}', STREET='{5}', CITY='{6}', STATE='{7}', ZIP={8}, SUPER_ID='{9}', HID='{10}', RID='{11}' WHERE EID = '{11}'".format(start_date,job_type,fname,minit,lname,street,city,state,zip_val,super_id,h_id,r_id,e_id)
    print(s)
    cursor.execute('')
    conn.commit()
    conn.close()


def view_employeesasset():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM EMPLOYEE')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_attraction(atr_id, attraction_name, b_id, building_name, number_of_shows_per_day, child_ticket_price,
                      adult_ticket_price, senior_ticket_price, a_id, number_of_animals):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_attraction(atr_id, attraction_name, b_id, building_name, number_of_shows_per_day, child_ticket_price,
                      adult_ticket_price, senior_ticket_price, a_id, number_of_animals):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_attractions():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_building(b_id, b_name, building_type):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_building(b_id, b_name, building_type):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_buildings():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_hourly_rate(h_id, rate):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def update_hourly_rate(h_id, rate):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    conn.commit()
    conn.close()


def view_hourly_rate():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="ads89", password="NJIT@sds2023", params=params)
    cursor = conn.cursor()
    cursor.execute('')
    rows = cursor.fetchall()
    conn.close()
    return rows
