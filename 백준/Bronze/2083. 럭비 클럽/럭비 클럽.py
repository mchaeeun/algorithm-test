import sys

for line in sys.stdin:
    line = line.split()
    if line == ['#', '0', '0']:
        break
    members_status = "Junior"
    if int(line[1]) > 17:
        members_status = "Senior"
    elif int(line[2]) >= 80:
        members_status = "Senior"
    print(line[0], members_status)