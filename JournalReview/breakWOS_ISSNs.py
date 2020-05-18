# add a column combining SN and EI in WOS data

def combineISSN(data):
    data.loc[:, 'ComISSNs'] = data.loc[:, 'SN']+','+data.loc[:, 'EI']
    return data
    
# Then break them down vertically    

def breakISSNs(data):
        # loop through the data frame
    for i in range(0, len(data)):
        so=[] # create empty list for source name
        ISSNs=[] # for ISSNs
        p15=[] # publication for 2015
        p16=[]
        p17=[]
        p18=[]
        p19=[]
        
        for j in range(0, len(data.loc[i]['ComISSNs'].split(','))):
            issn=[] # create a small list for issns
            issn.append(data.loc[i]['ComISSNs'].split(',')[j])
            ISSNs.append(issn)
            so.append(data.loc[i]['SO'])
            p15.append(data.loc[i]['P2015'])
            p16.append(data.loc[i]['P2016'])
            p17.append(data.loc[i]['P2017'])
            p18.append(data.loc[i]['P2018'])
            p19.append(data.loc[i]['P2019'])
    
    df=pd.DataFrame({'Sorce': so,
                    'ISSNs': ISSNs,
                    'P2015': p15,
                    'P2016': p16,
                    'P2017': p17,
                    'P2018': p18,
                    'P2019': p19})
    
    df['ISSNs']=df['ISSNs'].apply(lambda x: str(x).strip('\]\[\''))
 
    return df
