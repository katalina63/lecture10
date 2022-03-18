import csv 
import pandas as pd
 
 
def xlsx_to_csv_pd():
    data_xls = pd.read_excel('/Users/ekaterina/home_work_data/test_table.xlsx')
    data_xls.to_csv('/Users/ekaterina/home_work_data/test_table.csv')
 
 
if __name__ == '__main__':
    xlsx_to_csv_pd()
