# The pharmacy counting challenge

## Run
Codes is involved in folder src. Code is written in Python3 langauge. No external library is imported, only sys and re library are imported. This code may take about 2 mins to process all entries in de_cc_data.txt.

## Testing
This code is fully tested with itcont.txt file and de_cc_data.txt. Check process is passed in run_tests.sh!

## Steps of solution
1. Read dataset from input folder line by line.
2. Split the records from each line and check the line is splited correctly.
3. Create two dictionaries to record the drug_cost_sum and prescriber_name list with drug_name as key respectively.
4. Check if drug_name is in the dictionary key list, if not create one and assign initial values, otherwise update the related values.
5. Sort the dictionary by drug_cost and drug_name in decreasing order and count unique number of each prescriber_name list.
6. Because the decimal digits of value in de_cc_data.txt are limited to 2 digits. I rounded my results to 2 decimal digits with tail zeros removed.
7. Write results to output folder.   
