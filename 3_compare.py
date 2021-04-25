deseq2=set(['FABP6', 'ETV4', 'IER5L', 'KRT80', 'FUT1', 'C17orf96', 'CLDN1', 'ATG9B', 'KIAA1257', 'SLC51B'])
ttest=set(['C17orf96', 'IER5L', 'FUT1', 'CDH3', 'FXYD5', 'ZNHIT2', 'CLCA4', 'ACADSB', 'MT1F', 'PIGN'])
mann=set(['SFTA2', 'RAET1L', 'CTD-2147F2.1', 'LINC00460', 'AC007128.1', 'RP5-884M6.1', 'VAC14-AS1', 'RP11-399O19.9', 'CST1', 'LINC00858'])

print('deseq2+ttest',deseq2.intersection(ttest))
print('deseq2+mann',deseq2.intersection(mann))
print('ttest+mann',ttest.intersection(mann))

'''deseq2+ttest {'C17orf96', 'IER5L', 'FUT1'}
deseq2+mann set()
ttest+mann set()'''