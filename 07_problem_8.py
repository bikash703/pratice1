# a=input("Enter your Message:\n")

# if("make a lot of money" in a):
#     spam = True
# elif("subscrube This" in a):
#     spam = True
# elif("click This" in a):
#     spam = True
# elif("buy Now" in a):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This is spam message")
# else:
#     print("This is not spam message")



text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")