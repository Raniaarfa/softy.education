
def polyndrome(word):
    n = len(word)
    is_polyndrome = True

    for i in range (n // 2):
        if word[i] != word[n - i - 1]:
            is_polyndrome = False
    if is_polyndrome : 
        print(word , "is palyndrome")
    else :
        print(word, "is not palyndrome ")

word = input("Enter your word : ")
polyndrome(word)
    
# 2nd method
def if_palyndrome(i):
    reverse = i [::-1]
    if (i == reverse):
        return True
    return False

n = input ("\nEnter your word :  ")
if if_palyndrome(n):
    print(n, "is polyndrome")
else:
    print(n, "is not polyndrome")