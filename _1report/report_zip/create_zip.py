import zipfile
import os

ROOT_PATH = os.getcwd()
temp_dir_for_archive = os.path.join(ROOT_PATH, 'temp')

if not os.path.exists(temp_dir_for_archive):
    os.mkdir(temp_dir_for_archive)

path_to_file = os.path.join(ROOT_PATH, 'example.pdf')

if not os.path.exists(path_to_file):
    with open(path_to_file, 'a') as f:
        f.write('Hello World')

result_zip = os.path.join(temp_dir_for_archive, 'example2.zip')

# def __init__(self, file, mode="r", compression=ZIP_STORED, allowZip64=True,
#              compresslevel=None, *, strict_timestamps=True, metadata_encoding=None):
# Создание архива
with zipfile.ZipFile(result_zip, 'w',compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    z.write(path_to_file, os.path.basename(path_to_file), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    password = bytes('password1', encoding='utf-8')
    z.setpassword(bytes('pwd', encoding='utf-8'))
    z.close()