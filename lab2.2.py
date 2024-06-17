x = int(input("จำนวนคะแนน: "))
if x >= 80 and x <= 100:
    print("เกรด A")
elif x >= 70 and x <= 79:
    print("เกรด B")
elif x >= 60 and x <= 69:
    print("เกรด C")
elif x >= 50 and x <= 59:
    print("เกรด D")
elif x >= 0 and x <= 49:
    print("เกรด F")
else:
    print("กรุณากรอกข้อมูล 0-100")
