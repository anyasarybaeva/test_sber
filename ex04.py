'''
4) Написать скрипт который группирует слова по "общим буквам"
# Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
'''
from collections import defaultdict

def group_words(words):
    resul = defaultdict(list)
    for word in words:
        key=str(sorted(word))
        resul[key].append(word)

    return(resul.values())

ans=group_words((input()).split(','))
print(ans)
