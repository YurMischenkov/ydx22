import csv


# date;time;luminosity;color
with open('alpha_oriona.csv', newline='') as csvfile:
    r = csv.reader(csvfile, delimiter=';', quotechar='"')
    prevLum = -1
    startDate = ""
    startTime = ""
    duration = 1
    seq = [0, ""]
    for index, row in enumerate(r):
        if index == 0: 
            continue
        lum = int(row[2])
        if lum <= prevLum:
            duration += 1
        else:
            if duration > seq[0]:
                seq = [duration, startDate + ' ' + startTime]
            duration = 1
            startDate = row[0]
            startTime = row[1]
        prevLum = lum

    if duration > 0:
        if duration > seq[0]:
            seq = [duration, startDate + ' ' + startTime]

    with open('result.txt', 'w') as resFile:
        resFile.write("\n".join(map(str, seq)))

