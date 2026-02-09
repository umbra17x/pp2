#Example1(Sort a list of tuples by the second element)
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#Example2(Sort strings by length)
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
#Example3
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_by_name = sorted(students, key=lambda x: x[0])
print(sorted_by_name)
#Example4
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_desc)