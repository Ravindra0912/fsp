import operator
string = "hello how are you my friend friends friend hello"
word_list=[]
fo = open("bigfile.txt" , "r")
#print(fo.read())

word_list = fo.read().split()
print(word_list)
#word_list=string.split()
count_of_words = {}
#print(string)
for elem in word_list:
    count_of_words[elem] = word_list.count(elem)
sorted_counted_of_words = sorted(count_of_words.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_counted_of_words)
hash_table = {}

hash_symbols = {}
k=0
j=0
while k<len(sorted_counted_of_words):
    h = str(j)
    if(len(sorted_counted_of_words[k][0])>= len(h) and sorted_counted_of_words[k][1] > 2):
        hash_symbols[sorted_counted_of_words[k][0]] = h
        j+=1
    k+=1
    h=""
print(hash_symbols)
fo.close()
fo2 = open("bigfile.txt","r")
#print(fo2.read())
filedata = fo2.read().split()
print("file data")
print(filedata)
s=""
for elem in filedata:
    #print(elem)

    if(elem in hash_symbols.keys()):
        elem = hash_symbols[elem]
        s = s + elem+" "
    else:
        s = s+ elem +" "
fo2.close()
fo3 = open("test2.txt","w")
fo3.write(s)
fo3.close()
fo4 = open("test2.txt","r")
print("file")
print(fo4.read())
fo_hash = open("hash_file.txt","w")
#fo_hash.write(str(hash_symbols))
for k in hash_symbols:
    fo_hash.write(k)
    fo_hash.write(hash_symbols[k])
