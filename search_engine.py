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

#queryInput = input("Searching for: ")
#print("Searching for \"" + queryInput + "\"...") # So this is just a placeholder to be replaced with correct functionality

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

def test_query(query):
    print("Query: '" + query + "'")
    print("Rewritten:", rewrite_query(query))
    print("Matching:", eval(rewrite_query(query))) # Eval runs the string as a Python command
    print()

test_query("example AND NOT nothing")
test_query("NOT example OR great")
test_query("( NOT example OR great ) AND nothing") # AND, OR, NOT can be written either in ALLCAPS
test_query("( not example or great ) and nothing") # ... or all small letters
test_query("not example and not nothing")