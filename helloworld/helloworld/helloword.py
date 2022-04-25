#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from turtle import clear
from mytime_pkg import epoch_time
from myprint_pkg import pretty_time

# The module epoch_time is in the file epoch_time.py in the directory ./mytime_pkg
# The module pretty_time is in the file pretty_time.py in the directory ./myprint_pkg
# helloworld.py this file is run in ./

def main():
    print("Hello world\n")
    print("Today is: ", pretty_time.dtToPrettyTime(datetime.now()))
    print("Seconds since epoch is: ", epoch_time.dtSinceEpoch(datetime.now()))

if __name__ == "__main__":
    main()