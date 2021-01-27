# read in faculty names
small_name=pd.read_csv("XXXX")

small_name_last=[str(i).strip().split(',')[0] for i in small_name['NAME']] # create another column for last name
small_name_first=[str(i).strip().split(',')[1] for i in small_name['NAME']] # create another column for first name

# created another column for URL encoding first names per Scopus API demand
small_name['FirstNameURL']=[str(i).replace(' ', '%20') for i in small_name['FirstName']]

MY_API_KEY='XXXXXX' # your API key

search=[]
authlast=[]
authfirst=[]
author_id=[]
af_id=[]
af_name=[]
af_city=[]
af_country=[]

for j in range( , ): # 200 is the max result for each request, loop through faculty name dataframe
    url='https://api.elsevier.com/content/search/author?query=authlast({})%20and%20authfirst({})'
    resp = requests.get(url.format(big_name.loc[j]['LastName'], big_name.loc[j]['FirstNameURL']), 
                    headers={'Accept':'application/json',
                            'X-ELS-APIKey': MY_API_KEY})
    result=resp.json()
    try:
        for i in range(0, len(result['search-results']['entry'])):
            if 'dc:identifier' not in result['search-results']['entry'][i]:
                author_id.append('')
                search.append('')
            else:
                author_id.append(result['search-results']['entry'][i]['dc:identifier'].strip('AUTHOR_ID\:'))
                search.append(big_name.loc[j]['LastName']+','+big_name.loc[j]['FirstName'])
            if 'affiliation-current' not in result['search-results']['entry'][i]:
                af_id.append('')
                af_name.append('')
                af_city.append('')
                af_country.append('')
            else:
                if 'affiliation-id' not in result['search-results']['entry'][i]['affiliation-current']:
                    af_id.append('')
                else:
                    af_id.append(result['search-results']['entry'][i]['affiliation-current']['affiliation-id'])
                if 'affiliation-name' not in result['search-results']['entry'][i]['affiliation-current']:
                    af_name.append('')
                else:
                    af_name.append(result['search-results']['entry'][i]['affiliation-current']['affiliation-name'])
                if 'affiliation-city' not in result['search-results']['entry'][i]['affiliation-current']:
                    af_city.append('')
                else:
                    af_city.append(result['search-results']['entry'][i]['affiliation-current']['affiliation-city'])
                if 'affiliation-country' not in result['search-results']['entry'][i]['affiliation-current']:
                    af_country.append('')
                else:
                    af_country.append(result['search-results']['entry'][i]['affiliation-current']['affiliation-country'])
        
    except ValueError:
        author_id.append('')
        af_id.append('')
        af_name.append('')
        af_city.append('')
        af_country.append('')
        
df=pd.DataFrame({
    'search':search,
    'author_id': author_id,
    'af_id': af_id,
    'af_name': af_name,
    'af_city': af_city,
    'af_country': af_country
})

df=df[df.af_id.isin(ur_af_id_list)] # subset only within UR's affiliation-ids

if df is None:
    print("None")
else:
    df.to_csv("XXXXXX", index=False, encoding='utf-8-sig')
    
