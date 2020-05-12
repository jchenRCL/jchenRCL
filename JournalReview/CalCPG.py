def CalCPG(data):
    for i in range(0, len(data)): # loop thorugh whole data set
        if (data.loc[i]['Usage on All Platforms'] == np.nan or data.loc[i]['Usage on All Platforms'] == 0) \
        & (data.loc[i]['Total Cost'] != np.nan): 
            # if total usage = na or 0 but total cost is not na
            data.loc[i, 'Cost per Usage'] = data.loc[i]['Total Cost']
        elif (data.loc[i]['Usage on All Platforms'] != np.nan) & (data.loc[i]['Total Cost'] != np.nan):
            data.loc[i, 'Cost per Usage'] = np.round(data.loc[i]['Total Cost']/data.loc[i]['Usage on All Platforms'],2)
        elif (data.loc[i]['Usage on All Platforms'] != np.nan) & (data.loc[i]['Total Cost'] == np.nan):
            data.loc[i, 'Cost per Usage'] = np.nan
        else:
            data.loc[i, 'Cost per Usage'] = np.nan
    return data
