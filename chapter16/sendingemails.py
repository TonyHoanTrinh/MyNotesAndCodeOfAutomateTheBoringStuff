#! /usr/bin/env python3

import smtplib

smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
print(type(smtpObj))
print(smtpObj.ehlo())
print(smtpObj.starttls())
smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()
