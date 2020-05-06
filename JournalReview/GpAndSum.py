def GpAndSum(data):
    
    # if no Fund Code replace the value with 'TBD'
    data['Fund Code']=data['Fund Code'].apply(lambda x: x=='TBD' if x == '' else x)
    data_c = pd.DataFrame() # grouped cost
    data_u = pd.DataFrame() # grouped usage
    data_f = pd.DataFrame() # grouped fund
    data_c = data.groupby(data['Publisher Package'].str.lower())[['Total Cost']].sum()
    data_u = data.groupby(data['Publisher Package'].str.lower())[['Usage on All Platforms']].sum()
    data_f = data.groupby(data['Publisher Package'].str.lower()).apply(lambda x: ','.join((x['Fund Code']).unique()))
    data_f=data_f.to_frame().reset_index()
    data_f.columns=['Publisher Package', 'Fund Code']
    
    # combine them together
    # first reset index
    data_c.reset_index(inplace = True)
    data_u.reset_index(inplace = True)
    
    # concatenation, axis =1 means column concatenation
    data_gped = pd.concat([data_u, data_c, data_f], axis=1)
    
    # drop duplicated columns
    data_gped=data_gped.loc[:,~data_gped.columns.duplicated()]
    
    # calculate Cost Per Use
    # if usage is 0, then fill Total Cost
    # if usage is NA, then fill NA
    # else divide total cost by total usage and round to the second precision
    
    for i in range(0, len(data_gped)):
        if data_gped.loc[i]['Usage on All Platforms']==0: # usage is 0
            data_gped.loc[i, 'Cost Per Use on All Platforms (USD)']= \
                data_gped.loc[i]['Total Cost']
        elif data_gped.loc[i]['Usage on All Platforms']=='': # usage is np.nan
            data_gped.loc[i, 'Usage on All Platforms']==np.nan
            data_gped.loc[i, 'Cost Per Use on All Platforms (USD)']= np.nan
        else:
            data_gped.loc[i, 'Cost Per Use on All Platforms (USD)'] = \
                np.round(data_gped.loc[i]['Total Cost']/data_gped.loc[i]['Usage on All Platforms'], 2)
    
    ## change package names as upper
    
    data_gped['Publisher Package']=data_gped['Publisher Package'].apply(lambda x: x.upper())
    
    ## round Total Cost to 2nd precision
    
    data_gped['Total Cost']=data_gped['Total Cost'].apply(lambda x: np.round(x, 2))
    
    ## change data types to string
    
    data_gped['Total Cost']=data_gped['Total Cost'].apply(lambda x: str(x)) 
    data_gped['Cost Per Use on All Platforms (USD)']=\
    data_gped['Cost Per Use on All Platforms (USD)'].apply(lambda x: str(x)) 
    data_gped['Usage on All Platforms']=\
    data_gped['Usage on All Platforms'].apply(lambda x: str(x)) 
    
    ## if Total Cost and Cost Per Use on All Platforms (USD) not np.nan, add $
    
    s=[]
    for i in data_gped['Cost Per Use on All Platforms (USD)']:
        if i != "nan":
            s.append('$ '+ str(i))
        else:
            s.append(i)
            
    data_gped.loc[:, 'Cost Per Use on All Platforms (USD)']=s
    
    data_gped['Total Cost']=\
    data_gped['Total Cost'].apply(lambda x: '$ '+str(x) if x != np.nan else x)
    
    return data_gped
