def duplicate_encode(word):
    lcase_word=word.lower()
    ans = ""
    wordlist = [i for i in lcase_word]
    for j in wordlist:
        if wordlist.count(j) > 1:
            ans+=")"
        elif wordlist.count(j) == 1:
            ans+="("
    return ans