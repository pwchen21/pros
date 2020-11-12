#! /usr/local/bin/python3

"""1. 跟DB確認帳號密碼"""
"""2. 確認OK，近入記帳頁面"""
"""3. 確認失敗，回傳失敗網頁"""

import glob
import yate

data_files = glob.glob("data/*.txt")

print(yate.start_response())
print(yate.include_header("test"))
print(yate.include_footer({"Home": "/index.html"}))
