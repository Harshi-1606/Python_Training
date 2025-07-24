s = 'ABCABC'
n = 3
palindromes = []

def check_palindrome(s1):
    return s1 == s1[::-1]

for i in range(0, len(s)-n +1):
    substr = s[i:i+n]
    if check_palindrome(substr):
        palindromes.append(substr)

print("Palindromic substrings of length", n, "are: ", palindromes)

check_palindrome(s)

'''wap using function that calculates and returns the total price of an item including tax
Scenario: This  program works for  small shop where the user enters the price of an item and we have 
list of tax amount by default
List: 3%, 5% 7% 
List of Items: Books, Pen, Mobile
'''

l1 = ['books', 'pen', 'mobile']
l2 = [3, 5, 7]
combined = (list(zip(l1, l2)))
print(combined)
for i, j in zip(l1, l2):
    print(i, j)