import sqlite3

con = sqlite3.connect(input()) 
selch = input() # narrator
ys1 = input() # location == 'Caribbean sea'
so = input() # AND
ys2 = input() # year < 1780
cur = con.cursor()
q =f'SELECT {selch} FROM Stories f WHERE {ys1} {so} {ys2}'
result = cur.execute(q).fetchall()
for elem in result:
    print(elem[0])
con.close()
