import random
import pandas as pd

file = open('all_genes.txt', 'r')

all_genes=[]
for line in file:
    all_genes.append(line.strip())

df=pd.DataFrame({})
for i in range(5):
    chosen_1000_genes=set()
    while len(chosen_1000_genes)<1000:
        new_gene=random.choice(all_genes)
        chosen_1000_genes.add(new_gene)
    chosen_1000_genes=list(chosen_1000_genes)
    df[i]=chosen_1000_genes

df.to_csv("chosen_genes.tsv", sep="\t")

