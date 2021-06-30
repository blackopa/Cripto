import imaplib
import re

#datos
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

imap.login('diego.becerra1994@gmail.com', 'password')
imap.select('Inbox')
typ, data = imap.search(None,'FROM', 'info@zmart.cl')#se modifica para cada correo
b=0
for num in data[0].split():
    if b<40:
        typ, data = imap.fetch(num, '(BODY.PEEK[HEADER.FIELDS (MESSAGE-ID)])')
        msg_id= data[0][1].decode()
        msg_id=msg_id.replace("Message-ID:", "")
        msg_id=msg_id.replace(">", "")
        msg_id=msg_id.replace("<", "")
        msg_id=msg_id.replace("Message-Id:", "")
        msg_id=msg_id.strip()
        typ, data = imap.fetch(num, '(BODY.PEEK[HEADER.FIELDS (FROM)])')#se modifica para cada correo
        from_e= data[0][1].decode()
        from_m=from_e.strip()
        from_e=from_e.replace("From: ZMART", "")
        from_e=from_e.replace(">", "")
        from_e=from_e.replace("<", "")
        from_e=from_e.replace("From: ZMART", "")
        from_e=from_e.strip()
        typ, data = imap.fetch(num, '(BODY.PEEK[HEADER.FIELDS (RECEIVED)])')
        received= data[0][1].decode()
        received=received.strip()
        utc=received[-5:] #se modifico para los correos 2 y 5(-5 lo usal es -11), ya que no tiene el (PDT,PST,etc...)
        typ, data = imap.fetch(num, '(BODY.PEEK[HEADER.FIELDS (CONTENT-TYPE)])')
        content_type= data[0][1].decode()
        content_type=content_type.strip()
        with open("msg_id_correo5.txt",'a',encoding = 'utf-8') as p:#se modifica para cada correo
            p.write(msg_id)
            p.write('\n')
        with open ("correos_5.txt",'a',encoding='utf-8') as p:
            p.write('Message-Id:')
            p.write(msg_id)
            p.write('\n')
            p.write(from_m)
            p.write('\n')
            p.write('Email:')
            p.write(from_e)
            p.write('\n')
            p.write(received)
            p.write('\n')
            p.write('UTC:')
            p.write(utc)
            p.write('\n')
            p.write(content_type)
            p.write('##################################################')
            p.write('\n')
        b=b+1
    else:
        break
imap.close()