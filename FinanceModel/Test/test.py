import json
import numpy
import nltk
import sys
from Util import calculator
import sqlite3 as lite



str = "I'm good"

def hh():
    global str
    str = "Hello"

def gg():
    print str

hh()
gg() 