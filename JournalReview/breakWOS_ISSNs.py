# add a column combining SN and EI in WOS data

def combineISSN(data):
    data.loc[:, 'ComISSNs'] = data.loc[:, 'SN']+','+data.loc[:, 'EI']
    return data
    
# Then break them down vertically    

def breakISSNs(data):
    
    SO=[] # create empty list for source name
    ISSNs=[] # for ISSNs
    P15=[] # publication for 2015
    P16=[]
    P17=[]
    P18=[]
    P19=[]
    
        # loop through the data frame
    for i in range(0, len(data)):
        
        for j in range(0, len(data.loc[i]['ComISSNs'].split(','))):
            
            issn=[] # create a small list for issns
            issn.append(data.loc[i]['ComISSNs'].split(',')[j])       
            ISSNs.append(issn)
            SO.append(data.loc[i]['SO'])
            P15.append(data.loc[i]['P2015'])
            P16.append(data.loc[i]['P2016'])
            P17.append(data.loc[i]['P2017'])
            P18.append(data.loc[i]['P2018'])
            P19.append(data.loc[i]['P2019'])
    
    df=pd.DataFrame({'Sorce':SO,
                    'ISSNs': ISSNs,
                    'P2015': P15,
                    'P2016': P16,
                    'P2017': P17,
                    'P2018': P18,
                    'P2019': P19})
    
    df['ISSNs']=df['ISSNs'].apply(lambda x: str(x).strip('\]\[\''))
 

    return df
