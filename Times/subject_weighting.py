# weighting
def subjectWeight(data):
    weighted = []
    # put the THE subject weighting in a dictionary
    sub_dic = {'32':'0.35', '33':'0.15', '34':'0.35', '35':'0.25', '36':'0.275', '37':'0.35', '38':'0.275', '39':'0.35', \
               '40':'0.25', '41':'0.275', '42':'0.25'}
    for i in range(len(data)):
        if str(data.loc[i, 'THE code']) in sub_dic:
            weighted.append(sub_dic[str(data.loc[i, 'THE code'])])
        else:
            weighted.append('')
    data.loc[:, 'Weighted'] = weighted
# convert the weight column to float
    data['Weighted'] = data['Weighted'].apply(lambda x: float(x))    
# add a new column
    data['Weighted_Cit'] = data['Citation'] * data['Weighted']
    return data
