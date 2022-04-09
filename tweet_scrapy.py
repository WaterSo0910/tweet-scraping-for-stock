
import nest_asyncio
import twint
from datetime import date, timedelta
import pandas as pd
import os
from args_template import parse_args
import time
# Instantiate and configure the twint-object


def getDates():
    startDate = date(year, month, 1)
    endDate = date(year if month!=12 else year+1, month+1 if month!=12 else 1 , 1)
    # endDate = date(year, month+1, 1)
    Dates = pd.date_range(startDate-timedelta(days=1),endDate-timedelta(days=1),freq='d').strftime('%Y-%m-%d')
    return Dates

def setDir():
    dirname = os.getcwd()
    filename = os.path.join(dirname+'\\data', target)
    
    if not os.path.exists(filename):
        os.mkdir(filename)
        
    filename = os.path.join(filename, year_month)
    if not os.path.exists(filename):
        os.mkdir(filename)

def scrapy():
    c = twint.Config()
    nest_asyncio.apply()
    c.Hide_output = True
    for i, _ in enumerate(Dates):
        if i+1 == len(Dates):
            continue
        c.Store_csv =True
        c.Since = Dates[i]
        c.Until = Dates[i+1]
        c.Search = target
        c.Popular_tweets = True
        # c.Limit = max_nums
        c.Output = f"./data/{target}/{year_month}/Tweets_{c.Search}_{c.Until}_max={c.Limit}.csv"
        c.Lang = 'en'
        twint.run.Search(c)
        f = f"./data/{target}/{year_month}/Tweets_{c.Search}_{Dates[i+1]}_max={c.Limit}.csv"
        if not os.path.exists(f):
            print(f"[No data]: {target} | {Dates[i+1]}")
            print()
        else:   
            df = pd.read_csv(f)
            print(Dates[i+1], df.shape)

def main():
    global target, year, month, max_nums, year_month, Dates
    args = parse_args()
    target = args.search
    year = args.year
    month = args.month
    max_nums = args.max_nums
    
    Dates = getDates()
    year_month = Dates[-1][:7]
    setDir()
    scrapy()
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Elapsed time: ', str(timedelta(seconds=time.time() - start_time)))