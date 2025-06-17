'''
Question number 5 of IPA Sample questions pdf

Sample Input-
Hello Hi Bye TCS Hello Welcome Hello Bye

Sample Output-
Hello



'''

def count_words(input_string):
    words=input_string.split()
    res={}
    for i in words:
        res[i]=words.count(i)
    return res

def max_occurence_word(input_string):
    d=count_words(input_string)
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]






if __name__ == '__main__':
    input_string=input()
    dict=count_words(input_string)
    st=max_occurence_word(input_string)
    print(st)