s = "i am a coder"

print(s.endswith("co")) # returns False if string does not end with the given substring.
print(s.endswith("er")) # returns True if string ends with the given substring. 

print(s.capitalize()) # capitalize 1st char.

print(s.replace("i am", "you are")) # replaces all occurraences
print(s.find("o")) # return 1st index of 1st occurrences.

print(s.count("a")) # counts the occurrences of substr in string.