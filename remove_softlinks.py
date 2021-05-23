import os
def remove_softlinks(folder):
	files={}
	inodes=set()
	cwd = os.getcwd()
	print(cwd)
	for file in os.listdir(cwd):
		print(file)
		inode= os.stat(file).st_ino
		if os.path.islink(file) and inode in inodes:
			print(f'this file :{file} is a link with inod: {inode}')
			print(f'{file} will be deleted')
			os.remove(file)
		elif os.path.isfile(file) :
			inodes.add(inode)


remove_softlinks('file_dir')


