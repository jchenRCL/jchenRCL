university = []
country = []
code = []
uid = []


url = "https://api.elsevier.com/analytics/scival/institution/search?query=name({})&limit=100&offset=0&apiKey=XXXXXXXXXXXX"

for uni in us_uni['uni_format'][100:]:
    resp = requests.get(url.format(uni), headers={'Accept':'application/json'})
    
    if not 200:
        print("An error has occured. [Status code", resp, "]")
    else:
        try:
            data = resp.json() #Only convert to Json when status is OK.
            if not data["results"]:
                print("Empty JSON")
            else:
                result=data['results']
                for i in result:
                    if i is None:
                        pass
                    else:
                        unis = i['name']
                        countries = i['country'] 
                        codes= i['countryCode']
                        uids = i['id']
                        if unis is not None:
                            university.append(unis)
                        else:
                            university.append("")
                        if countries is not None:
                            country.append(countries)
                        else:
                            country.append("")
                        if codes is not None:
                            code.append(codes)
                        else:
                            code.append("")
                        if uids is not None:
                            uid.append(uids)
                        else:
                            uid.append("")
        except ValueError:
            pass
    
df = pd.DataFrame({'Country Name': country, 'Country Code': code, 'University Id': uid, 'University': university})

df.to_csv("the_2021_us_uni_details_university_3.csv", index=False)
