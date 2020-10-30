university = []
metric_type = []
the_code =[]
value = []
MY_API = "XXXXXXXXXXXXXXX"

url = "https://api.elsevier.com/analytics/scival/institution/metrics?metricTypes=CitationCount&institutionIds={}&yearRange=5yrs&subjectAreaFilterURI=Class%2FTHE%2FCode%2F{}&includeSelfCitations=false&byYear=false&includedDocs=ArticlesReviewsConferencePapersBooksAndBookChapters&journalImpactType=CiteScore&showAsFieldWeighted=true&apiKey={}"
for the_id in [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]:
    for uid in join_result['University Id'][:2]:
#    for uid in join_result['University Id'][:50]:    
        resp = requests.get(url.format(uid, the_id, MY_API), headers={'Accept':'application/json'})
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
                            try:
                                for j in range(len(result)):
                                    university.append(result[j]['institution']['name'])
                                    metric_type.append(result[j]['metrics'][0]['metricType'])
                                    the_code.append(the_id)
                                    value.append(result[j]['metrics'][0]['value'])
                            except ValueError:
                                pass
                                value.append('')

            except (ValueError, KeyError):
                pass
                value.append('')
            
df = pd.DataFrame({'Uni Name': university, 'Metrics': metric_type, 'THE code': the_code, 'Metric Value': value})
df.to_csv("the_file_name.csv", index = False)
