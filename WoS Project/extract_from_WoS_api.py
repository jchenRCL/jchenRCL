# Step 1
# clean the title: strip '"', replace ' ' with '%20', replace ',' with ''

new = []
for i in range(len(L_data['title'])):
    new.append(L_data['title'][i].replace('"', '').replace(' ', '%20').replace(',', ''))
    
# append the new title to the original dataframe

L_data_2 = L_data.loc[:] # create a copy

L_data_2['URL_title'] = new

# extract data from WoS api

MY_API_KEY = 'XXXXXXXXXXXXXXXXXX'
url = 'https://wos-api.clarivate.com/api/wos/?databaseId=WOS&usrQuery=TS%3D({})&count=100&firstRecord=1'
res = []

for i in range(0, len(L_data_2['URL_title'])):  
    resp = requests.get(url.format(L_data_2['URL_title'][i]),
                    headers={'Accept':'application/json',
                             'X-ApiKey': MY_API_KEY})
    result=resp.json() 
    try:
        if 200:
            if result['QueryResult']['RecordsFound'] != 0:
                res.append('True')
            else:
                res.append('False')
    except KeyError:
        res.append('Error')
        
L_data_2['Found in WoS'] = res

# check the percentage of true/false/error in the result set

# percentage of true
count = 0
for word in res:
    if word == 'True':
        count += 1
print(round(count/len(res), 2))


# Optional: might check again those error titles by create another dataframe called error_table

error_title = L_data_2[L_data_2['Found in WoS'].apply(lambda x: x == 'Error')]['title'] 

url = 'https://wos-api.clarivate.com/api/wos/?databaseId=WOS&usrQuery=TS%3D({})&count=100&firstRecord=1'

MY_API_KEY = 'XXXXXXXXXXXXXXXX'
#url = 'https://wos-api.clarivate.com/api/wos/?databaseId=WOS&usrQuery=TS%3D({})&count=100&firstRecord=1'
res = []
for i in range(0, len(error_table['URL_title'])):  
    resp = requests.get(url.format(error_table['URL_title'][i]),
                    headers={'Accept':'application/json',
                             'X-ApiKey': MY_API_KEY})
    result=resp.json() 
    try:
        if 200:
            if result['QueryResult']['RecordsFound'] != 0:
                res.append('True')
            else:
                res.append('False')
    except KeyError:
        res.append('Error')

# Use linear search to find if some of the error title can find result, and then put back to the original dataframe

for i in range(len(L_data_2)):
    for j in range(len(review_res)):
        if L_data_2['title'][i] == review_res['title'][j]:
            L_data_2['Found in WoS'][i] = review_res['Found in WoS'][j]
            
            

