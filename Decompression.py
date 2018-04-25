#import Compressor as Comp


class Decompressor():

    hash_pairs = []
    hash_d = {}
    n_file_data = []
    final_file = ""

    def read_file(self):
        self.compFile = open("test2.txt", "r")
        self.hashFile = open("hash_file.txt", "r")

    def map_hash(self):
        for i in self.hashFile:
            self.hash_pairs.append(i.split())
            print("this is a hash_pair")
            print(self.hash_pairs)

    def new_hash(self):
        i = 0
        while i <len(self.hash_pairs):
            self.hash_d[self.hash_pairs[i][1]] = self.hash_pairs[i][0]
            i+=1
        print(self.hash_d)

    def replace_keys_with_word_in_compressed_file(self):
        self.n_file_data = self.compFile.read().split()
        print("this new file data")
        print(self.n_file_data)
        i=0
        while i < len(self.n_file_data):
            if self.n_file_data[i] in self.hash_d.keys():
                self.n_file_data[i] = self.hash_d[self.n_file_data[i]]
            i+=1
        for elem in self.n_file_data:
            self.final_file = self.final_file + elem + " "

    def decompressed_file(self):
        fo6 = open("decompressed.txt","w")
        fo6.write(self.final_file)
        fo6.close()
        fo7 = open("decompressed.txt","r")
        print(fo7.read())


d = Decompressor()
d.read_file()
d.map_hash()
d.new_hash()
d.replace_keys_with_word_in_compressed_file()
d.decompressed_file()
