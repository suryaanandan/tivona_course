def Vowel_check(input_char):
    if (input_char == 'a' or input_char ==  'e' or input_char == 'i' or input_char == 'o' or input_char == 'u' or input_char == 'A' or input_char == 'E' or input_char == 'I' or input_char == 'O' or input_char == 'U'):
        return "True"
        
    else:
        return "False"
        
input_char=input("Enter the letter to check:")
if Vowel_check(input_char) == "True":
    print("True")
else:
    print("False")