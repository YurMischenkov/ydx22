import csv
import sqlite3

name = input()
yearfrom, yearto = input().split(' ')

con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute(
    f"""select ship, captain, navigator, year, s.benefit
        from ships s
        join navigators n
        on s.id_navigator = n.id_navigator
        join captains c
        on s.id_cap = c.id_cap
        where c.captain = "Billy Bons"
        or n.navigator = "Billy Bons"
        and year between {yearfrom} and {yearto}""")

with open('pirates.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=';')
    # wr.writerow(['корабль', 'капитан', 'штурман', 'год', 'добыча'])
    for elem in result:
        wr.writerow(map(str, elem))

con.close()
