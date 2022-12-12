'''1.Create New Python File
2. The user will input 4 information (2 nouns and 2 adjectives)
3. Search for any poem or song on the internet (use 1 stanza only)
4. Replace the poem or song lyrics string with the nouns and adjectives
from user's input.
5. Display the original song and poem and display the result (nouns and
adjectives must be in ALL CAPS).
6. Upload the "py" file here. (filename should be lastname_firstname_day2_act1.py'''

noun1 = str(input("Input the first noun: "))
noun2 = str(input("Input the second noun: "))
adjective1 = str(input("Input the first adjective: "))
adjective2 = str(input("Input the second adjective: "))

poem = "Today on your birthday consider your luck, You could have been born as fat pig, big cow, or little duck."
poem2 = "Today on your birthday consider your luck, You could have been born as fat pig,{} {}, or {} {}."
poem2 = poem2.format(noun1.upper(), adjective1.upper(), noun2.upper(), adjective2.upper())
print("Original poem: ", poem)
print("Result: ", poem2)