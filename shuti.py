import shutil
shutil.copy("op.txt","kk.txt")
shutil.copy("kk.txt","modules/")
shutil.copy2("op.txt","kk.txt")
shutil.move("kkk.txt","modules/")