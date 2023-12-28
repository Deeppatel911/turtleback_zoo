import oracledb


def get_connection():
    params = oracledb.ConnectParams(host="prophet.njit.edu", port=1521, sid='course')
    conn = oracledb.connect(user="", password="", params=params)
    return conn
