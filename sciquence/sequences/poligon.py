import numpy as np

# np.random.seed(42)
#
# rts = np.random.rand(30, 120)
# sax_vsm = SAX_VSM(window=12)
#
# out = sax_vsm.fit(rts)
#
# print sax_vsm.timeseries

#print out

# from sklearn.feature_extraction.text import TfidfVectorizer
#
# tfvec = TfidfVectorizer()
#
# print tfvec.fit_transform(out)


from cy_searching2 import max_seq

x = np.array([1,2,3,4,5])

print max_seq(x)