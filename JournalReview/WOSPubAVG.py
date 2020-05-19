# first subset the 'P2015' - 'P2019' not null data points and then calculate the sum and the average

def CalAvgPub(data):
    
    for i in range(0, len(data)):
        
        if (data.loc[i]['P2015'] != np.nan) | (data.loc[i]['P2016'] != np.nan) | (data.loc[i]['P2017'] != np.nan) | \
        (data.loc[i]['P2018'] != np.nan) | (data.loc[i]['P2019'] != np.nan):
            data.loc[i,'P2015-19'] = data.loc[i]['P2015'] + data.loc[i]['P2016'] + data.loc[i]['P2017'] + \
            data.loc[i]['P2018']+data.loc[i]['P2019']
            
            #calculate mean
            
            data.loc[i, 'PAVG5Y'] = data.loc[i,'P2015-19']/5
            
    return data
