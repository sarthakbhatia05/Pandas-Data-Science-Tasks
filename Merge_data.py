import pandas as pd
import glob

#merging data
path = r'D:\VS code\Sales analysis with pandas\Pandas-Data-Science-Tasks\SalesAnalysis\Sales_Data'
filenames = glob.glob(path + "/*.csv")

dfs =[]
for filename in filenames:
    dfs.append(pd.read_csv(filename))

sales = pd.concat(dfs, ignore_index=True)

sales.to_csv('Sales Merge.csv',index= False)