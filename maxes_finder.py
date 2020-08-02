from data_collection import return_gold

gold_pd = return_gold()


def find_max():
    max = 0
    max2 = 0
    max3 = 0
    index = 0
    index2 = 0
    index3 = 0
    for i in range(len(gold_pd)):
        if max < gold_pd.iloc[i][1]:
            index = i
            max = gold_pd.iloc[i][1]
        elif (max2 < gold_pd.iloc[i][1]) & (max2 != max):
            index2 = i
            max2 = gold_pd.iloc[i][1]
        elif (max3 < gold_pd.iloc[i][1]) & (max3 != max2):
            index3 = i
            max3 = gold_pd.iloc[i][1]
    print(max)
    print(index,index2,index3)
    print(gold_pd.iloc[index])
    print(max2)
    print(gold_pd.iloc[index2]) 
    print(max3)
    print(gold_pd.iloc[index3])
    

find_max()