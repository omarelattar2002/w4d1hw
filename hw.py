import re

# tweet1 = "Python is the best #Python #Programming #CodingTemple"

# pattern = re.compile(r'#\w*')

# f = pattern.findall(tweet1)

# print(f)

#this was for testing


tweets = ["Python is the best #Python #Programming #CodingTemple","I love my life! #blessed","Bear Down"]




def fun(tweets):
    return re.findall(r'#\w*',tweets)


for t in tweets:
    print('Expected output', fun(t))
