import operator


class Compressor:


    word_list = []
    sorted_counted_of_word ={}
    hash_symbols = {}
    file_data = []
    s = ""
    # read the original file to be compressed

    def read_file(self):

        file_name = "bigfile.txt"
        fo = open(file_name, "r")
        self.word_list = fo.read().split()
        fo.close()

    # get a list of tuples with words arranged in descending order of their count
    def get_sorted_tuple(self):

        count_of_words = {}
        for elem in self.word_list:
            count_of_words[elem] = self.word_list.count(elem)
        self.sorted_counted_of_words = sorted(count_of_words.items(), key=operator.itemgetter(1), reverse=True)


    # make hash values that are to be replaced with the original strings in the file

    def make_hash(self):
        k = 0
        j = 0
        while k < len(self.sorted_counted_of_words):
            h = str(j)
            if len(self.sorted_counted_of_words[k][0]) >= len(h) and self.sorted_counted_of_words[k][1] > 2:
                self.hash_symbols[self.sorted_counted_of_words[k][0]] = h
                j += 1
            k += 1
            h = ""


    def create_compressed_file(self):

        fo2 = open("bigfile.txt", "r")
        self.file_data = fo2.read().split()
        print(self.s)
        for elem in self.file_data:
            print(self.file_data)
            if elem in self.hash_symbols.keys():
                print(elem)
                elem = self.hash_symbols[elem]
                self.s = self.s + elem + " "
            else:
                self.s = self.s + elem + " "



        fo2.close()
        fo3 = open("test2.txt", "w")
        fo3.write(self.s)
        fo3.close()
        fo4 = open("test2.txt", "r")
        print("file")
        print(fo4.read())

    fo_hash = open("hash_file.txt", "w")

    def create_hash_table(self):

        for k in self.hash_symbols:
            self.fo_hash.write(k)
            self.fo_hash.write(" ")
            self.fo_hash.write(self.hash_symbols[k])
            self.fo_hash.write("\n")


c = Compressor()
c.read_file()
c.get_sorted_tuple()
c.make_hash()
c.create_compressed_file()
c.create_hash_table()
