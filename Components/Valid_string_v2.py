def check_string(question):
    while True:
        response = input(question)
        x = response != '' and all(chr.isalpha() or chr.isspace() for chr in response)
        if x == False:
            print("Input must only contain letters")
        else: 
            return response.title()

question = "Please enter your name "
name = check_string(question)
print(name)      