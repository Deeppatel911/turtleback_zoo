import pyodbc

query1="select r1.*,r.subtotal from revenue_type r1,(select rid,sum(revenue) as subtotal from revenue_events where date_time >= TO_DATE('2023-06-01 00:00:00','YYYY-MM-DD HH24:MI:SS') and date_time < TO_DATE('2023-06-02 00:00:00','YYYY-MM-DD HH24:MI:SS') group by rid) r where r1.rid = r.rid;"

q2_sub1="select count(AID),sid,status from animal group by sid,status;"
q2_sub2="SELECT s.NAME AS Species, s.FOODCOST AS MonthlyFoodCost FROM SPECIES s;"
q2_sub3="SELECT e.FIRST || ' ' || e.LAST AS EmployeeName, s.NAME AS SpeciesName, e.JOBTYPE AS Role, hr.RATE AS HourlyRate, COUNT(a.AID) AS NumberofAnimalsAssigned, COUNT(a.AID) * hr.RATE * 40 AS Cost FROM EMPLOYEE e JOIN HOURLY_RATE hr ON e.HID = hr.HID LEFT JOIN CARES_FOR cf ON e.EID = cf.EID LEFT JOIN ANIMAL a ON cf.SID = a.SID LEFT JOIN SPECIES s ON a.SID = s.SID GROUP BY e.EID, e.FIRST, e.LAST, e.JOBTYPE, hr.RATE, s.NAME;"
query2=''

query3="SELECT A.NAME AS AttractionName, SUM(RE.REVENUE) AS TotalRevenue FROM REVENUE_EVENTS RE JOIN REVENUE_TYPE A ON RE.RID = A.RID WHERE RE.DATE_TIME BETWEEN TO_DATE('2023-06-01','YYYY-MM-DD') AND TO_DATE('2023-07-01','YYYY-MM-DD') GROUP BY A.NAME ORDER BY TotalRevenue DESC OFFSET 0 ROWS FETCH FIRST 3 ROWS ONLY;"

query4="SELECT CAST(RE.DATE_TIME AS DATE) AS RevenueDate, SUM(RE.REVENUE) AS TotalRevenue FROM REVENUE_EVENTS RE WHERE EXTRACT(MONTH FROM RE.DATE_TIME) = 6 AND EXTRACT(YEAR FROM RE.DATE_TIME) = 2023 GROUP BY CAST(RE.DATE_TIME AS DATE) ORDER BY TotalRevenue DESC FETCH FIRST 5 ROWS ONLY;"

query5="SELECT A.NAME AS ItemName, AVG(RE.REVENUE) AS AverageRevenue FROM REVENUE_EVENTS RE JOIN REVENUE_TYPE A ON RE.RID = A.RID WHERE RE.DATE_TIME BETWEEN TO_DATE('2023-06-01','YYYY-MM-DD') AND TO_DATE('2023-07-01','YYYY-MM-DD') GROUP BY A.NAME UNION SELECT 'Total Attendance' AS ItemName, AVG(RE.TICKETS_SOLD) AS AverageAttendance FROM REVENUE_EVENTS RE WHERE RE.DATE_TIME BETWEEN TO_DATE('2023-06-01','YYYY-MM-DD') AND TO_DATE('2023-07-01','YYYY-MM-DD');"


def generate_day_revenue_by_source(cal_date):
    print(cal_date)
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def generate_animal_stats():
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def compute_top_attractions_by_revenue(begin_cal_date,end_cal_date):
    print(begin_cal_date)
    print(end_cal_date)
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def compute_month_best_days_revenue(selected_month_item,year):
    print(selected_month_item)
    print(year)
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows


def compute_average_revenue_attraction_concession_totalAttendance(begin_cal_date, end_cal_date):
    print(begin_cal_date)
    print(end_cal_date)
    conn_string="prophet.njit.edu/1521/course;username=djp223;password=Hellodb#12345"
    conn=pyodbc.connect(connstring=conn_string)
    cursor=conn.cursor()
    cursor.execute('')
    rows=cursor.fetchall()
    conn.close()
    return rows
    