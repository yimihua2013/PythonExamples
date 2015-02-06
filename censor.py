'''
Write a function called censor that takes two strings, text and word, as input.
It should return the text with the word you chose replaced with asterisks.
For example:
censor("this hack is wack hack", "hack") 
should return:
"this **** is wack ****"
'''
def censor(text, word):
    list = text.split()
    lens = len(word)
    new_text = []
    for i in range(len(list)):
         if list[i]== word:
             list[i]= lens * "*"
             new_text.append(list[i])
         else:
         	 new_text.append(list[i])

    return " ".join(new_text)

a = raw_input("input your text for the censorship: ")
b = raw_input("input a sensitive word: ")

print "You are going to censor the text on the word: " + b
print "The result after censoring is: " + censor(a,b)