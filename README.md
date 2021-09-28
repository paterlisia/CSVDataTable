# CSVDataTable
## i. Coding


You are responsible for implementing and testing two classes in Python: CSVDataTable, BaseDataTable.
The python files and data can be found in the assignment under Courseworks. 

We have already given you **find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None)**
Use this as a jumping off point for the rest of your functions.

Methods to complete:

CSVDataTable.py
- [x] find_by_primary_key(self, key_fields, field_list=None)
- [x] delete_by_key(self, key_fields)
- [x] delete_by_template(self, template)
- [x] update_by_key(self, key_fields, new_values)
- [x] update_by_template(self, template, new_values)
- [ ] insert(self, new_record)
CSV_table_tests.py
- [ ] You must test all methods. You will have to write these tests yourself. 
- [ ] You must test your methods on the People and Batting table.

If you do not include tests and tests outputs 50% of this section's points will be deducted at the start

## ii. Testing

Please copy the text from the output of your tests and paste it below: