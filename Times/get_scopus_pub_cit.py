MY_API = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

query = "AFFIL(University%20of%20Rochester) and (DOCTYPE(ar) OR DOCTYPE(bk) OR DOCTYPE(ch) OR DOCTYPE(cp) OR DOCTYPE(re)) and \
(PUBYEAR > 2014 and PUBYEAR < 2016)"

# The cursor value for the next ref

nt = 'AoNRuu9MCEDexLEyMi1zMi4wLTg0OTM5NDIzNzA2'

url = f"https://api.elsevier.com/content/search/scopus?query={query}&cursor={nt}&count=100"

prism_url=[]
#dc_identifier=[]
eid=[]
dc_title=[]
dc_creator=[]
prism_publicationNam=[]
prism_issn=[]
prism_eIssn=[]
prism_volume=[]
prism_issueIdentifier=[]
#prism_pageRange=[]
prism_coverDate=[]
prism_coverDisplayDate=[]
prism_doi=[]
citedby_count=[]
affiliation=[]
#prism_aggregationType=[]
subtype=[]
subtypeDescription=[]
source_id=[]
openaccess=[]
total_result = []
cursor = []
link = []

header = pd.DataFrame()

resp = requests.get(url,
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': MY_API})

if not 200:
    print("An error has occured. [Status code", resp, "]")
        
else:
    try:
        data = resp.json() #Only convert to Json when status is OK.
        if not data['search-results']:
            print("Empty JSON")
        else:
            result = data['search-results']
            total_result.append(result['opensearch:totalResults'])
            cursor.append(result['cursor'])
            link.append(result['link'])
            
            for i in range(0, len(result['entry'])):
                if 'prism:url' in result['entry'][i]:
                    prism_url.append(result['entry'][i]['prism:url'])
                else:
                    prism_url.append('')
                if 'eid' in result['entry'][i]:
                    eid.append(result['entry'][i]['eid'])
                else:
                    eid.append('')
                if 'dc:creator' in result['entry'][i]:
                    dc_creator.append(result['entry'][i]['dc:creator'])
                else:
                    dc_creator.append('')
                if 'dc:title' in result['entry'][i]:
                    dc_title.append(result['entry'][i]['dc:title'])
                else:
                    dc_title.append('')
                if 'prism:publicationName' in result['entry'][i]:
                    prism_publicationNam.append(result['entry'][i]['prism:publicationName'])
                else:
                    prism_publicationNam.append('')
                if 'prism:issn' in result['entry'][i]:
                    prism_issn.append(result['entry'][i]['prism:issn'])
                else:
                    prism_issn.append('')
                if  'prism:eIssn' in result['entry'][i]:
                    prism_eIssn.append(result['entry'][i]['prism:eIssn'])
                else:
                    prism_eIssn.append('')
                if 'prism:issueIdentifier' in result['entry'][i]:
                    prism_issueIdentifier.append(result['entry'][i]['prism:issueIdentifier'])
                else:
                    prism_issueIdentifier.append('')
                if 'prism:coverDate' in result['entry'][i]:
                    prism_coverDate.append(result['entry'][i]['prism:coverDate'])
                else:
                    prism_coverDate.append('')
                if 'prism:coverDisplayDate' in result['entry'][i]:
                    prism_coverDisplayDate.append(result['entry'][i]['prism:coverDisplayDate'])
                else:
                    prism_coverDisplayDate.append('')
                if  'prism:doi' in result['entry'][i]:
                    prism_doi.append(result['entry'][i]['prism:doi'])
                else:
                    prism_doi.append('')
                if  'citedby-count' in result['entry'][i]:
                    citedby_count.append(result['entry'][i]['citedby-count'])
                else:
                    citedby_count.append('')
                if 'affiliation' in  result['entry'][i]:
                    if 'affilname' in result['entry'][i]['affiliation'][0]:
                        affiliation.append(result['entry'][i]['affiliation'][0]['affilname'])
                else:
                     affiliation.append('')
                if 'subtype' in result['entry'][i]:
                    subtype.append(result['entry'][i]['subtype'])
                else:
                    subtype.append('')
                if 'subtypeDescription' in result['entry'][i]:
                    subtypeDescription.append(result['entry'][i]['subtypeDescription'])
                else:
                    subtypeDescription.append('')
                if 'source-id' in result['entry'][i]:
                    source_id.append(result['entry'][i]['source-id'])
                else:
                    source_id.append('')
                if 'openaccess' in result['entry'][i]:
                    openaccess.append(result['entry'][i]['openaccess'])
                else:
                     openaccess.append('')
                        
    except(ValueError, KeyError):
        pass
    
df=pd.DataFrame({'prism_url': prism_url,
                'eid': eid,
                'dc_title': dc_title,
                'dc_creator': dc_creator,
                'prism_publicationNam': prism_publicationNam,
                'prism_issn': prism_issn,
                'prism_eIssn': prism_eIssn,
                'prism_coverDate': prism_coverDate,
                'prism_coverDisplayDate': prism_coverDisplayDate,
                'prism_doi': prism_doi,
                'citedby_count': citedby_count,
                'affiliation': affiliation,
                'subtype': subtype,
                'subtypeDescription': subtypeDescription,
                'source_id': source_id,
                'openaccess': openaccess})

df_new = df.append([total_result, cursor, link], ignore_index=True)

df_new.to_csv("the_file_name.csv", index=False, encoding='utf-8-sig')

