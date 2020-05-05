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
    
    data_gped['Cost Per Use on All Platforms (USD)'] = \
    np.round(data_gped['Total Cost']/data_gped['Usage on All Platforms'], 2)
    
    return data_gped
