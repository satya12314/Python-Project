text=str(input("Enter the Phrase : "))
text=text.split()
print(text)
acronym=''
for i in text:
    acronym+=i[0].upper()
print(acronym)