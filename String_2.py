course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course)       # But Original doesn't affect
print(course.lower())
print(course)       # But Original doesn't affect

# To Find Letter In Sentence
print(course.find('y'))       # It gives the index of that character
print(course.find('Y'))      # if the character is not in sentence then it will throw -1
print(course.find('Beginners'))

# To Replace
print(course.replace('Beginners', 'Absolute_Beginners'))
print(course)  # But Still doesn't affect the Original String
print(course.replace('P', 'J'))
print(course)   # But Still doesn't affect the Original String

# To know whether the character or string is in or not -> if yes then it will return True else False
print('Python' in course)
