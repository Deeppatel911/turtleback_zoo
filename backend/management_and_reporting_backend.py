#import pyodbc
import oracledb


def generate_day_revenue_by_source(cal_date):
    print(cal_date)
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()

    query1=f"select r1.*,r.subtotal from revenue_type r1,(select rid,sum(revenue) as subtotal from revenue_events where date_time >= TO_DATE('{cal_date}','YYYY-MM-DD') and date_time < TO_DATE('2023-06-02','YYYY-MM-DD') group by rid) r where r1.rid = r.rid".format(cal_date)
    cursor.execute(query1)
    rows=cursor.fetchall()
    conn.close()
    return rows


def generate_animal_stats():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    query2 = """
            SELECT
                e.FIRST || ' ' || e.LAST AS EmployeeName,
                s.NAME AS SpeciesName,
                e.JOBTYPE AS Role,
                hr.RATE AS HourlyRate,
                COUNT(a.AID) AS NumberofAnimalsAssigned,
                COUNT(a.AID) * hr.RATE * 40 AS Cost
            FROM
                EMPLOYEE e
            JOIN
                HOURLY_RATE hr ON e.HID = hr.HID
            LEFT JOIN
                CARES_FOR cf ON e.EID = cf.EID
            LEFT JOIN
                ANIMAL a ON cf.SID = a.SID
            LEFT JOIN
                SPECIES s ON a.SID = s.SID
            GROUP BY
                e.EID, e.FIRST, e.LAST, e.JOBTYPE, hr.RATE, s.NAME
            """
    cursor.execute(query2)
    rows=cursor.fetchall()
    conn.close()
    return rows


def compute_top_attractions_by_revenue(begin_cal_date,end_cal_date):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute(f"SELECT A.NAME AS AttractionName, SUM(RE.REVENUE) AS TotalRevenue FROM REVENUE_EVENTS RE JOIN REVENUE_TYPE A ON RE.RID = A.RID WHERE RE.DATE_TIME BETWEEN TO_DATE('{begin_cal_date} 00:00:00','YYYY-MM-DD HH24:MI:SS') AND TO_DATE('{end_cal_date} 00:00:00','YYYY-MM-DD HH24:MI:SS') GROUP BY A.NAME ORDER BY TotalRevenue DESC OFFSET 0 ROWS FETCH FIRST 3 ROWS ONLY"
.format(begin_cal_date,end_cal_date))
    rows=cursor.fetchall()
    print(rows)
    conn.close()
    return rows


def compute_month_best_days_revenue(selected_month_item,year):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute(f"SELECT CAST(RE.DATE_TIME AS DATE) AS RevenueDate, SUM(RE.REVENUE) AS TotalRevenue FROM REVENUE_EVENTS RE WHERE EXTRACT(MONTH FROM RE.DATE_TIME) = '{selected_month_item}' AND EXTRACT(YEAR FROM RE.DATE_TIME) = '{year}' GROUP BY CAST(RE.DATE_TIME AS DATE) ORDER BY TotalRevenue DESC FETCH FIRST 5 ROWS ONLY"
.format(selected_month_item,year))
    rows=cursor.fetchall()
    conn.close()
    return rows


def compute_average_revenue_attraction_concession_totalAttendance(begin_cal_date, end_cal_date):
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521,sid='course')
    conn = oracledb.connect(user="djp223", password="Hellodatabase#123",params=params)
    cursor = conn.cursor()
    cursor.execute(f"SELECT A.NAME AS ItemName, AVG(RE.REVENUE) AS AverageRevenue FROM REVENUE_EVENTS RE JOIN REVENUE_TYPE A ON RE.RID = A.RID WHERE RE.DATE_TIME BETWEEN TO_DATE('{begin_cal_date}','YYYY-MM-DD') AND TO_DATE('{end_cal_date}','YYYY-MM-DD') GROUP BY A.NAME UNION SELECT 'Total Attendance' AS ItemName, AVG(RE.TICKETS_SOLD) AS AverageAttendance FROM REVENUE_EVENTS RE WHERE RE.DATE_TIME BETWEEN TO_DATE('2023-06-01','YYYY-MM-DD') AND TO_DATE('2023-07-01','YYYY-MM-DD')"
.format(begin_cal_date,end_cal_date))
    rows=cursor.fetchall()
    conn.close()
    return rows
