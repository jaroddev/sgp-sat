# Project SGP: SAT part

## Installation steps

 - setup a venv and activate the source 
 - install wheels and setuptools
 - update pip
 - install the requirements via the (pysat, etc...)

## How to use it

### use the CLI

An example: 
` python3 run.py -g 4 -s 2 -w 2`

### Test runner (simple script)

Follow the steps:
 - Create the bench folder.
 `mkdir bench`
 
 - Run the script in the project's root directory.
 `python3 client.py`

 - You can run this command to find which configuration are UNSAT.
 `grep -rni "UNSAT" bench/*.out`

  - You can look at the csv files to watch the times for each g-p tuples.

## Aknowledgment

The custom_timeout.py file was taken from this location:
 - https://github.com/pnpnpn/timeout-decorator

They also aknowledge that it was derived from another place:
 - http://www.saltycrane.com/blog/2010/04/using-python-timeout-decorator-uploading-s3/ and https://code.google.com/p/verse-quiz/source/browse/trunk/timeout.py