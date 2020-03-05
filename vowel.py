vowels = {"a","e","i","o","u"}
app_vow = set()

wo = input("Enter word/name here: ")
word = wo.lower()
c = 0
for i in range(len(word)):
   if word[i] in vowels:
           c += 1
           app_vow.add(word[i])
           
print("{} has {} vowels in it, i.e. {}".format(wo,c,app_vow))

