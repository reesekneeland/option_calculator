import csv
import os

inputfilepath="C:/Users/reese/Documents/personal_projects/option_calculator/CSV_Files/"
calloutputfilepath="C:/Users/reese/Documents/personal_projects/option_calculator/formatted_data/calls/"
putoutputfilepath="C:/Users/reese/Documents/personal_projects/option_calculator/formatted_data/puts/"
os.chdir(inputfilepath)

spydata = open("C:/Users/reese/Documents/personal_projects/option_calculator/SPY_price_2020.csv", 'r')
spyreader = csv.DictReader(spydata)
spy_price = {}
for row in spyreader:
    spydate = row['Date']
    close = row['Close']
    spy_price.update({spydate : close})
    print(spy_price)

for filename in os.listdir(inputfilepath):
    if(len(filename) <=14):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            os.chdir(calloutputfilepath)
            from os import path
            if path.exists('call-' + filename):
                callfile = open('call-' + filename, 'w')
            else:
                callfile = open('call-' + filename, 'x')
            os.chdir(putoutputfilepath)
            from os import path
            if path.exists('puts-' + filename):
                putfile = open('puts-' + filename, 'w')
            else:
                putfile = open('puts-' + filename, 'x')
            callfile.write("ticker,ticker_price,expiration,strike,15:45_price\n")
            putfile.write("ticker,ticker_price,expiration,strike,15:45_price\n")
            os.chdir(inputfilepath)
            for row in reader:
                ticker = row['root']
                date = row['quote_date']
                expiration = row['expiration']
                strike = round(float(row['strike']))
                otype = row['option_type']
                p1545 = round(((float(row['bid_1545']) + float(row['ask_1545']))/2.0), 2)
                volume = row['trade_volume']
                tickerprice = round(float(spy_price.get(date)))
                print(volume)
                if (int(volume) > 0):
                    if(otype == 'C'):
                        callfile.write("{},{},{},{},{}\n" .format(ticker, tickerprice, expiration, strike, p1545))
                    if(otype == 'P'):
                        putfile.write("{},{},{},{},{}\n" .format(ticker, tickerprice, expiration, strike, p1545))
            csvfile.close()