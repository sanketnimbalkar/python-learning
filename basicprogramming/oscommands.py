"""Running OS Commands¶
Let us understand how to run OS commands using Python using libraries such as os and subprocess.
Python provides several libraries which can be used to run OS commands. os and subprocess are most popular ones.
We can import the libraries such as os and subprocess to start using them.
There are bunch of commands to create directories, change ownership, change permission, run general system commands etc.
os library is extensively used to read environment variables at run time of the application.
It is used to pass keys and credentials to work with databases, external applications etc.
Typically keys and credentials should not be part of the source code.
subprocess can be used to run the commands and also to process the output."""

import os
import subprocess

print(os.getcwd())  # Get current working directory.

# Read environment variables
print(os.environ.get('PATH'))

print(os.environ.get('USER'))

print(os.environ.get('HOME'))

# Run ls -ltr command to get list of files in the current directory.

output = subprocess.check_call(['ls', '-ltr'])

print(output)
