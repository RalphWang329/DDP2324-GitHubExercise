def case_counter(text):
    str(text)

    lowercase = 0
    uppercase = 0

    for i in text:
        if i.islower():
            lowercase += 1
        elif i.isupper():
            uppercase += 1
    
    print("Uppercase letter:", str(uppercase) , "," , "Lowercase letter:" , str(lowercase) + ".")


case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
