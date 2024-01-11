import re
def detect_word_pattern(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        print ("word pattern detected")
        for i in matches :
            print(i)
    else:
        print("no word pattern detected")
sample_inputs=[("[0-9]+","I bought 10 pens 2 days back"),#Detecting the digit's from the text
               ("[a-z A-Z]+","Bowrrow me a 2 pen"),#Detecting words from the text
               ("[A-Z][a-z]+","get a book from Ram"),#Detecting the name which is in capital followed by small letter
               ("[AEIOU aeiou]+","Natural Language Processing"),#Detecting the vowels from the text
               ("[0-9]{2}-[0-9]{2}-[0-9]{4}","meeting is postponed to 11-01-2024"),#Detecting the date from the text
               ("[a-z]+[0-9]+@[a-z]+.[a-z]+","send this message to abc23@gmail.com for their reference")]#Detecting the mailid from the text
for p,t in sample_inputs:
    print("pattern =",p)
    print("text=",t)
    
    detect_word_pattern(p,t)
    print("------------------------------------------------")
