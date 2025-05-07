def send_RSA
import smtplib

smtp_server = "smtp.gmail.com"
smtp_port = 587  # Для TLS
email_address = "ваш_email@gmail.com"
password = "ваш_пароль_или_токен"
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart()
message["From"] = email_address
message["To"] = "получатель@example.com"
message["Subject"] = "Тема письма"

body = "Это текст вашего письма."
message.attach(MIMEText(body, "plain"))
