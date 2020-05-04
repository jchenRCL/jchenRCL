# match parent data's column C (abbreviated title) with citation data's CR column
def MatchCitation(data, parent):
    # add a JCR Abbreviated Title column to data
    data['JCR Abbreviated Title']=data['CR']
    
    # left join
    result=parent.join(data.set_index('JCR Abbreviated Title'), on='JCR Abbreviated Title')
    
    return result # this is the matched file, export


