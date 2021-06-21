import os


#crack de las passwords hasheadas para cada archivo
os.system(r"hashcat  -a 0 -m 0 .\archivo_1 diccionario_2.dict")
os.system(r"hashcat  -a 0 -m 10 .\archivo_2 .\diccionario_2.dict")
os.system(r"hashcat  -a 0 -m  10 .\archivo_3 .\diccionario_2.dict")
os.system(r"hashcat  -a 0 -m 1000 .\archivo_4 .\diccionario_2.dict")
os.system(r"hashcat  -a 0 -m  1800 .\archivo_5 .\diccionario_2.dict")
#Se crea un archivo con las password en texto plano
os.system(r"hashcat --show -a 0 -m 0 .\archivo_1 .\diccionario_2.dict --outfile-format 2 -o passw_archivo1.txt")
os.system(r"hashcat --show -a 0 -m 10 .\archivo_2 .\diccionario_2.dict --outfile-format 2 -o passw_archivo2.txt")
os.system(r"hashcat --show -a 0 -m 10 .\archivo_3 .\diccionario_2.dict --outfile-format 2 -o passw_archivo3.txt")
os.system(r"hashcat --show -a 0 -m 1000 .\archivo_4 .\diccionario_2.dict --outfile-format 2 -o passw_archivo4.txt")
os.system(r"hashcat --show -a 0 -m 1800 .\archivo_5 .\diccionario_2.dict --outfile-format 2 -o passw_archivo5.txt")
