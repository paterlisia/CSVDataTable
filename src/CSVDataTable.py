from src.BaseDataTable import BaseDataTable
import copy
import logging
import json
import os
import pandas as pd
import csv

pd.set_option("display.width", 256)
pd.set_option('display.max_columns', 20)


class CSVDataTable(BaseDataTable):
    """
    The implementation classes (XXXDataTable) for CSV database, relational, etc. with extend the
    base class and implement the abstract methods.
    """
    _rows_to_print = 10
    _no_of_separators = 2

    def __init__(self, table_name, connect_info, key_columns, debug=True, load=True, rows=None):

        """
        :param table_name: Logical name of the table.
        :param connect_info: Dictionary of parameters necessary to connect to the data.
        :param key_columns: List, in order, of the columns (fields) that comprise the primary key.
        """
        self._data = {
            "table_name": table_name,
            "connect_info": connect_info,
            "key_columns": key_columns,
            "debug": debug
        }

        self._key_columns = key_columns

        self._logger = logging.getLogger()

        self._logger.debug("CSVDataTable.__init__: data = " + json.dumps(self._data, indent=2))

        if rows is not None:
            self._rows = copy.copy(rows)
        else:
            self._rows = []
            self._load()

    def __str__(self):

        result = "CSVDataTable: config data = \n" + json.dumps(self._data, indent=2)

        no_rows = len(self._rows)
        if no_rows <= CSVDataTable._rows_to_print:
            rows_to_print = self._rows[0:no_rows]
        else:
            temp_r = int(CSVDataTable._rows_to_print / 2)
            rows_to_print = self._rows[0:temp_r]
            keys = self._rows[0].keys()

            for i in range(0, CSVDataTable._no_of_separators):
                tmp_row = {}
                for k in keys:
                    tmp_row[k] = "***"
                rows_to_print.append(tmp_row)

            rows_to_print.extend(self._rows[int(-1 * temp_r) - 1:-1])

        df = pd.DataFrame(rows_to_print)
        result += "\nSome Rows: = \n" + str(df)

        return result

    def _add_row(self, r):
        if self._rows is None:
            self._rows = []
        self._rows.append(r)

    def _load(self):

        dir_info = self._data["connect_info"].get("directory")
        file_n = self._data["connect_info"].get("file_name")
        full_name = os.path.join(dir_info, file_n)

        with open(full_name, "r") as txt_file:
            csv_d_rdr = csv.DictReader(txt_file)
            for r in csv_d_rdr:
                self._add_row(r)

        self._logger.debug("CSVDataTable._load: Loaded " + str(len(self._rows)) + " rows")

    def save(self):
        """
        Write the information back to a file.
        :return: None
        """
        fn = self._data["connect_info"].get("directory") + "/" + self._data["connect_info"].get("file_name")
        with open(fn, "w") as csvfile:
            self.columns = self._rows[0].keys()
            csvw = csv.DictWriter(csvfile, self.columns)
            csvw.writeheader()
            for r in self._rows:
                csvw.writerow(r)

    def get_key_column(self):
        pkey = self._data.get("key_columns")
        return pkey

    @staticmethod
    def _project(row, field_list):

        result = {}

        if field_list is None:
            return row

        for f in field_list:
            result[f] = row[f]

        return result

    @staticmethod
    def matches_template(row, template):

        result = True
        if template is not None:
            for k, v in template.items():
                if v != row.get(k, None):
                    result = False
                    break

        return result

    def find_by_primary_key(self, key_fields, field_list=None):
        """
        Finds and returns the records that match the primary key
        :param key_fields: The list with the values for the key_columns, in order, to use to find a record.
        :param field_list: A subset of the fields of the record to return.
        :return: None, or a dictionary containing the requested fields for the record identified
            by the key.
        """
        # transfer to template format(dictionary)
        dictionary = dict(zip(self._key_columns, key_fields))
        # search by template using primary key
        # the primary key is unique so that we do not have to use a list to save our results
        results = self.find_by_template(dictionary)
        return results[0] if len(results) > 0 else None
        # What method can you use?

    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None):
        """
        Finds the record that matches the template.
        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}
        :param field_list: A list of request fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :return: A list containing dictionaries. A dictionary is in the list representing each record
            that matches the template. The dictionary only contains the requested fields.

        """
        result = []

        for r in reversed(self._rows):
            if CSVDataTable.matches_template(r, template):
                new_r = CSVDataTable._project(r, field_list)
                result.append(new_r)

        return result

    def delete_by_key(self, key_fields):
        """
        Deletes the record that matches the key.
        :param key_fields: List of value for the key fields.
        :return: A count of the rows deleted.
        """

        # HINT: Create a dictionary of values/a template for key fields, then call a method you wrote
        # transfer to template format(dictionary)
        dictionary = dict(zip(self._key_columns, key_fields))
        # search by template using primary key and call delete by template
        return self.delete_by_template(dictionary)

    def delete_by_template(self, template):
        """
        Deletes the record that matches the template
        :param template: Template to determine rows to delete.
        :return: Number of rows deleted.
        """
        counter = 0

        # Iterate through rows, if matches, remove the row
        # search by template using primary key
        # the primary key is unique so that we do not have to use a list to save our results
        for r in reversed(self._rows):
            if CSVDataTable.matches_template(r, template):
                counter += 1  # count match rows
                self._rows.remove(r)  # remove the matched row
        self.save()  # save updated CSVDataTable to csv file
        return counter

    def update_by_key(self, key_fields, new_values):
        """

        :param key_fields: List of value for the key fields.
        :param new_values: A dict of field:value to set for updated row.
        :return: Number of rows updated.
        """

        # HINT: Create a dictionary of values/a template for key fields, then call a method you wrote
        # transfer to template format(dictionary)
        dictionary = dict(zip(self._key_columns, key_fields))
        # search by template using primary key and call delete by template
        return self.update_by_template(dictionary, new_values)

    def update_by_template(self, template, new_values):
        """
        :param template: Template for rows to match.
        :param new_values: New values to set for matching fields.
        :return: Number of rows updated.
        """

        counter = 0

        # Iterate through rows, if matches, update the row... what should you check first?
        # search the original data by primary key, if the pk of new value existed, return 0
        for r in reversed(self._rows):
            if CSVDataTable.matches_template(r, template):
                counter += 1  # count match rows
                if 'playerID' in template.keys():
                    # jump if the updated pk will cause duplicate pk
                    serach_result = self.find_by_primary_key(template['playerID'])
                    if serach_result is not None:
                        if r['playerID'] == template['playerID'] and len(serach_result) > 1:
                            continue
                        elif r['playerID'] == template['playerID'] and len(serach_result) > 0:
                            continue
                for key in new_values:
                    r[key] = new_values[key]
                print(r)
        self.save()  # save updated CSVDataTable to csv file

        return counter

    def insert(self, new_record):
        """
        Inserts a new record
        :param new_record: A dictionary representing a row to add to the set of records.
        :return: None
        """

        # HINT: Append a new_record... what should you check first?
        # search the original data by primary key, if the pk of new value existed, return error
        if self.find_by_primary_key(new_record['playerID']):
            self._logger = logging.getLogger()
            self._logger.debug("Error: duplicate playerID, return")
            return
        for r in reversed(self._rows):
            if CSVDataTable.matches_template(r, new_record):
                self._logger = logging.getLogger()
                self._logger.debug("Error: duplicate record, return")
                return
        self._rows.append(new_record)
        self.save()
        return

    def get_rows(self):
        return self._rows
