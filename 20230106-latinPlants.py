import csv
from sys import stdin

# inp = """Adonis	sibirica	Patrin ex Ledeb	Стародубка сибирская	Ranunculaceae	Лютиковые
# Artemisia	laciniata	Willd.	Полынь рассеченная	Asteraceae	Астровые
# Cypripedium	guttatum	Sw.	Башмачок капельный	Orchidaceae	Орхидные
# Galium	uliginosum	L.	Подмаренник топяной	Rubiaceae	Мареновые
# Geum	rivale	L.	Гравилат речной	Rosaceae	Розоцветные"""

with open('plantis.csv', 'w', newline="") as f:
    c = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL, quotechar="'")
    c.writerow(["nomen", "definitio", "pluma", "Russian nomen", "familia", "Russian nomen familia"])
    for r in stdin:
        c.writerow([value for value in r.rstrip().split("\t")])
