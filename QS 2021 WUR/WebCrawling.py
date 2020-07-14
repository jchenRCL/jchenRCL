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
            
for i in range(400, 450): # specify the range to your interest
    
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
        
        
s1 = pd.Series(UniName, name='University')
s2 = pd.Series(WUR, name='Ranking')
s3 = pd.Series(status, name='Status')
s4 = pd.Series(ResearchOutput, name='Research Output')
s5 = pd.Series(TolStudent, name='Total Student')
s6 = pd.Series(AcademicFaculty, name='Academic Faculty')
s7 = pd.Series(InStudent, name='International Student')

test_df = pd.concat([s1,s2,s3,s4,s5,s6,s7], axis = 1)

