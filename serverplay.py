import smtplib
import ssl
from email.message import EmailMessage

import openpyxl as xl
from PyQt5.QtCore import QDate

today = QDate.currentDate()
today = [today.month(), today.day()]
wb = xl.load_workbook("teachers.xlsx")
sheet = wb["Sheet1"]
data = eval(sheet["A1"].value)
wb2 = xl.load_workbook("children.xlsx")
sheet2 = wb2["Sheet1"]
data2 = eval(sheet2["A1"].value)
sent = False
while sent != True:
    for i in data.keys():
        info = data[i]
        students = info['students']
        for i2 in students:
            student = data2[i2]
            birthday = student['date of birth']
            listed = str(birthday).split("/")
            birthday = QDate(int(listed[2]), int(listed[0]), int(listed[1]))
            birthday = [birthday.month(), birthday.day()]
            if birthday == today:
                port = 465
                smtp_server = "smtp.gmail.com"
                msg = EmailMessage()
                if student['gender'] == 'f':
                    r = 'her'
                else:
                    r = 'him'
                msg.set_content(f"Today is {student['name']}'s birthday, Wish {r} a happy birthday\n")

                msg['Subject'] = 'Birthday Message'
                msg['From'] = "orieozichi@gmail.com"
                msg['To'] = info["email"]

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login("orieozichi@gmail.com", "growingbetter985")
                    server.send_message(msg)
                    sent = True
                    server.quit()