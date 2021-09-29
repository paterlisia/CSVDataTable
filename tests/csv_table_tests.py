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
    print("This is the test cases for people table")
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable("People", connect_info, ["playerID"])
    try:
        # -------------find existed record by primary key-----------
        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(["aaronha01"]))

        # -------------find non-existed record by primary key-----------
        print()
        print("find_by_primary_key(): find non-existed record by primary key")
        print(people.find_by_primary_key((["cah2251"])))

        # -------------find existed record by template-----------
        print()
        print("find_by_template(): find existed record by template")
        template = {"nameFirst": "Hank", "nameLast": "Aaron", "nameGiven": "Henry Louis"}
        print(people.find_by_template(template))

        # -------------delete existed record by primary key-----------
        print()
        print("delete_by_key(): delete existed record by primary key")
        print(people.delete_by_key(["aardsda01"]))
        template = OrderedDict(
            [('playerID', 'aardsda01'), ('birthYear', '1981'), ('birthMonth', '12'), ('birthDay', '27'),
             ('birthCountry', 'USA'), ('birthState', 'CO'), ('birthCity', 'Denver'), ('deathYear', ''),
             ('deathMonth', ''), ('deathDay', ''), ('deathCountry', ''), ('deathState', ''), ('deathCity', ''),
             ('nameFirst', 'David'), ('nameLast', 'Aardsma'), ('nameGiven', 'David Allan'), ('weight', '215'),
             ('height', '75'), ('bats', 'R'), ('throws', 'R'), ('debut', '2004-04-06'), ('finalGame', '2015-08-23'),
             ('retroID', 'aardd001'), ('bbrefID', 'aardsda01')])
        people.insert(template)  # insert deleted one

        # -------------delete non-existed record by primary key-----------
        print()
        print("delete_by_key(): delete non-existed record by primary key")
        print(people.delete_by_key((["cah2251"])))

        # -------------delete existed record by template-----------
        print()
        print("delete_by_template(): delete existed record by template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.delete_by_template(template))

        # -------------update existed record by primary key and pk not updated-----------
        # update by key test
        template_for_update = {"nameFirst": "Andyy", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print()
        print("update_by_key(): update existed record by primary key and pk not updated")
        print(people.update_by_key(["abadan01"], template_for_update))

        # -------------update non-existed record by primary key and pk not updated-----------
        print()
        print("update_by_key(): update non-existed record by primary key")
        print(people.update_by_key((["cah2251"]), template_for_update), "rows updated")

        # -------------update existed record by primary key and pk updated-----------
        print()
        print("update_by_key(): update existed record by primary key and pk updated")
        template_for_update_duplicated_pk = {"playerID": "abbeybe01", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print(people.update_by_key((["abadan01"]), template_for_update_duplicated_pk), "rows updated")

        # -------------update existed record by template and pk not updated-----------
        print()
        print("update_by_template(): update existed record by template and pk not updated")
        template_existed = {"nameFirst": "Andyy", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        template_for_update = {"nameFirst": "Andy", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print(people.update_by_template(template_existed, template_for_update))

        # -------------update non-existed record by template and pk updated-----------
        print()
        print("update_by_template(): update non-existed record by template and pk updated")
        template_for_non_existed = {"playerID": "121", "nameLast": "ads", "nameGiven": "fdsaf"}
        template_for_update_duplicated_pk = {"playerID": "abbeybe01", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print(people.update_by_template(template_for_non_existed, template_for_update_duplicated_pk))

        # -------------update existed record by template and pk updated and existed-----------
        print()
        print("update_by_template(): update existed record by template and pk updated and existed")
        template_existed = {"nameFirst": "Andy", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        template_for_update_duplicated_pk = {"playerID": "abbeybe01", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print(people.update_by_template(template_existed, template_for_update_duplicated_pk))

        # insert by key test
        # -------------insert a new record without duplicate----------------------------------
        template = OrderedDict(
            [('playerID', 'aardsda01'), ('birthYear', '1981'), ('birthMonth', '12'), ('birthDay', '27'),
             ('birthCountry', 'USA'), ('birthState', 'CO'), ('birthCity', 'Denver'), ('deathYear', ''),
             ('deathMonth', ''), ('deathDay', ''), ('deathCountry', ''), ('deathState', ''), ('deathCity', ''),
             ('nameFirst', 'David'), ('nameLast', 'Aardsma'), ('nameGiven', 'David Allan'), ('weight', '215'),
             ('height', '75'), ('bats', 'R'), ('throws', 'R'), ('debut', '2004-04-06'), ('finalGame', '2015-08-23'),
             ('retroID', 'aardd001'), ('bbrefID', 'aardsda01')])
        print()
        print("insert(): new record")
        print(people.insert(template))
        # -------------insert a new record without duplicate----------------------------------
        template_duplicate_record = OrderedDict(
            [('playerID', 'aardsda01'), ('birthYear', '1981'), ('birthMonth', '12'), ('birthDay', '27'),
             ('birthCountry', 'USA'), ('birthState', 'CO'), ('birthCity', 'Denver'), ('deathYear', ''),
             ('deathMonth', ''), ('deathDay', ''), ('deathCountry', ''), ('deathState', ''), ('deathCity', ''),
             ('nameFirst', 'David'), ('nameLast', 'Aardsma'), ('nameGiven', 'David Allan'), ('weight', '215'),
             ('height', '75'), ('bats', 'R'), ('throws', 'R'), ('debut', '2004-04-06'), ('finalGame', '2015-08-23'),
             ('retroID', 'aardd001'), ('bbrefID', 'aardsda01')])
        print()
        print("insert(): new record")
        print(people.insert(template_duplicate_record))
        # -------------insert a new record without duplicate----------------------------------
        template_duplicate_pk = OrderedDict(
            [('playerID', 'aardsda01'), ('birthYear', '1919'), ('birthMonth', '12'), ('birthDay', '27'),
             ('birthCountry', 'USA'), ('birthState', 'CO'), ('birthCity', 'Denver'), ('deathYear', ''),
             ('deathMonth', ''), ('deathDay', ''), ('deathCountry', ''), ('deathState', ''), ('deathCity', ''),
             ('nameFirst', 'David'), ('nameLast', 'Aardsma'), ('nameGiven', 'David Allan'), ('weight', '215'),
             ('height', '75'), ('bats', 'R'), ('throws', 'R'), ('debut', '2004-04-06'), ('finalGame', '2015-08-23'),
             ('retroID', 'aardd001'), ('bbrefID', 'aardsda01')])
        print()
        print("insert(): new record")
        print(people.insert(template_duplicate_pk))

        # Please complete code IN THE SAME FORMAT to test when the rest of methods pass or fail
        # HINT HINT: Don't forget about testing the primary key integrity constraints!!
        # For these tests, think to yourself: When should this fail? When should this pass?

    except Exception as e:
        print("An error occurred:", e)


def tests_batting():
    # Do the same tests for the batting table, so you can ensure your methods work for a table with a composite
    # primary key
    print("This is the test cases for batting table")
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    batting = CSVDataTable("Batting", connect_info, ["playerID", "yearID", "stint"])
    try:
        # -------------find existed record by primary key-----------
        print()
        print("find_by_primary_key(): Known Record")
        print(batting.find_by_primary_key(["abercda01", "1871", "1"]))

        # -------------find non-existed record by primary key-----------
        print()
        print("find_by_primary_key(): find non-existed record by primary key")
        print(batting.find_by_primary_key((["ch2251", "1871", "1"])))

        # -------------find existed record by template-----------
        print()
        print("find_by_template(): find existed record by template")
        template = {"teamID": "TRO", "lgID": "NA", "G": "1"}
        print(batting.find_by_template(template))

        # -------------delete existed record by primary key-----------
        print()
        print("delete_by_key(): delete existed record by primary key")
        print(batting.delete_by_key(["abercda01", "1871", "1"]))
        template = OrderedDict([('playerID', 'abercda01'), ('yearID', '1871'), ('stint', '1'), ('teamID', 'TRO'), ('lgID', 'NA'), ('G', '1'), ('AB', '4'), ('R', '0'), ('H', '0'), ('2B', '0'), ('3B', '0'), ('HR', '0'), ('RBI', '0'), ('SB', '0'), ('CS', '0'), ('BB', '0'), ('SO', '0'), ('IBB', ''), ('HBP', ''), ('SH', ''), ('SF', ''), ('GIDP', '0')])

        batting.insert(template)  # insert deleted one

        # -------------delete non-existed record by primary key-----------
        print()
        print("delete_by_key(): delete non-existed record by primary key")
        print(batting.delete_by_key((["cah2251", "1871", "1"])))

        # -------------delete existed record by template-----------
        print()
        print("delete_by_template(): delete existed record by template")
        template = {"playerID": "abercda01", "yearID": "1871", "stint": "1", "teamID": "TRO", "lgID": "NA", "G": "1"}
        print(batting.delete_by_template(template))

        # -------------update existed record by primary key and pk not updated-----------
        # update by key test
        template_for_update = {"teamID": "WS4", "lgID": "NA", "G": "27"}
        print()
        print("update_by_key(): update existed record by primary key and pk not updated")
        print(batting.update_by_key(["allisdo01", "1871", "1"], template_for_update))

        # -------------update non-existed record by primary key and pk not updated-----------
        print()
        print("update_by_key(): update non-existed record by primary key")
        print(batting.update_by_key((["cah2251"]), template_for_update), "rows updated")

        # -------------update existed record by primary key and pk updated-----------
        print()
        print("update_by_key(): update existed record by primary key and pk updated")
        template_for_update_duplicated_pk = {"playerID": "ansonca01", "yearID": "1871", "stint": "1", "G": "27"}
        print(batting.update_by_key((["allisdo01", "1871", "1"]), template_for_update_duplicated_pk), "rows updated")

        # -------------update existed record by template and pk not updated-----------
        print()
        print("update_by_template(): update existed record by template and pk not updated")
        template_existed = {"playerID": "allisdo01", "yearID": "1871", "stint": "1", "teamID": "WS4", "lgID": "NA", "G": "27"}
        template_for_update = {"teamID": "WS3", "lgID": "NA", "G": "27"}
        print(batting.update_by_template(template_existed, template_for_update))

        # -------------update non-existed record by template and pk updated-----------
        print()
        print("update_by_template(): update non-existed record by template and pk updated")
        template_for_non_existed = {"playerID": "anssadasonca01", "yearID": "1871", "stint": "1", "teamID": "WS4", "lgID": "NA", "G": "27"}
        template_for_update_duplicated_pk = {"playerID": "abbeybe01", "nameLast": "Abad", "nameGiven": "Fausto Andres"}
        print(batting.update_by_template(template_for_non_existed, template_for_update_duplicated_pk))

        # -------------update existed record by template and pk updated and existed-----------
        print()
        print("update_by_template(): update existed record by template and pk updated and existed")
        template_existed = {"playerID": "allisdo01", "yearID": "1871", "stint": "1", "G": "27"}
        template_for_update_duplicated_pk = {"playerID": "ansonca01", "yearID": "1871", "stint": "1", "G": "27"}
        print(batting.update_by_template(template_existed, template_for_update_duplicated_pk))

        # insert by key test
        # -------------insert a new record without duplicate----------------------------------
        template = OrderedDict([('playerID', 'abercda01'), ('yearID', '1871'), ('stint', '1'), ('teamID', 'TRO'), ('lgID', 'NA'), ('G', '1'), ('AB', '4'), ('R', '0'), ('H', '0'), ('2B', '0'), ('3B', '0'), ('HR', '0'), ('RBI', '0'), ('SB', '0'), ('CS', '0'), ('BB', '0'), ('SO', '0'), ('IBB', ''), ('HBP', ''), ('SH', ''), ('SF', ''), ('GIDP', '0')])

        print()
        print("insert(): new record")
        print(batting.insert(template))
        # -------------insert a new record without duplicate----------------------------------
        template_duplicate_record = OrderedDict([('playerID', 'abercda01'), ('yearID', '1871'), ('stint', '1'), ('teamID', 'TRO'), ('lgID', 'NA'), ('G', '1'), ('AB', '4'), ('R', '0'), ('H', '0'), ('2B', '0'), ('3B', '0'), ('HR', '0'), ('RBI', '0'), ('SB', '0'), ('CS', '0'), ('BB', '0'), ('SO', '0'), ('IBB', ''), ('HBP', ''), ('SH', ''), ('SF', ''), ('GIDP', '0')])

        print()
        print("insert(): new record")
        print(batting.insert(template_duplicate_record))
        # -------------insert a new record without duplicate----------------------------------
        template_duplicate_pk = OrderedDict([('playerID', 'abercda01'), ('yearID', '1871'), ('stint', '1'), ('teamID', 'TRO'), ('lgID', 'NY'), ('G', '1'), ('AB', '4'), ('R', '0'), ('H', '0'), ('2B', '0'), ('3B', '0'), ('HR', '0'), ('RBI', '0'), ('SB', '0'), ('CS', '0'), ('BB', '0'), ('SO', '0'), ('IBB', ''), ('HBP', ''), ('SH', ''), ('SF', ''), ('GIDP', '0')])

        print()
        print("insert(): new record")
        print(batting.insert(template_duplicate_pk))

        # Please complete code IN THE SAME FORMAT to test when the rest of methods pass or fail
        # HINT HINT: Don't forget about testing the primary key integrity constraints!!
        # For these tests, think to yourself: When should this fail? When should this pass?

    except Exception as e:
        print("An error occurred:", e)


tests_people()
tests_batting()
