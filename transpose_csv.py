import os
import csv
path="C:/Users/reese/Documents/personal_projects/option_calculator/"
os.chdir("C:/Users/reese/Documents/personal_projects/option_calculator/")

from csv import reader, writer 
with open('SPY_price_raw.csv') as f, open('SPY_price.csv', 'w') as fw: 
    writer(fw, delimiter=',').writerows(zip(*reader(f, delimiter=',')))