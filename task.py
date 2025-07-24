def clean_and_sort_names(name_string):
    names = name_string.split(',')
    cleaned_names = [name.strip().title() for name in names]
    cleaned_names.sort()
    return cleaned_names

name_string = " Harshith, Yashas, Abhijith, Akash, Joyal "
print(clean_and_sort_names(name_string))

# Wap to check the given string is palindrome or not

