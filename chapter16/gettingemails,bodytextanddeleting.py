#! /usr/bin/env python3

import pyzmail
# Getting address
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

# Getting Body Text
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)

# Deleting Emails
imapObj.select_folder('INBOX', readonly = False)
UIDs = imapObj.search(['ON 09-Jul-2015'])
print(UIDs)
imapObj.delete_messages(UIDs)
imapObj.expunge()

# Disconnecting from IMAP
imapObj.logout()
