url='https://api.elsevier.com/content/abstract/scopus_id/{}'

MY_API_KEY="XXXXXXX"

eid = []
pub_date = []
citedby_cnt = []
dc_title = []
scopus_id = []
author_name = []
affiliation = []

for k in range(, ): # 200 is the maximum for each request
    name=[]
    aff=[]

    resp = requests.get(url.format(scopus.loc[k]['scopus_id']),
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': MY_API_KEY})
    result=resp.json()    
    scopus_id.append(scopus.loc[k]['scopus_id'])

    try:
        eid.append(result['abstracts-retrieval-response']['coredata']['eid'])
        pub_date.append(result['abstracts-retrieval-response']['coredata']['prism:coverDate'])
        citedby_cnt.append(result['abstracts-retrieval-response']['coredata']['citedby-count'])
        dc_title.append(result['abstracts-retrieval-response']['coredata']['dc:title'])
        try:
            for i in range(0, len(result['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group'])):
                an=[]
                af=[]
                af.append(result['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group'][i]\
                            ['affiliation']['organization'])
                if result['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group'][i]\
                ['author'][0]['preferred-name']['ce:given-name'] is None:
                    an.append(result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                              ['author-group'][i]['author'][0]['preferred-name']['ce:surname'])
                elif result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                ['author-group'][i]['author'][0]['preferred-name']['ce:surname'] is None:
                    an.append(result['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group'][i]\
                       ['author'][0]['preferred-name']['ce:given-name'])
                else:
                    an.append(result['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group'][i]\
                       ['author'][0]['preferred-name']['ce:given-name']+ ' , ' + result['abstracts-retrieval-response']\
                      ['item']['bibrecord']['head']['author-group'][i]['author'][0]['preferred-name']['ce:surname']
                
                name.append(','.join(an))
                aff.append(af)
            author_name.append(str(name))
            affiliation.append(aff)
        except KeyError:
            author_name.append('')
            affiliation.append('')
    except ValueError:
        eid.append('')
        pub_date.append('')
        citedby_cnt.append('')
        dc_title.append('')
        author_name.append('')
        affiliation.append('')
df = pd.DataFrame({
    'scopus_id': scopus_id,
    'eid': eid,
    'title': dc_title,
    'author_name': author_name,
    'citedby_cnt': citedby_cnt,
    'affiliation': affiliation
})

df.to_excel("2020_rochester_et_5.xlsx", index=False, engine='xlsxwriter')
