#   DATA

documents = [
    "This is an example that is different from the one online",
    "A better example indeed",
    "I just want to play around a bit",
    "I must say this example is a bit better than the online one",
    "And I add this one example more",
    "There is really nothing great here"
]

import documents_library
wiki100 = documents_library.wiki100

#   QUERY PROMPT

queryInput = input("Searching for: ")

#   MAKING A MATRIX

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(lowercase=True, binary=True)
sparse_matrix = cv.fit_transform(wiki100)     # HERE THE DATA SOURCE IS CHOSEN
dense_matrix = sparse_matrix.todense()

td_matrix = dense_matrix.T

#   SEARCHING

t2i = cv.vocabulary_

            # Operators and/AND, or/OR, not/NOT become &, |, 1 -
            # Parentheses are left untouched
            # Everything else interpreted as a term and fed through td_matrix[t2i["..."]]

d = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}          # operator replacements

def rewrite_token(t):
    return d.get(t, 'td_matrix[t2i["{:s}"]]'.format(t)) # Can you figure out what happens here?

def rewrite_query(query): # rewrite every token in the query
    return " ".join(rewrite_token(t) for t in query.split())

#def test_query(query):
#    print("Query: '" + query + "'")
#    print("Rewritten:", rewrite_query(query))
#    print("Matching:", eval(rewrite_query(query))) # Eval runs the string as a Python command
#    print()
#
#test_query("example AND NOT nothing")
#test_query("NOT example OR great")
#test_query("( NOT example OR great ) AND nothing") # AND, OR, NOT can be written either in ALLCAPS
#test_query("( not example or great ) and nothing") # ... or all small letters
#test_query("not example and not nothing")

hits_matrix = eval(rewrite_query(queryInput))
hits_list = list(hits_matrix.nonzero()[1])

print("Searching for \"" + queryInput + "\"...")
if (len(hits_list) == 1):
    print("One (1) matching article was found.")
if (len(hits_list) > 1):
    print("A total of " + str(len(hits_list)) + " matching articles were found.")

#for i, doc_idx in enumerate(hits_list):
#    print("Matching article #{:d}: {:s}".format(i, wiki100[doc_idx], "\n\n\n"))

for i, doc_idx in enumerate(hits_list, start=1):
    print("\n\nMatching article #" + str(i) + ":")
    print(wiki100[doc_idx][0:1500])

print("\n\nEnd of results.\n\n\n\n")