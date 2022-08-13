import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('parleg10rs@gmail.com', '')
server.sendmail('parleg10rs@gmail.com', 'adeshgadekar98@gmail.com', 'mail sent from python code')