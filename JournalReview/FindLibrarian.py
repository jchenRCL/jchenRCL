def FindLib(data, fund_code_dict):
    lib=[]  #create a list 
    for i in range(0, len(data)):
        for j in range(0,58): # fund_code_hash table
            if data.loc[i]['FundCode']== fund_code_dict['Fund Code'][j].strip():
                lib.append(fund_code_dict['Librarian'][j])
    data.loc[:, 'Librarian'] = lib
    
    # group by packageName and then append FundCode and Librarian separately,
    # and then concat two together
    
    res1=data.groupby('packageName')['FundCode'].apply(lambda x: ','.join(x)).to_frame()
    res1.reset_index(inplace=True)
    
    res2=data.groupby('packageName')['Librarian'].apply(lambda x: ','.join(x)).to_frame()
    res2.reset_index(inplace=True)
    
    res = pd.concat([res1, res2], axis=1)
    
    # droup duplicated columns
    res_nodup=res.loc[:,~res.columns.duplicated()]
    
    return res_nodup
