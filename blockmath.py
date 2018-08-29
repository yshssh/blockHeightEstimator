import pandas as pd
import sys 

blocks = pd.read_csv("blocks.csv")

startDate = 1438214400

def printValues():
    for index, row in blocks.iterrows():
        avgTime = row[2]
        print(avgTime)

#estimate block height at the end of day based on average block time in seconds 
#86400 seconds in a day 
#end block date = starting block height + 86400/average 
# b = 0
# b += 86400/average for whole days 

#1535514683
#block height for a given unix epoch t
#calculate difference between t and startDate
# g = t - startDate
# add 

def estimateBlockHeight(target_timestamp):
    if (target_timestamp < startDate):
        raise ValueError('Timestamp precedes genesis block')
    b = 0.0
    for index, row in blocks.iterrows():
        #if the difference is less than one day
        if (target_timestamp > (row[1] + 86400)):
            b += 86400.00/row[2]
        else:
            delta = 0.0 * (target_timestamp - row[1])
            b  += delta/row[2]
    print(b)


if __name__ == '__main__':
    a = int(sys.argv[1])
    estimateBlockHeight(a)