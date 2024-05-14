#update delete
import mysql.connector

# เชื่อมต่อกับ MySQL Server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="networkequipment"
)

if connection.is_connected():
    print("เชื่อมต่อกับ MySQL Server สำเร็จ")

# สร้าง cursor object
cursor = connection.cursor()

# คำสั่ง SQL สำหรับลบข้อมูล
sql = "UPDATE equipment SET proid = '6971693270411' WHERE id BETWEEN 140 AND 143;"

# ดำเนินการลบข้อมูลในฐานข้อมูล
cursor.execute(sql)

# ยืนยันการเปลี่ยนแปลง
connection.commit()

# ปิดการเชื่อมต่อ
connection.close()
