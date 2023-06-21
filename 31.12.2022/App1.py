text = input()
s = input()
if s.lower() in text.lower():
    for i in range(len(text)):
        for j in range(len(text)):
            if j - i == len(s):
                if s.lower() == text[i:j]:
                    print(i)
