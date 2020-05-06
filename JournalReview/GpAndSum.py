def GpAndSum(data):
    # fillna(0) for Usage
    data['Usage on All Platforms']=data['Usage on All Platforms'].fillna(0)
    data_c = pd.DataFrame() # grouped cost
    data_u = pd.DataFrame() # grouped usage
    data_c = data.groupby(data['Publisher Package'].str.lower())[['Total Cost']].sum()
    data_u = data.groupby(data['Publisher Package'].str.lower())[['Usage on All Platforms']].sum()
    
    # combine them together
    # first reset index
    data_c.reset_index(inplace = True)
    data_u.reset_index(inplace = True)
    
    # concatenation, axis =1 means column concatenation
    data_gped = pd.concat([data_u, data_c], axis=1)
    
    # droup duplicated columns
    data_gped = data_gped.iloc[:, 1:]
    data_gped.set_index('Publisher Package', inplace=True)
    data_gped.reset_index(inplace=True)
    
    # calculate Cost Per Use
    
    # calculate Cost Per Use
    # if usage is 0, then fill Total Cost
    # if usage is NA, then fill NA
    # else divide total cost by total usage and round to the second precision
    
    for i in range(0, len(data_gped)):
        if data_gped.loc[i]['Usage on All Platforms']==0: # usage is 0
            data_gped.loc[i, 'Cost Per Use on All Platforms (USD)']= \
                data_gped.loc[i]['Total Cost']
        elif data_gped.loc[i]['Usage on All Platforms'] == "NA": # usage is np.nan
            data_gped.loc[i, 'Cost Per Use on All Platforms (USD)']= "NA"
        else:
            data_gped.loc[i, 'Cost Per Use on All Platforms (USD)'] = \
                np.round(data_gped.loc[i]['Total Cost']/data_gped.loc[i]['Usage on All Platforms'], 2)
            
            
        ## change package names as upper
    
    data_gped['Publisher Package']=data_gped['Publisher Package'].apply(lambda x: x.upper())
    
    ## if Total Cost and Cost Per Use on All Platforms (USD) not np.nan, add $
    
    data_gped['Cost Per Use on All Platforms (USD)']= ['$'+str(x) for x in data_gped['Cost Per Use on All Platforms (USD)']\
                                                      if x != np.nan]
    
    data_gped['Total Cost']= ['$'+str(x) for x in data_gped['Total Cost']\
                                                      if x != np.nan]
    
    return data_gped
