def sort_nona_sj(data):
    
    # first exclude nan data records and save them
    nan=data[data['Cost Per Use on All Platforms (USD)'].apply(lambda x: x=='nan')]
    nan.reset_index(inplace=True, drop=True)
    
    # create another data frame which has no na data records
    data_nona = data[data['Cost Per Use on All Platforms (USD)'].apply(lambda x: x!='nan')]
    data_nona.reset_index(inplace=True, drop=True)
    
    # first replace $ so we can convert cpg data types to float for sorting
    data_nona.loc[:, 'Cost Per Use on All Platforms (USD)']=\
    data_nona['Cost Per Use on All Platforms (USD)'].apply(lambda x: float(x.replace('$','')))
    # next we can sort the cpg
    data_nona.sort_values(by='Cost Per Use on All Platforms (USD)', ascending=False, inplace=True)
    # reset index
    data_nona.reset_index(inplace=True, drop=True)
    
    # concatenate
    data_new = pd.concat([nan, data_nona])
    data_new.reset_index(inplace=True, drop=True)
    
    data_new['Cost Per Use on All Platforms (USD)']=np.round(data_new['Cost Per Use on All Platforms (USD)'],2)
    
    # convert datatypes to string and add $
    data_new['Cost Per Use on All Platforms (USD)'] = \
    data_new['Cost Per Use on All Platforms (USD)'].apply(lambda x: str(x))
    data_new['Cost Per Use on All Platforms (USD)'] = \
    data_new['Cost Per Use on All Platforms (USD)'].apply(lambda x: '$ '+x if x !='nan' else x)
    
    return data_new
