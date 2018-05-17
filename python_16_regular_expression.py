import re

# # patterns = ['term1','term2']

# text = "This is a string with term1, not te other!"

# match = re.search('term1', text)
# print(type(match.start()))
# # print((match.start()))

# split_term ="@"

# email = "user@gmail.com"
# # email.split(split_term)
# print(re.split(split_term,email))

# print(re.findall('match','test phrase match in match middle'))

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern{}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

# test_phrase = 'This is a string! But is has punctuation. How can we remove it?'
test_phrase = 'This is a string! with numbers 12312 and a symbol #hasing'

# test_pattern = ['[^!.?]+']
# test_pattern = ['[A-Z][a-z]+']
# test_pattern = [r'\w'] AlphaNumeric
# test_pattern = [r'\W'] Not AlphaNumeric

test_pattern = ['[^!.?]+']
test_pattern = [r'\W+']

multi_re_find(test_pattern,test_phrase)