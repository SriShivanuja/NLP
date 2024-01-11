Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:/NLP_sem6/Detecting_WordPattern.py
pattern = [0-9]+
text= I bought 10 pens 2 days back
word pattern detected
10
2
------------------------------------------------
pattern = [a-z A-Z]+
text= Bowrrow me a 2 pen
word pattern detected
Bowrrow me a 
 pen
------------------------------------------------
pattern = [A-Z][a-z]+
text= get a book from Ram
word pattern detected
Ram
------------------------------------------------
pattern = [AEIOU aeiou]+
text= Natural Language Processing
word pattern detected
a
u
a
 
a
ua
e 
o
e
i
------------------------------------------------
pattern = [0-9]{2}-[0-9]{2}-[0-9]{4}
text= meeting is postponed to 11-01-2024
word pattern detected
11-01-2024
------------------------------------------------
pattern = [a-z]+[0-9]+@[a-z]+.[a-z]+
text= send this message to abc23@gmail.com for their reference
word pattern detected
abc23@gmail.com
------------------------------------------------
