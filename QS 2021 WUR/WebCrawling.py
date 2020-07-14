'''
The script is used for scrapping faculty records on QS 2021 World University Ranking website
'''
import requests
from bs4 import BeautifulSoup 

UniName = []
WUR = []
status = []
ResearchOutput = []
TolStudent = []
AcademicFaculty = []
InStudent = []


url = 'https://www.topuniversities.com/universities/{}'
    
        
for i in range(55, 100):
    soup = BeautifulSoup(requests.get(url.format(name_drop_the_brace_OK[i])).content, "html.parser")
            # Find the table which contains the information I want
    x = soup.find(name="div", attrs={"class": "uni_stats"})
    
    try:

        if len(list(x.text.split('\n'))) > 22:
            try:
                UniName.append(name_drop_the_brace_OK[i].strip())
                WUR.append(x.text.strip().split('\n')[1])
                status.append(x.text.strip().split('\n')[4])
                ResearchOutput.append(x.text.strip().split('\n')[7])
                TolStudent.append(x.text.strip().split('\n')[10])
                AcademicFaculty.append(x.text.strip().split('\n')[16])
                InStudent.append(x.text.strip().split('\n')[19])
                
            except IndexError:
                UniName.append(name_drop_the_brace_OK[i].strip())
                WUR.append('')
                status.append('')
                ResearchOutput.append('')
                TolStudent.append('')
                AcademicFaculty.append('')
                InStudent.append('')
        elif len(list(x.text.split('\n'))) < 22:
        
            try:
                UniName.append(name_drop_the_brace_OK[i].strip())
                WUR.append(x.text.strip().split('\n')[1])
                status.append('')
                ResearchOutput.append('')
                TolStudent.append(x.text.strip().split('\n')[4])
                AcademicFaculty.append(x.text.strip().split('\n')[7])
                InStudent.append(x.text.strip().split('\n')[10])
            
            except IndexError:
                UniName.append(name_drop_the_brace_OK[i].strip())
                WUR.append('')
                status.append('')
                ResearchOutput.append('')
                TolStudent.append('')
                AcademicFaculty.append('')
                InStudent.append('')
        else:
            
            try:
                
                UniName.append(name_drop_the_brace_OK[i].strip())
                WUR.append(x.text.strip().split('\n')[1])
                status.append(x.text.strip().split('\n')[4])
                ResearchOutput.append(x.text.strip().split('\n')[7])
                TolStudent.append(x.text.strip().split('\n')[10])
                AcademicFaculty.append(x.text.strip().split('\n')[13])
                InStudent.append(x.text.strip().split('\n')[16])
            
            except IndexError:
                
                UniName.append(name_drop_the_brace_OK[i].strip())
                WUR.append('')
                status.append('')
                ResearchOutput.append('')
                TolStudent.append('')
                AcademicFaculty.append('')
                InStudent.append('')
                
    except (RuntimeError, TypeError, NameError, AttributeError):
                
        UniName.append(name_drop_the_brace_OK[i].strip())
        WUR.append('')
        status.append('')
        ResearchOutput.append('')
        TolStudent.append('')
        AcademicFaculty.append('')
        InStudent.append('')
            

df = pd.DataFrame({'University': UniName,
                  'Ranking': WUR,
                  'Status': status,
                  'Research Output': ResearchOutput,
                  'Total Student': TolStudent,
                  'Academic Faculty': AcademicFaculty,
                  'International Student': InStudent})

df
