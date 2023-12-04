import os
import time
import sys
import shutil
import getpass
from os import path
username = getpass.getuser()
tempdir = "C:/temp"
extract_dir = "C:/temp/sfx"
isdirchkzip = os.path.isdir(extract_dir)
istempdirchk = os.path.isdir(tempdir)
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_zip = os.path.abspath(os.path.join(bundle_dir, 'testuser.zip'))
if isdirchkzip == True:
   time.sleep(2.4)
   shutil.rmtree(extract_dir)
   time.sleep(2.4)
if istempdirchk == True:
   time.sleep(1.5)
   shutil.rmtree(tempdir)
   time.sleep(2.4)
os.mkdir(tempdir)
time.sleep(2.4)
os.mkdir(extract_dir)
time.sleep(2.4)
shutil.unpack_archive(path_to_zip, extract_dir)
time.sleep(1.5)
os.chdir(extract_dir)
time.sleep(2.4)
# Run after Extract

