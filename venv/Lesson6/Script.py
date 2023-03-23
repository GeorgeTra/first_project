from sys import argv
import random

import random as rnd
21
START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]
# print(rnd.random())
rnd.seed(42)
state = rnd.getstate()
# print(rnd.random())
# rnd.setstate(state)
# print(rnd.random())
# print(rnd.randint(START, STOP))
# print(rnd.uniform(START, STOP))
# print(rnd.choice(data))
# print(rnd.randrange(START, STOP, STEP))
# print(data)
# rnd.shuffle(data)
# print(data)
# print(rnd.sample(data, 2))
# print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))

# print(random.uniform(int(argv[1]), int(argv[2])))
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))
