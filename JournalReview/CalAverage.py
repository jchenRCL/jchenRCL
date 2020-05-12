def CalAverage(data):
    data.loc[:,'PAVG5Y']=np.round(data['P2015-19']/5,2)
    data.loc[:,'CRAVG5Y']=np.round(data['CR2015-19']/5,2)
    return data
    
    
