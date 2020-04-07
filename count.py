#!/usr/bin/python3
"""
Calculate how much each payee has paid from one or more Nordea .txt files
Prints the file name before results
Can be used for example like:
./count.py test_data.txt test_data2.txt >> all_results.txt
Date format: day-month-year
"""

import re
import sys
import os
import datetime

def print_results(data_people_sorted, file_name, start_date, end_date):
    """Print the results for example like follows.

    FILE_NAME
    01.01.2020 – 05.03.2020

    PERSON 1 NAME             : 100.0
    PERSON 2 NAME             : -25.55
    PERSON 3 WITH LONGER NAME : 15.0
    """
    print("----------------------------")
    print(os.path.splitext(file_name)[0].upper()) #strip file extension
    print("%d.%d.%d – %d.%d.%d\n" % (
                            start_date.day, start_date.month, start_date.year,
                            end_date.day, end_date.month, end_date.year))

    for i in data_people_sorted:
        print(i["name"].ljust(len(max(names, key=len))) +
              " : " + str(i["amount"]))
    print()

def parseFields(line):
    """Return date, amount and name"""
    fields = re.split(r'\t+', line)
    date, amount, name = fields[2:5]
    amount = float(amount.replace(',', '.'))

    day, month, year = [int(i) for i in date.split('.')]
    date = datetime.date(year, month, day)
    return date, amount, name

def add_or_edit_person(date, amount, name):
    """Add or edit person in data_people.

    if not person in data_people, add person to data_people
    if person in data_people, update the paid amount
    """
    if name not in names:
        person_new = {}
        person_new.update({"name": name})
        person_new.update({"amount": amount})
        person_new.update({"date": date})
        data_people.append(person_new)
        names.append(name)
    else:
        editPerson = next(filter(lambda person: person['name'] == name,
                                 data_people))
        editPerson["amount"] += amount

def main(argv):
    global data_people
    global names
    if len(argv) <= 1:
        print("Usage: ./count.py test_data.txt [test_data2.txt ...]")
        sys.exit()
    else:
        txt_files = argv[1:]

    for txt_file in txt_files:
        data_people = []
        names = []
        try:
            with open(txt_file, encoding='utf-8') as f:
                #extract date, amount and name from each line
                #maintain names-list for checking if the names already exist
                #grab start_date and update end_date

                #skip headers
                next(f), next(f), next(f), next(f)

                line = f.readline()
                # this is done "manually" to get start_date from first line
                date, amount, name = parseFields(line)
                start_date = date
                add_or_edit_person(date, amount, name)

                for line in f:
                    if not line.strip():
                        continue
                    date, amount, name = parseFields(line)
                    if date >= start_date:
                        end_date = date
                    add_or_edit_person(date, amount, name)
                try:
                    data_people_sorted = sorted(data_people,
                                            key=lambda person: person["name"])
                    print_results(data_people_sorted, f.name,
                                  start_date, end_date)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

if __name__== "__main__":
    main(sys.argv)
