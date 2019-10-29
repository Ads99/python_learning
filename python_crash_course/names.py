name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

# whitespace demo
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitepace - this is best seen in a terminal session without print statements
favourite_language = 'python  '
print(len(favourite_language))
print(len(favourite_language.rstrip()))
# however, note aboe that the variable is unchanged by rstrip()
# to change the variable we need to re-assign
favourite_language = favourite_language.rstrip()
print(len(favourite_language))

message = "One of Python's strengths is its diverse community"
print(message)
# incorrect use of apostrophes
#message = 'One of Python's strengths is its diverse community'