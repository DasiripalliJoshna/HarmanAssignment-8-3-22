import sqlite3
connection = sqlite3.connect("hospital.db")
res = connection.execute(" SELECT * FROM DOCTOR ")
for i in res:
    print("Id",i[0])
    print("Doctors Name: ", i[1])
    print("Doctors Qualification: ", i[2])
    print("Doctors Address: ", i[3])
    print(" Doctors Phone number: ", i[4])
    print("Doctors Email ID: ", i[5])
    print("*********$$$$$$***********")
