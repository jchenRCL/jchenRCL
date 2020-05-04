def MatchParent_new(data, parent):
    wos_sn=pd.DataFrame() # wos_pub with sn.notnull()
    wos_ei=pd.DataFrame() # wos_pub with ei.notnull()
    wos_sn = data[data['SN'].notnull()] # subset
    wos_ei = data[data['EI'].notnull()] # subset
    wos_sn.reset_index(inplace=True, drop=True)
    wos_ei.reset_index(inplace=True, drop=True)
    
    # first match with sn
    # add a "ISSN" column in wos_sn
    
    wos_sn['ISSN']=wos_sn.loc[:]['SN']
    match_sn = parent.join(wos_sn.set_index('ISSN'), on='ISSN', lsuffix='_parent', rsuffix='_sn')
    match_sn.reset_index(inplace=True, drop=True)
    
    # secondly match with ei
    # add a "ISSN" column in wos_ei
    
    wos_ei['ISSN']=wos_ei.loc[:]['EI']
    match_ei = parent.join(wos_ei.set_index('ISSN'), on='ISSN', lsuffix='_parent', rsuffix='_ei')
    match_ei.reset_index(inplace=True, drop=True)
    
    # extract the ones with publication counts
    
    pub_col=['P2015','P2016','P2017','P2018','P2019','P2015-19'] # the columns with publication
    
    ei_jr_title=match_ei[match_ei['P2015-19'].notnull()]['Full Journal Title']
    
    sn_jr_title=match_sn[match_sn['P2015-19'].notnull()]['Full Journal Title']
    
    # extract ei_jr_title_test as the ei journal titles not in sn's journal titles
    
    ei_jr_title_test=ei_jr_title[~ei_jr_title.isin(list(sn_jr_title))]
    
    ei_index=match_ei[match_ei['Full Journal Title'].isin(list(ei_jr_title_test))].index
    
    match_sn.loc[ei_index, pub_col]=match_ei.loc[ei_index, pub_col]
    
    return match_sn # this is the matched file, export
