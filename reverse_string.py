def reverse_string(text):
    output = ""

    for i in range(len(text)):
        output = text[i] + output

    print(output)

reverse_string("ayod")  