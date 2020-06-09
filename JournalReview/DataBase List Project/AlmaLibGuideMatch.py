# import library

from fuzzywuzzy import fuzz

def get_ratio_lib2(data1, data2):

    alma = [] # create list for Alma title
    lib = [] # create list for Summon title 
    ratio = []
    try:
        for i in range(0, len(data1)):
            for j in range(0, len(data2)):
                alma.append(data1.loc[i]['Title3']) # append Alma titles, here Title3 is Alma's and Name1 is LibGuides'
                if fuzz.token_set_ratio(data1.loc[i]['Title3'], data2.loc[j]['Name1']) > 70 : # here we use 70 as a threshold value
                    lib.append(data2.loc[j]['Name1'])
                    ratio.append(fuzz.token_set_ratio(data1.loc[i]['Title3'], data2.loc[j]['Name1']))
                else:
                    lib.append('Ratio Less than 70')
                    ratio.append('Ratio Less than 70')
                    
        df = pd.DataFrame({'Alma': alma,
                        'LibGuides': lib,
                        'Ratio': ratio})
    except KeyError:
        pass
                

    return df
