
# turn nested lists into dictionary key value pairs
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {i[0]: i[1] for i in person}
# answer = {k : v for k,v in person}
# answer = dict(person)
print(answer)
