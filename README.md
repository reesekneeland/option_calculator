how to populate the input.csv file:
- ticker: stock ticker, example: SPY, TSLA, etc
- otype: C or P (call or put)
- action: B or W (buy or write)
- expiration: days to expiration date (will be rounded to the nearest date if option at exact expiration is not available), example: 14 will test biweely options
- hold: how many days into the option do you want to sell it, example: 7 to test selling halfway through a biweekly option
- history(NOT YET IMPLEMENTED): how many days back into the history do you want to check the data for example: 365 will check the last year of available data