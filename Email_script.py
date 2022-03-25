
import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("xxx@gmail.com", "insira senha gerada")

mensagem = """From:<xxx29@gmail.com>
To:<yyy@gmail.com>
Subject: Python está te enviando este email

O meu Script python está lhe enviando este email como forma de teste.
"""



server.sendmail(
    "xxx@gmail.com",
    "yyy@gmail.com",
    mensagem)
server.quit()


