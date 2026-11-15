# bonus: sentence Palindrome

sentence = input("Enter a sentence: ")

clean_sentence = sentence.replace(" ", "").lower()

if clean_sentence == clean_sentence[::-1]:
     print("Palindrome")
else:
     print("Not a palindrome")
     
