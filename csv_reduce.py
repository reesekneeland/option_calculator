import csv
import os

inputfilepath="/home/reese/personal_projects/option_calculator/CSV_Files/"
calloutputfilepath="/home/reese/personal_projects/option_calculator/formatted_data/calls/"
putoutputfilepath="/home/reese/personal_projects/option_calculator/formatted_data/puts/"
os.chdir(inputfilepath)

spydata = open("/home/reese/personal_projects/option_calculator/SPY_price_2020.csv", 'r')
spyreader = csv.DictReader(spydata)
spy_price = {}
for row in spyreader:
    spydate = row['Date']
    close = row['Close']
    spy_price.update({spydate : close})
    print(spy_price)

for filename in os.listdir(inputfilepath):
    if(len(filename) >=14):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            os.chdir(calloutputfilepath)
            from os import path
            if path.exists('call-' + filename[-14:]):
                callfile = open('call-' + filename[-14:], 'w')
            else:
                callfile = open('call-' + filename[-14:], 'x')
            os.chdir(putoutputfilepath)
            from os import path
            if path.exists('puts-' + filename[-14:]):
                putfile = open('puts-' + filename[-14:], 'w')
            else:
                putfile = open('puts-' + filename[-14:], 'x')
            callfile.write("call ticker, ticker price, date, expiration, strike, type, 15:45 price\n")
            putfile.write("put ticker, ticker price date, expiration, strike, type, 15:45 price\n")
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
                        callfile.write("{}, {}, {}, {}, {} ,{}, {}\n" .format(ticker, tickerprice, date, expiration, strike, otype, p1545))
                    if(otype == 'P'):
                        putfile.write("{}, {}, {}, {}, {} ,{}, {}\n" .format(ticker, tickerprice, date, expiration, strike, otype, p1545))
            csvfile.close()