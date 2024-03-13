import re

# tweet1 = "Python is the best #Python #Programming #CodingTemple"

# pattern = re.compile(r'#\w*')

# f = pattern.findall(tweet1)

# print(f)

#this was for testing

#EX1
tweets = ["Python is the best #Python #Programming #CodingTemple","I love my life! #blessed","Bear Down"]

def fun(tweets):
    return re.findall(r'#\w*',tweets)

for t in tweets:
    print('Expected output', fun(t))

#EX2
all_usernames = ["CodingTemple123", "1love", "CT", "This_is_a_username_that_I_would_like_to_use", "brian_ct123"]


def validate(user):
    pattern = re.compile(r'^[A-Za-z]\w{3,16}$')
    answer = re.match(pattern, user)
    if answer:
        print('correct')
    else:
        print('wrong')
    
for u in all_usernames:
    print(validate(u))


#EX3
    import re

with open('example.txt', 'r') as file:
    data = file.read()
    
print(data)

pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
correct_order = re.finditer(pattern,data)






