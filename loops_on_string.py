##these are exercises about applying loops on strings in Python###


# (1)reverse a string
# 1st way:use string concatenation

def reverse_a_string_01(string):
    length = len(string)
    result = ""
    for i in range(1,length+1):
         result += string[length-i]
    return result

# 2nd way: applying a list
   
def reverse_a_string_02(text):
    length = len(text)
    lst = []
    for i in range(1,length+1):
         lst.append(text[length-i])
    return "".join(lst)

     

#(2) remove all vowels(both lower case and upper case) in a string
def anti_vowel(text):
   vow = "aeiouAEIOU"
   result = " "
   for char in text:
   	     if char not in vow:
   	    	 result += char
   return result

#(3) scrabble_score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    word = word.lower()
    total_score = 0
    for char in word:
    	if char.isalpha():
             total_score += score[char] 
    return total_score


# execute functions
input = raw_input("input a string:")
print "The reversed string is: " + reverse_a_string_01(input)
print "The reversed string is: " + reverse_a_string_02(input)
print "Removing all the vowels, here is your remainning string: " + anti_vowel(input)
print "The scrabble score of your string is: " + str(scrabble_score(input))

