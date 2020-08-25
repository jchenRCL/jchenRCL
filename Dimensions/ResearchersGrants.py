# Below is the script demonstrating how to query grants if given a list of researchers' Dimensions ids.
# Also, how to normalize the nested json data formats.
# Lastly, the script to concatenating several normalized datasets together

# import required libraries

import pandas as pd
import numpy as np
import json
import requests

!pip install dimcli -U

# I have created a local credential. Otherwise, can try log in with user name and password. Details in the Dimensions API lab: https://docs.dimensions.ai/dsl

import dimcli
dimcli.login()
dsl = dimcli.Dsl()
dimcli.login()

# create a list for researchers' ids

researcher_id = ['ur.01215450000.22','ur.011725645715.40','ur.01244272356.36','ur.01105074143.21','ur.01033403276.88',
                'ur.015324333431.33','ur.0720260005.12','ur.0665714166.39']
  
# Use iterative to query all researchers within UR
                
data = dsl.query_iterative("""search researchers 
where research_orgs in ["grid.461628.f", "grid.412750.5", "grid.414078.e", "grid.416663.0"] 
and obsolete=0 return researchers""")

# There is a column called "id" which is the Dimensions id of the researchers.
# To this end, I have found the UR's researchers by their Dimensions ids

data_df.head()

# subset the researchers I am interested in

ur_researchers = data_df[data_df['id'].apply(lambda x: x in researcher_id)]

ur_researchers.reset_index(inplace=True, drop=True)

# Take Natalie as an example. This way, I got her grants data

Natalie_grants = json_normalize(ur_researchers.iloc[0,:]['research_orgs'])

# I hope to create a data frame with her first and last name as the columns as well

Natalie_grants['first_name'] =ur_researchers.iloc[0,:]['first_name']

Natalie_grants['last_name'] =ur_researchers.iloc[0,:]['last_name']


# Lastly, the script below is to show how to concatenate all the normalized datasets

chuck = []

for i in range(len(ur_researchers)):
    chuck.append(pd.json_normalize(ur_researchers.iloc[i,:]['research_orgs']))

test_df = pd.concat(chuck)

