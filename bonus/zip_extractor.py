import zipfile
def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("/Users/venka\PycharmProjects/todo_app/bonus\compressed1.zip", "/Users/venka\PycharmProjects/todo_app/bonus\dest")