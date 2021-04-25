import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu

df = pd.read_csv("colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv", sep="\t", index_col=0)
df["ttest"] = [ttest_ind(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
df = df.sort_values("ttest")
print('ttest:',df.iloc[:10].index)

df = pd.read_csv("colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv", sep="\t", index_col=0)
df["mannwhitneyu"] = [mannwhitneyu(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
df = df.sort_values("mannwhitneyu")
print('mannwhitneyu:',df.iloc[:10].index)

'''ttest: Index(['C17orf96', 'IER5L', 'FUT1', 'CDH3', 'FXYD5', 'ZNHIT2', 'CLCA4',
       'ACADSB', 'MT1F', 'PIGN'],
      dtype='object')
mannwhitneyu: Index(['SFTA2', 'RAET1L', 'CTD-2147F2.1', 'LINC00460', 'AC007128.1',
       'RP5-884M6.1', 'VAC14-AS1', 'RP11-399O19.9', 'CST1', 'LINC00858'],
      dtype='object')'''