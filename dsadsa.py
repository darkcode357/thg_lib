import psycopg2 
conn = psycopg2.connect(host="192.168.222.20",port=6554,database="dbsimec", user="simec", password="phpsimecalt")
b = cur = conn.cursor()
a = cur.execute('SELECT version()')
db_version = cur.fetchone()
print(b)
print(a)
print(db_version)
