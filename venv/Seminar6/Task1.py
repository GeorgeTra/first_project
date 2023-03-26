# 1. Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в
# модуль функции под псевдонимами. (3-7 строк импорта).

import numpy as np
import sys as s
import random as rnd
import requests as req
from Task2 import guess

if guess(1, 3, 3):
    print("Win!")