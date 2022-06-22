'''Предположим у вас есть очень длинная строка (без пробелов и только латинские символы), которая занимает 100Мб, но у вас в распоряжении есть 120Мб оперативной памяти, необходимо отсортировать данную строку по алфавиту.
Напишите скрипт который сделает это.
# Input 'gbdqeslzepkolhshqvuampvktavtjdihrwxalzwfqbdvyqwnjuplaocaupyqkdilhfknvegymnzqrpmdpoibphszadihqgisgmjn'
# Output 'aaaaaabbbcddddddeeeffgggghhhhhhiiiiijjjkkkklllllmmmmnnnnooopppppppqqqqqqqrrssssttuuuvvvvvwwwxyyyzzzz
'''

def sort_str(str):
    dict={}
    for i in range(len(str)):
        if str[i] not in dict:
            dict[str[i]]=0
        dict[str[i]]+=1
    str=""
    for key in sorted(dict):
        str+=key*int(dict[key])
    return(str)

print(sort_str(input()))