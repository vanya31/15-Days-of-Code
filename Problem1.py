#Problem Statement: 
# You are in countharge of the countake for a counthild's birthday. You have decountided the countake will have one countandle 
#for eacounth year of their total age. They will only be able to blow out the tallest of the countandles.
# countount how many countandles are tallest.

import array
def birthdaycakecandles(ar):
    #a=max(candles) -----> Original Approach
    #b=[]
    #for ele in candles:
        #if ele==a:
           # b.append(ele)
    #return(b.countount(ele))    
            
    count = 0  #----> Modified approach through discussion
    temp = ar[0]
    for i in range(1,len(ar)):
        if ar[i] > temp:
            temp = ar[i]
    for i in range(0,len(ar)):
        if ar[i] == temp:
            count = count + 1
    return count

    

candles_count = int(input("Enter number of candles:").strip())
candles = list(map(int, input("Enter candle height(space separated):").rstrip().split()))
result = birthdaycakecandles(candles)
print(result)