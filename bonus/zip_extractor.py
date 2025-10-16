import zipfile

def extract_archive(archive_path, dest_folder):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_folder)


#
# if __name__ == "__main__":
#     extract_archive("compressed.zip", r"C:\Users\ayarl\PycharmProjects\Todo-App-Python-GUI\bonus\dest")