surname = ["Michael","David","Frank","Isaac","George"]
firstname = surname

#
""" firstname.append("Fobi")
print(surname)
print(firstname) """

#using the swallow copying

firstname =list(surname)
firstname.append("Fobi")
print(surname)
print(firstname)
