try:
    import numpy.random as random
except ImportError:
    import random


    class Roller:
        def __init__(self, seed=None):
            self._generator = random.Random(seed) if seed else random

        def get(self, next_buffer_size):
            return self._generator.uniform(0,1)

        def shuffle(self, seq):
            return self._generator.shuffle(seq)
else:
    class Roller:
        def __init__(self, seed=None):
            self._buffer = ()
            self._next_ind = 0
            self._generator = random.RandomState(seed) if seed else random

        def get(self, next_buffer_size):
            if self._next_ind == len(self._buffer):
                self._buffer = self._generator.uniform(size=next_buffer_size)
                self._next_ind = 0
            ret = self._buffer[self._next_ind]
            self._next_ind += 1
            return ret

        def shuffle(self, seq):
            return self._generator.shuffle(seq)