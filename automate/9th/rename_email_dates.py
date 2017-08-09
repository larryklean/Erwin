#! python3
# Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import shutil
import os
import re

# reate a regex that matches files with the American date format
date_regex = re.compile("""^(.*?)
    ([01]?\d)-
    ([0123]?\d)-
    ((19|20)?\d\d)
    (.*?)$
    """, re.VERBOSE)

# loop over the files in the working directory
for current_file_name in os.listdir('.'):
    mo = date_regex.search(current_file_name)
    if mo is None:
        continue
    befor_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(3)
    year_part = mo.group(4)
    after_part = mo.group(5)
    # get absolute path
    abs_path = os.getcwd()
    # form european-style filename
    euro_file_name = befor_part + day_part + '-' + month_part + '-' + year_part + after_part
    # concat file name
    euro_file_name = os.path.join(abs_path, euro_file_name)
    amer_file_name = os.path.join(abs_path, current_file_name)
    # rename
    print('Renaming "%s" to "%s"...' % (amer_file_name, euro_file_name))
    shutil.move(amer_file_name, euro_file_name)
