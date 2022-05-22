# 1_Run possible rsequences aganinst previous classified score matrix og actual binding site
# 2_We get a score matrix convert to csv

# This script combines the 'all possible sequence' and 'respective scores'
# 3_Get the 10 lowest scores and query against hg38 to show better corrections using psi-blast

import pandas as pd
Y = pd.read_csv('test.csv', sep="\t", header=None)
X = pd.read_csv('Combine_File.txt', sep="\t", header=None)
# print(X)
# print(Y)

result = pd.concat([X, Y], axis=1, join="inner")
result.columns = ['Sequence', 'Score']
#print(result)

result.to_csv('lookup.csv', sep='\t')

result.nsmallest(10, 'Score')
result.nlargest(10, 'Score')
