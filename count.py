#!/usr/bin/python3
"""
Calculate how much each payee has paid from a .txt gotten from Nordea
"""

import re
import sys

data_people = []
names = []
txt_file = ""

def print_results(data_people_sorted):
    for i in data_people_sorted:
        print(i["name"].ljust(len(max(names, key=len))) + " : " + str(i["amount"]))

def parseFields(line):
    #return date, amount and name
    fields = re.split(r'\t+', line)
    date, amount, name = fields[2:5]
    amount = float(amount.replace(',', '.'))
    return date, amount, name

def main():
    global data_people
    global names
    global txt_file
    try:
        txt_file = sys.argv[1]
    except:
        print("Usage so far: ./count.py test_data.txt")

    try:
        with open(txt_file, encoding='utf-8') as f:
            #extract date, amount and name from each line
            #if not person in data_people, add people to data_people
            #if person in data_people, update the paid amount
            #also maintain names-list making it easier to check if the names already exist

            #skip headers
            next(f), next(f), next(f)

            for line in f:
                ##initial handling
                #skip empty lines
                if not line.strip():
                    continue
                date, amount, name = parseFields(line)

                #add or edit person in data_people
                if name not in names:
                    newPerson = {}
                    newPerson.update({"name": name})
                    newPerson.update({"amount": amount})
                    newPerson.update({"date": date})
                    data_people.append(newPerson)
                    names.append(name)
                else:
                    editPerson = next(filter(lambda person: person['name'] == name,
                                             data_people))
                    editPerson["amount"] += amount
    except Exception as e:
        print(e)

    try:
        data_people_sorted = sorted(data_people, key=lambda person: person["name"])
        print_results(data_people_sorted)
    except Exception as e:
        print(e)

if __name__== "__main__":
    main()
