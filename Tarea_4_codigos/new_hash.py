import bcrypt
import time
import base64

salt = bcrypt.gensalt(rounds=16) 

f = open("passw_archivo5.txt",'r',encoding = 'utf-8')

start = time.time()
for line in f:
	hashed = bcrypt.hashpw(f.readline().encode('utf-8'), salt)
	with open("new_hash_archivo5.txt",'a',encoding = 'utf-8') as p:
		p.write(hashed.decode('utf-8'))
		p.write('\n')
end = time.time()
f.close()
print(end - start)