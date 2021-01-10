#! /usr/bin/env python3

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)

imapObj.select_folder('INBOX', readonly = False)
