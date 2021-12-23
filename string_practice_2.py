letter = '''Dear <|NAME|>,
 greeding from abc coding ,i am happy to tall you
you are selected 
 DATE : <|DATE|>'''

 
name = input("enter the name \n")
date = input("entre the date \n")

letter = letter.replace(" <|NAME|>",name)
letter = letter.replace(" <|DATE|>",date)

print(letter)
