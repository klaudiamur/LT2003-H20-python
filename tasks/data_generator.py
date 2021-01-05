


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
        self.files = files

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        first_line = open(self.files[self.i]).readline()
        #ignores the files that contain the word "ignore" in the first line
        if "ignore" not in first_line:
            self.i += 1
            return first_line
        else:
            self.i += 1
            return next(self)



files = ["file1.txt", "file2.txt", "ignore1.txt", "file3.txt", "ignore2.txt", "file4.txt"]
my_generator =  DataGenerator(files)
for data in my_generator:
    print(data)
    if "3" in data:
        break
print(next(my_generator)) #assuming that the next element is not to be ignored
