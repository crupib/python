from scipy import stats
from scipy.sparse import csr_matrix
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print (x.max(),x.min(),x.mean(),x.var())
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print (stats.ttest_1samp(rvs,5.0))
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print (stats.ttest_ind(rvs1,rvs2))
G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],
                     [1, 0, 0] ])
                     
G_masked = np.ma.masked_values(G_dense, 0)
G_sparse = csr_matrix(G_dense)
print (G_sparse.data)
# not working
#from scipy.sparse.csgraph import csgraph_from_dense
#G2_data = np.array
#([
#   [np.inf, 2, 0 ],
#   [2, np.inf, np.inf],
#   [0, np.inf, np.inf]
#])
#G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
#print(G2_sparse.data)
wordlist = open('/usr/share/dict/words').read().split()
print (len(wordlist))

word_list = [word for word in wordlist if len(word) == 3]
word_list = [word for word in wordlist if word[0].islower()]
word_list = [word for word in wordlist if word.isalpha()]
print (len(word_list))
word_list = map(str.lower, wordlist)
