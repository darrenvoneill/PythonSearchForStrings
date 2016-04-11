import csv

people = ['Joe Bloggs',
'Tim O Reilly',
'Mary Bloggs']


with open('users.csv') as oldfile, open('report.csv', 'w') as newfile:
    for line in oldfile:
        if any(people in line for people in people):
            newfile.write(line)
