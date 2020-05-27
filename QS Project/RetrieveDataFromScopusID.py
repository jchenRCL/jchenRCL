url='https://api.elsevier.com/content/abstract/scopus_id/{}'

MY_API_KEY="XXXXXXXXXXX"

af=[]
au1=[]
cit_title=[]
scopus_id=[]
eid = []
pub_date = []
citedby_cnt = []


for k in range( , ): # 200 maximum for reach request
    
    resp = requests.get(url.format(scopus.loc[k]['scopus_id']),
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': MY_API_KEY})
    result=resp.json()    
    scopus_id.append(scopus.loc[k]['scopus_id'])
    
    if 'abstracts-retrieval-response' in result:
        l=[]
        q=[]
        eid.append(result['abstracts-retrieval-response']['coredata']['eid'])
        pub_date.append(result['abstracts-retrieval-response']['coredata']['prism:coverDate'])
        citedby_cnt.append(result['abstracts-retrieval-response']['coredata']['citedby-count'])
        if 'item' in result['abstracts-retrieval-response']:
            if 'bibrecord' in result['abstracts-retrieval-response']['item']:
                if 'head' in result['abstracts-retrieval-response']['item']['bibrecord']:
                    if 'citation-title' in result['abstracts-retrieval-response']['item']['bibrecord']['head']:
                        cit_title.append(result['abstracts-retrieval-response']['item']['bibrecord']['head']['citation-title'])
                    if 'author-group' in result['abstracts-retrieval-response']['item']['bibrecord']['head']:
                        if len(result['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group'])<1:
                            pass
                        else:
                            for i in range(0, len(result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                                              ['author-group'])):
                                try:
                                    if 'affiliation' not in result['abstracts-retrieval-response']['item']\
                                                            ['bibrecord']['head']['author-group'][i]:
                                        l.append('')
                                    else:
                                        if 'organization' not in result['abstracts-retrieval-response']['item']\
                                                                ['bibrecord']['head']['author-group'][i]['affiliation']:
                                            l.append('')
                                        else:
                                            if len(result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                                                    ['author-group'][i]['affiliation']['organization'])<1:
                                                pass
                                            else:
                                                if len(result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                                                        ['author-group'][i]['affiliation']\
                                                        ['organization'])==1:
                                                    l.append(str(result['abstracts-retrieval-response']['item']['bibrecord']\
                                                                ['head']['author-group'][i]['affiliation']\
                                                                ['organization']['$']).strip())
                                                else:
                                                    for j in range(0, len(result['abstracts-retrieval-response']\
                                                                    ['item']['bibrecord']['head']\
                                                                    ['author-group'][i]['affiliation']\
                                                                    ['organization'])):
                                                        for w in range(1, j+1):
                                                            s=[]
                                                            s.append((str(result['abstracts-retrieval-response']\
                                                                        ['item']['bibrecord']['head']\
                                                                        ['author-group'][i]['affiliation']\
                                                                        ['organization'][w]['$']).strip())\
                                                                        +' '+(str(result['abstracts-retrieval-response']\
                                                                        ['item']['bibrecord']['head']\
                                                                        ['author-group'][i]['affiliation']\
                                                                        ['organization'][j]['$']).strip()))
                                                            for k in range(0, len(s)):
                                                                l.append(s[k])                                                           
                                    if 'author' not in result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                                                        ['author-group'][i]:
                                        q.append('')
                                    else:
                                        if len(result['abstracts-retrieval-response']['item']['bibrecord']['head']\
                                                ['author-group'][i]['author']) <1:
                                            pass
                                        else:
                                            for v in range(0, len(result['abstracts-retrieval-response']['item']['bibrecord']\
                                                                  ['head']['author-group'][i]['author'])):
                                                if 'preferred-name' not in result['abstracts-retrieval-response']\
                                                                            ['item']['bibrecord']\
                                                                            ['head']['author-group'][i]['author'][v]:
                                                    pass
                                                else:
                                                    if 'ce:indexed-name' not in result['abstracts-retrieval-response']['item']\
                                                        ['bibrecord']['head']['author-group'][i]['author']\
                                                        [v]['preferred-name']:
                                                        pass
                                                    else:
                                                        r=[]
                                                        r.append(result['abstracts-retrieval-response']['item']['bibrecord']\
                                                                    ['head']['author-group'][i]['author'][v]['preferred-name']\
                                                                    ['ce:indexed-name'])   
                                                        for t in range(0,len(r)):
                                                            q.append(r[t])                                
                                except KeyError:
                                                if 'affiliation' not in result['abstracts-retrieval-response']['item']\
                                                                        ['bibrecord']['head']['author-group']:
                                                    l.append('')
                                                else:
                                                    if 'organization' not in result['abstracts-retrieval-response']\
                                                                             ['item']['bibrecord']['head']\
                                                                             ['author-group']['affiliation']:
                                                        l.append('')
                                                    else:
                                                        if len(result['abstracts-retrieval-response']['item']\
                                                               ['bibrecord']['head']['author-group']\
                                                               ['affiliation']['organization'])==1:
                                                            l.append(result['abstracts-retrieval-response']['item']\
                                                                     ['bibrecord']['head']['author-group']\
                                                                     ['affiliation']['organization']['$'])
                                                        else:
                                                            for c in range(0, len(result['abstracts-retrieval-response']['item']\
                                                                                  ['bibrecord']['head']['author-group']\
                                                                                  ['affiliation']['organization'])):
                                                                l.append(result['abstracts-retrieval-response']['item']['bibrecord']\
                                                                         ['head']['author-group']['affiliation']['organization']\
                                                                         [c]['$'] + ' '+result['abstracts-retrieval-response']['item']\
                                                                         ['bibrecord']['head']['author-group']['affiliation']\
                                                                         ['organization'] [c]['$'])
                                                                c+=1
                                                if 'author' not in result['abstracts-retrieval-response']['item']\
                                                                   ['bibrecord']['head']['author-group']:
                                                    q.append('')
                                                else:
                                                    for v in range(0, len(result['abstracts-retrieval-response']['item']\
                                                                          ['bibrecord']['head']['author-group']\
                                                                          ['author'])):
                                                        if 'preferred-name' in result['abstracts-retrieval-response']\
                                                                               ['item']['bibrecord']['head']\
                                                                               ['author-group']['author'][v]:
                                                            if 'ce:indexed-name' in result['abstracts-retrieval-response']\
                                                                                    ['item']['bibrecord']['head']\
                                                                                    ['author-group']\
                                                                                    ['author'][v]['preferred-name']:
                                                                n=[]
                                                                n.append(result['abstracts-retrieval-response']['item']\
                                                                         ['bibrecord']['head']['author-group']\
                                                                         ['author'][v]['preferred-name']\
                                                                         ['ce:indexed-name'])
                                                                for h in range(0, len(n)):
                                                                    q.append(n[h])
                                                    
    au1.append(str(q).strip('\] \['))
    af.append(str(l).strip('\] \['))


df=pd.DataFrame({'Title': cit_title,
                'Author': au1,
                'Affiliation': af,
                'Scopus_id': scopus_id,
                'eid':eid,
                'pub_date': pub_date,
                'citedby_cnt': citedby_cnt})

df.to_excel("2020_rochester_et_new_1.xlsx", index=False, engine='xlsxwriter')
