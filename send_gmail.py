def send_RSA(email_address, password, text, reciever_email):
    #на вход даются строки str
    import smtplib
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    message = MIMEMultipart()
    message["From"] = email_address
    message["To"] = reciever_email
    message.attach(MIMEText(text, "plain"))
    try:
       server = smtplib.SMTP(smtp_server, smtp_port)
       server.starttls()  
       server.login(email_address, password)
       server.sendmail(email_address, reciever_email, message.as_string())
       print("Письмо отправлено!")
    except:
       print("Ошибка")
    finally:
       server.quit()
