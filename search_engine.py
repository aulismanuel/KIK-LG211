#1 Giving the text for the program

documents = [
    "This is an example that is different from the one online",
    "A better example indeed",
    "I just want to play around a bit",
    "I must say this example is a bit better than the online one",
    "And I add this one example more"
]

#2 Making a document-term matrix

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(lowercase=True, binary=True)
sparse_matrix = cv.fit_transform(documents)
dense_matrix = sparse_matrix.todense()
print(dense_matrix)

#3 Transposing to term-document matrix (the .T in the end)

td_matrix = dense_matrix.T
print(td_matrix)

#4 Getting an ordered list (array) of terms. This shows a list of all terms in alphabetical order.

terms = cv.get_feature_names_out()
print(terms)

print("First term (with row index 0):", terms[0])
print("Third term (with row index 2):", terms[2])

#5 Another way of making a list of terms. This shows a map from term to index,
#  in the order in which the words occur in the text, and shows the alph. index aside. 

print(cv.vocabulary_)

#6 Searching an index of a single word: (It seems this only gives the index of the first occurrence)

print(cv.vocabulary_["example"])

#   SSSSSS  EEEEEEE     A     RRRRR      CCCCC  HH   HH  IIII  NNN   NN    GGGGG  #
#  SSS      EE         AAA    RR  RRR  CCC      HH   HH   II   NNNN  NN  GGG      #
#   SSSSS   EEEEE     AA AA   RRRRR    CC       HHHHHHH   II   NN NN NN  GG  GGG  #
#      SSS  EE       AAAAAAA  RR RRR   CCC      HH   HH   II   NN  NNNN  GGG  GG  #
#  SSSSSS   EEEEEEE AAA   AAA RR   RRR   CCCCC  HH   HH  IIII  NN   NNN    GGGGG  #

#7  We are using the td_matrix which was declared at #3, together with cv.vocabulary_ from #6
#   t2i ~ term to index

t2i = cv.vocabulary_
print(td_matrix[t2i["example"]])

#8  Querying with AND operator

print(td_matrix[t2i["example"]] & td_matrix[t2i["better"]])

#9  And with OR operator

print(td_matrix[t2i["example"]] | td_matrix[t2i["better"]])

#10 Finally the NOT operator. 1 - x returns 0 as 1 and 1 as 0. (1-1=0 and 1-0=1)

print(1 - td_matrix[t2i["example"]])


