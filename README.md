# remove_softlinks.py

You are given a directory named file_dir with the following files

file1: a text file with content "hello"

file2: a softlink pointing to file1 (Hint: create file2 in shell by "ln -s file1 file2")

file3: a softlink pointing to file2

file4: a text file with content "bye"

root: a softlink pointing to /  

empty_dir: an empty directory
 
Assume there's no hard links under file_dir

You need to remove all the softlinks that point to any files (or directories) under file_dir. With that said, don't remove softlinks that point to file (or directories) outside file_dir.
