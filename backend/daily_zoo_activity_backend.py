from Connection.Oracle_Connection import get_connection


def insert_attractions_attendance_and_revenue(attractions_id, date, attendance, revenue):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO REVENUE_EVENTS (RID, DATE_TIME, REVENUE, TICKETS_SOLD) VALUES ('{0}', TO_DATE('{1}',"
                   "'YYYY-MM-DD HH24:MI:SS'), {2}, {3})".format(attractions_id, date, revenue, attendance))
    conn.commit()
    conn.close()


def view_attractions_attendance_and_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT R.RID, TRUNC(R.DATE_TIME), SUM(R.REVENUE), SUM(R.TICKETS_SOLD) FROM REVENUE_EVENTS R JOIN '
                   'ANIMAL_SHOWS A ON R.RID=A.RID GROUP BY R.RID,TRUNC(R.DATE_TIME)')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_concessions_daily_revenue(r_id, product):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CONCESSION (RID, PRODUCT) VALUES ('{0}', '{1}')".format(r_id, product))
    conn.commit()
    print('Concession inserted')
    conn.close()


def view_concessions_daily_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT C.RID, C.PRODUCT, SUM(R.REVENUE) FROM CONCESSION C JOIN REVENUE_EVENTS R ON R.RID = C.RID '
                   'GROUP BY C.RID,C.PRODUCT,TRUNC(R.DATE_TIME) ORDER BY C.RID, TRUNC(R.DATE_TIME)')
    rows = cursor.fetchall()
    conn.close()
    return rows


def insert_attendance_numbers_and_revenue(attendance_id, date, numbers, revenue):
    conn = get_connection()
    cursor = conn.cursor()
    s = ("INSERT INTO REVENUE_EVENTS (RID, DATE_TIME, REVENUE, TICKETS_SOLD) VALUES ('{0}', TO_DATE('{1}','YYYY-MM-DD "
         "HH24:MI:SS'), {2}, {3})").format(attendance_id, date, revenue, numbers)
    cursor.execute(s)
    conn.commit()
    conn.close()


def view_attendance_numbers_and_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Z.RID, TRUNC(R.DATE_TIME), SUM(R.TICKETS_SOLD), SUM(R.REVENUE) FROM ZOO_ADMISSION Z JOIN '
                   'REVENUE_EVENTS R ON R.RID = Z.RID GROUP BY Z.RID,TRUNC(R.DATE_TIME) ORDER BY Z.RID, '
                   'TRUNC(R.DATE_TIME)')
    rows = cursor.fetchall()
    conn.close()
    return rows
