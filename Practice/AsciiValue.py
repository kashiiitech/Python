# Asciivalue Programe

""" this will take integer as input from the user and tell us the ascii value of that integer """


"""The ASCII table contains letters, numbers, control characters, and other symbols. Each character is assigned a unique 7-bit code. ASCII is an acronym for American Standard Code for Information Interchange."""

asciiValue = int(input("Enter Any Num : "))
while asciiValue<256:
    alphabate = chr(asciiValue)
    print(alphabate)
    asciiValue += 1
    break
