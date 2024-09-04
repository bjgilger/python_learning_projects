import zipfile
import pathlib


def make_archive(filepaths, directory):
    dest_path = pathlib.Path(directory, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


