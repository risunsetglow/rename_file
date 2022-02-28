import os
from glob import glob
import datetime

# テキストファイル取得
current_dir = os.getcwd()
path_list = glob(os.path.join(current_dir, "*.txt"))

#ファイル名に現在の日付を加える
today = datetime.datetime.now()
formated_today = today.strftime('%Y%m%d')
for path in path_list:
  dirname, file_and_txt = os.path.split(path)
  file, exe = os.path.splitext(file_and_txt)
  new_file_name = file + "_" + formated_today +  exe
  os.rename(path, os.path.join(dirname, new_file_name)) 

# 元のファイル名に戻す
# for path in path_list:
#   dirname, file_and_txt = os.path.split(path)
#   file, exe = os.path.splitext(file_and_txt)
#   file_split = file.split('_')
#   new_file_name = file_split[0] + exe
#   os.rename(path, os.path.join(dirname, new_file_name)) 