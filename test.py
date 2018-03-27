import operator
string = "hello how are you my friend friends friend hello"
word_list=[]
word_list=string.split()
count_of_words = {}
ss = string.replace("hello","#")
print(string)
for elem in word_list:
    count_of_words[elem] = word_list.count(elem)
sorted_counted_of_words = sorted(count_of_words.items(),key=operator.itemgetter(1),reverse=True)
print(count_of_words)
print(sorted_counted_of_words)
s=""
dic = {'hello':"#",'friend':"*"}
hash_symbols = ['#','%','@']
for elem in word_list:
    #print(elem)
    if(elem in dic.keys()):
     #   print(elem)
    #    print(s)
        s = string.replace(elem,dic[elem])
        string = s
print(s)
