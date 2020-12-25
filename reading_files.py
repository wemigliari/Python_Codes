import docx

# Reading files

#booklet = open("booklet_statistics.docx", "r") ### just reading the information
#print(booklet.read()) # Either READ function or READLINES
#print(booklet.readline())
#print(booklet.readlines())
#print(booklet.readable())

### The function READLINES just print one line, so we created a loop for reading the entire document
#for totals in booklet.readlines():
    #print(totals)

#booklet.close()

booklet = open("text_test.py", "r") ### writing information
print(booklet.readable())
print(booklet.read())

booklet.close()

#open("booklet_statistics.docx", "a") ### append information or adding you information
#open("booklet_statistics.docx", "w") ### append information or adding you information