from data_collection import return_gold

gold_pd = return_gold()


def find_max():
    max = 0
    max2 = 0
    max3 = 0
    index = 0
    for i in range(len(gold_pd)):
        if max < gold_pd.iloc[i][1]:
            index = i
            max = gold_pd.iloc[i][1]
    print(max)
    print(gold_pd.iloc[index])

find_max()