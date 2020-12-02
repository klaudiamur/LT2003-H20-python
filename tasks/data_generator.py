"""
create a class that given a list of text files will at each iteration return
the first line of the text only if the file is not suppose to be ignored (see example files below)

example:

lets assume we have the following files and that the first line of each file is the name of the file

files = ["file1.txt", "file2.txt", "ingore_this_file1.txt", "file3.txt", "ingore_this_file1.txt", "file4.txt"]


following code should run:

>> my_generator =  DataGenerator(files)
>> for data in my_generator:
..      print(data)
..      if "3" in data:
..          break
>>"file1.txt"
>>"file2.txt"
>>"file3.txt"
>> next(my_generator)
>>"file4.txt"

"""

class DataGenerator:
    def __init__(self, files):
        #the constructor of DataGenerator class holds the "filtered" files as one of its attributes
        new_files = [file for file in files if open(file).readline() == file]
        self.files = list(new_files)

    def __iter__(self):
        #the _iter_ function initializes the index of the iterator i.e. 0
        self.i = 0
        return self

    def __next__(self):
        #gets the file name in the next index
        next_file = self.files[self.i]
        #increment the index by 1
        self.i += 1
        return next_file


# #Uncomment to test
# files = ["file1.txt", "file2.txt", "ignore1.txt", "file3.txt", "ignore2.txt", "file4.txt"]
# my_generator =  DataGenerator(files)
# for data in my_generator:
#     print(data)
#     if "3" in data:
#         break
# print(next(my_generator))
