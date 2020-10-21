# Thanks to https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10 for flatten json functions below

from pandas.io.json import json_normalize

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

MY_API = "XXXXXXXXXXX"

# The script below is to retrieve the university's citation counts, excluding self-citation, with THE subject area codes

url = "https://api.elsevier.com/analytics/scival/institution/metrics?metricTypes=CitationCount&institutionIds={}&yearRange=5yrs&subjectAreaFilterURI=Class%2FTHE%2FCode%2F{}&includeSelfCitations=false&byYear=false&includedDocs=ArticlesReviewsConferencePapersBooksAndBookChapters&journalImpactType=CiteScore&showAsFieldWeighted=true&apiKey={}"

for uid in join_result['University Id'][:50]:
    for the_id in the_asjc['THE_subject_id']:
        resp = requests.get(url.format(uid, the_id, MY_API), headers={'Accept':'application/json'})
        if not 200:
            print("An error has occured. [Status code", resp, "]")
        else:
            try:
                data = resp.json() #Only convert to Json when status is OK.
                if not data["results"]:
                    print("Empty JSON")
                else:
                    result = data['results']
                    output = pd.json_normalize(flatten_json(result))
            except (ValueError, KeyError):
                pass
df = pd.DataFrame(output)
df.to_csv("the_file_name.csv", index= False)

                    
