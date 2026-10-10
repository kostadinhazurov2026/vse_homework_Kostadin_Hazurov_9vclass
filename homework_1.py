mode = input("Choose (1 - Encoding or 2 - Decoding): ")
text = input("Enter text: ")

if mode == "1":
    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    if text:
        encoded += text[-1] + str(count)

    print(encoded)

elif mode == "2":
    decoded = ""

    for i in range(0, len(text), 2):
        char = text[i]
        count = int(text[i + 1])
        decoded += char * count

    print(decoded)

else:
    print("Invalid number!")