#!/usr/bin/python3
"""
Calculate how much each payee has paid from one or more Nordea .txt files
Prints the file name before results
Can be used for example like:
./count.py test_data.txt test_data2.txt >> all_results.txt
"""

import re
import sys

def print_results(data_people_sorted, file_name):
    """Print the results for example like follows.

    FILE_NAME.TXT

    PERSON 1 NAME             : 100.0
    PERSON 2 NAME             : -25.55
    PERSON 3 WITH LONGER NAME : 15.0
    """
    print(file_name.upper(), '\n')
    for i in data_people_sorted:
        print(i["name"].ljust(len(max(names, key=len))) + " : " + str(i["amount"]))
    print()

def parseFields(line):
    """Return date, amount and name"""
    fields = re.split(r'\t+', line)
    date, amount, name = fields[2:5]
    amount = float(amount.replace(',', '.'))
    return date, amount, name

def add_or_edit_person(date, amount, name):
    """Add or edit person in data_people.

    if not person in data_people, add person to data_people
    if person in data_people, update the paid amount
    """
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

def main(argv):
    global data_people
    global names
    try:
        txt_files = argv[1:]
    except:
        print("Usage so far: ./count.py test_data.txt")

    for txt_file in txt_files:
        data_people = []
        names = []
        try:
            with open(txt_file, encoding='utf-8') as f:
                #extract date, amount and name from each line
                #also maintain names-list making it easier to check if the names already exist

                #skip headers
                next(f), next(f), next(f)

                for line in f:
                    ##initial handling
                    #skip empty lines
                    if not line.strip():
                        continue
                    date, amount, name = parseFields(line)
                    add_or_edit_person(date, amount, name)

                try:
                    data_people_sorted = sorted(data_people, key=lambda person: person["name"])
                    print_results(data_people_sorted, f.name)
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

if __name__== "__main__":
    main(sys.argv)
