folder_name = "b139"
num_of_files = 6
import os
import string
import shutil
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
for i in range(num_of_files):
    dstpath = "{0}/{1}.py".format(folder_name,
                                  string.ascii_lowercase[i])
    if not os.path.exists(dstpath):
        shutil.copyfile("template.py", dstpath)
        print("file {0} was created".format(dstpath))