import zipfile as z

def make_archive(filepath, folderpath):
    with z.ZipFile(folderpath, 'x') as file:
        for filepath in filepath:
            file.write(filepath)
            
# if __name__ == '__main__':
    # def make_archive()