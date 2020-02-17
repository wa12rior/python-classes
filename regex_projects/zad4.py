import re

with open('bond.txt') as f:
    for line in f:
        titles = line.split()[:-4]
        date = re.search(r"(\d\d)/(\d\d)/(\d{4})", line)
        year = date.group().split('/')[2]
        print(year + ' ' + ' '.join(titles))
