while True:
    word = input("Введіть своє слово: ")
    new_word = ""
    for i in word:
        new_word += chr(ord(i)+1)
        e = new_word.replace("ѐ", "a")
        o = e.replace("{","a")
        d = o.replace("!", " ")
    print(d)