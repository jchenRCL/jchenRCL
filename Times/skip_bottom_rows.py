chuck = []
for i in range(2, 23):
    path = f"test_data_{i}.csv"
    chuck.append(pd.read_csv(path, skipfooter = 3, engine = 'python')) # skip bottom 3 rows
combine_file = pd.concat(chuck)
combine_file
