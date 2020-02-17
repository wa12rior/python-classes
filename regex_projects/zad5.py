import re
from datetime import datetime as dt

with open('bond.txt') as f:
    for line in f:
        titles = ' '.join(line.split()[:-4])
        date = re.search(r"(\d\d)/(\d\d)/(\d{4})", line)
        date = dt.strptime(date.group(), '%d/%m/%Y')
        now = dt.now()
        diff = (now - date).days
        print(titles + '\t' + str(diff))
