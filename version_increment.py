#  
#  version_increment.py - Simple versioning script for Platformio
#  
#  Copyright (C) 2020  Davide Perini
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy of 
#  this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
#  copies of the Software, and to permit persons to whom the Software is 
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in 
#  all copies or substantial portions of the Software.
#  
#  You should have received a copy of the MIT License along with this program.  
#  If not, see <https://opensource.org/licenses/MIT/>.
#  

import sys
import datetime

## DO NOT EDIT THIS FILE, edit version file if you want to start from a different version
BUILD_NUMBER = 'version'
VERSION_FILE = 'include/Version.h'
version = '0.1.'

## Increment version during the upload stage only
upload = False
n = len(sys.argv) 

for i in range(1, n): 
    if sys.argv[i] == "upload":
        upload = True; 

if upload:
    
    print("Version Increment Scritp ARGS=")
    print (sys.argv[1:])    

    build_no = 0

    try:
        with open(BUILD_NUMBER) as f:
            build_no = f.readline()
            version = build_no[0:build_no.rindex('.')+1]
            build_no = int(build_no[build_no.rindex('.')+1:]) + 1 
    except:
        print('No version file found or incorrect data in it. Starting from 0.1.0')
        build_no = 1
    with open(BUILD_NUMBER, 'w+') as f:
        f.write(version + str(build_no))
        print('Build number: {}'.format(version + str(build_no)))

    hf = """
    // AUTO GENERATED FILE FROM version_increment.py, DO NOT EDIT THIS FILE
    #ifndef VERSION
      #define VERSION "{}"
    #endif
    #ifndef BUILD_TIMESTAMP
      #define BUILD_TIMESTAMP "{}"
    #endif
    """.format(version + str(build_no), datetime.datetime.now(), version+str(build_no))
    with open(VERSION_FILE, 'w+') as f:
        f.write(hf)
else:  
    print("Version Increment Script. Nothing to do. ARGS=")
    print (sys.argv[1:])