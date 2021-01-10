#! /usr/bin/env python3

import imapclient
imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl = True)
imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')
import pprint
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly = True)
UIDs = imapObj.search(['SINCE 05-Jul-2014'])
print(UIDs)
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])

import imaplib
imaplib._MAXLINE = 10000000

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_address('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))
print(message.text_part != NONE)
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part != NONE)
print(message.html_part.get_payload().decode(message.html_part.charset))
imapObj.logout()
