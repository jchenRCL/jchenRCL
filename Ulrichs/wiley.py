url = 'http://ulrichsweb.serialssolutions.com/api/{}/search?filterQuery=country%3AUSA&query=publisher%3Awiley \
&start=1150&rows=50' # start = starting index, max for rows is 50

SEARCHAPI_KEY='XXXXXXXX'
title = []
publisher = []
year = []
desp = []
subject = []

resp = requests.get(url.format(SEARCHAPI_KEY),
                    headers={'Accept':'application/json'})
result=resp.json()

if not 200:
    print("An error has occured. [Status code", resp, "]")
else:
    try:
        data = resp.json() #Only convert to Json when status is OK.
        if not data["results"]:
            print("Empty JSON")
        else:
            output = data['results']['UlrichTitle']
            for i in range(len(output)):
                title.append(str(output[i]['title']).strip('\]\['))
                publisher.append(str(output[i]['publisher']).strip('\]\['))
                year.append(str(output[i]['startYear']).strip('\]\['))
                desp.append(str(output[i]['description']).strip('\]\['))
                subject.append(str(output[i]['subject']).strip('\]\['))

    except (ValueError, KeyError):
        pass
    
    
df = pd.DataFrame({'title': title, 'publisher': publisher,'startYear': year, 'description': desp, 'subject': subject})

df.to_csv("film_name.csv", index = False)
