# create column names for output
title=[]
issn=[]
formats=[]
serialTypes=[]

SEARCHAPI_KEY="XXXXXX" 

url='http://ulrichsweb.serialssolutions.com/api/{}/search?version=1.2&operation=searchRetrieve&query={}&maximumRecords=10'

# more details about available url can check: https://knowledge.exlibrisgroup.com/Ulrich's/Product_Documentation/Configuring/Ulrichsweb_API/Ulrichsweb%3A_Using_the_Ulrichsweb_API
# and http://ulrichsweb.serialssolutions.com/api-ui.html

for i in range(0, 100): # the website shows each query has max 50 data records, but here I use loop seem get around that
    resp = requests.get(url.format(SEARCHAPI_KEY, wos_pub.loc[i]['SO']), # input journal titles
                    headers={'Accept':'application/json'})
    result=resp.json()
    try:
        for j in range(0, len(result['results']['UlrichTitle'])):
            title.append(result['results']['UlrichTitle'][j]['title'])
            issn.append(result['results']['UlrichTitle'][j]['issn'])
            formats.append(result['results']['UlrichTitle'][j]['formats'])
            serialTypes.append(result['results']['UlrichTitle'][j]['serialTypes'])
    except ValueError:
        title.append('')
        issn.append('')
        formats.append('')
        serialTypes.append('')
df=pd.DataFrame({
    'title': title,
    'issn': issn,
    'formats': formats,
    'serialTypes': serialTypes
})


df.to_excel("wos_pub_Ulrich_ISSNs_1.xlsx", index=False, engine='xlsxwriter')
