"""

csv_table_tests.py

"""
from collections import OrderedDict

from src.CSVDataTable import CSVDataTable

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../Data/Baseball")


def tests_people():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable("People", connect_info, ["playerID"])
    try:
        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(["abadan01"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(people.find_by_primary_key((["cah2251"])))

        print()
        print("find_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template))

        # delete by key test
        print()
        print("delete_by_key(): Known Record")
        print(people.delete_by_key(["aardsda01"]))

        print()
        print("delete_by_key(): Unknown Record")
        print(people.delete_by_key((["cah2251"])))

        print()
        print("delete_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.delete_by_template(template))

        # update by key test
        template = {"nameFirst": "Andy", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        template_for_update = {"nameFirst": "Andyy", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print()
        print("update_by_key(): Known Record")
        print(people.update_by_key(["abadan01"], template_for_update))

        print()
        print("update_by_key(): Unknown Record")
        print(people.update_by_key((["cah2251"]), template_for_update))

        print()
        print("update_by_template(): Known Template")
        print(people.update_by_template(template_for_update, template))

        # insert by key test
        template = OrderedDict(
            [('playerID', 'aardsda01'), ('birthYear', '1981'), ('birthMonth', '12'), ('birthDay', '27'),
             ('birthCountry', 'USA'), ('birthState', 'CO'), ('birthCity', 'Denver'), ('deathYear', ''),
             ('deathMonth', ''), ('deathDay', ''), ('deathCountry', ''), ('deathState', ''), ('deathCity', ''),
             ('nameFirst', 'David'), ('nameLast', 'Aardsma'), ('nameGiven', 'David Allan'), ('weight', '215'),
             ('height', '75'), ('bats', 'R'), ('throws', 'R'), ('debut', '2004-04-06'), ('finalGame', '2015-08-23'),
             ('retroID', 'aardd001'), ('bbrefID', 'aardsda01')])
        print()
        print("insert(): Known Record")
        print(people.insert(template))

        # Please complete code IN THE SAME FORMAT to test when the rest of methods pass or fail
        # HINT HINT: Don't forget about testing the primary key integrity constraints!!
        # For these tests, think to yourself: When should this fail? When should this pass?

    except Exception as e:
        print("An error occurred:", e)


def tests_batting():
    # Do the same tests for the batting table, so you can ensure your methods work for a table with a composite primary key
    pass  # Replace this line with your tests


tests_people()
tests_batting()
