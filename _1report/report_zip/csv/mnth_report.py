import csv
import os
import subprocess

ROOT_PATH = os.getcwd()
temp_dir_for_result = os.path.join(ROOT_PATH, 'temp')

if not os.path.exists(temp_dir_for_result):
    os.mkdir(temp_dir_for_result)

result_zip_file = os.path.join(temp_dir_for_result, 'result.7z')
PASSWORD = '-ptest1'

target_file = os.path.join(ROOT_PATH, 'pythonworldru.pdf')
print(target_file)

subprocess.Popen(['C:\\Program Files\\7-Zip\\7z.exe','a','-mx5' ,'-r0',PASSWORD,result_zip_file ,target_file])

# 7z a  -mx5 -r0 -pPas1 C:\Users\Public\113\test.7z C:\Users\Public\112