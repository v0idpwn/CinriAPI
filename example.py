from api_client import CinriConn
TOKEN = ""
KEY = ""
conn = CinriConn(TOKEN, KEY)
print(conn.check_login("johndoe","doe456"))
print(conn.get_user_info(u_name="johndoe"))
