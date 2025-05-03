import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compress.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)

if __name__ == "__main__":  # to test we will use it.
    make_archive(filepaths= ["bonus1.py", "bonus3.py"], dest_dir = "dest")
