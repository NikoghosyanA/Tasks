n = int(input())
d = {}
for _ in range(n):
    word = input()
    d.setdefault(word[0], []).append(word)
max_words = max(d.items(), key=lambda item: (len(item[1]), item[0]))
print(max_words[1][-1])
