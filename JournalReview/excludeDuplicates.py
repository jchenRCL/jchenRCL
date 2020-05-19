# subset data frame whose title names not in duplicated_title_name and issns not in duplicated_issns

sud_j_code_exclude_dup=sud_j_code[(sud_j_code['Title Name'].apply(lambda x : x not in list(dup_ttl_unique['Duplicated Title']))) & \
(sud_j_code['ISSN'].apply(lambda x: x not in list(dup_issn_unique['ISSN'])))]

sud_j_code_exclude_dup.reset_index(inplace=True, drop=True)


