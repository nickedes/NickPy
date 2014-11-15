import os,shutil

sources = ["E://Cmder"]
dest_root = "C:\\Mirror\\"

if os.path.exists(dest_root):
    shutil.rmtree(dest_root)

ignore_folders = ['.git', 'lib', 'env', 'bin', '.Trash']
ignore_files = ['.DS_Store', '.localized']
for src in sources:
    for cur_fol, dirs, files in os.walk(src, topdown=True):
        for ignore in ignore_folders:
            if ignore in dirs:
                dirs.remove(ignore)

        for ignore in ignore_files:
            if ignore in files:
                files.remove(ignore)

        dest_dir = cur_fol.replace(src, dest_root)

        for dirname in dirs:
            destination = os.path.join(dest_dir, dirname)
            if not os.path.exists(destination):
                os.makedirs(destination)

        for filename in files:
            b = os.path.join(cur_fol, filename)
            destination = os.path.join(dest_dir, filename)
            if not os.path.exists(destination):
                open(destination, "w").close()
                stinfo = os.stat(b)
                os.utime(destination,(stinfo.st_atime,stinfo.st_mtime))
