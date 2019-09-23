from unittest import TestCase

from randombag import RandomBag


class RandomBagTests(TestCase):
    def make2(self):
        seed = range(100)
        return RandomBag(seed, seed=0), set(seed)

    def test_simple(self):
        rb, control = self.make2()
        self.assertCountEqual(rb, control)
        for i in range(25):
            rb.remove(i)
            control.remove(i)
            self.assertCountEqual(rb, control)

        for i in range(200, 300):
            rb.add(i)
            control.add(i)
            self.assertCountEqual(rb, control)

        for _ in range(25):
            control.remove(
                rb.pop()
            )
            self.assertCountEqual(rb, control)

    def test_reproducability(self):
        rb1 = RandomBag(range(25), seed=0)
        rb2 = RandomBag(rb1)

        for i in range(100):
            rb1.add(i)
            rb2.add(i)

        self.assertSequenceEqual(rb1, rb2)

        self.assertEqual(rb1.popn(3), rb2.popn(3))

        self.assertEqual(rb1.popn(5)+rb1.popn(5), rb2.popn(10))

    def test_non_reproducability(self):
        rb1 = RandomBag(range(25), seed=0)
        rb2 = RandomBag(rb1, seed=False)

        self.assertNotEqual(list(rb1), list(rb2))

    def test_empty(self):
        rb, control = self.make2()
        while rb:
            control.remove(rb.pop())
            self.assertCountEqual(rb, control)
        self.assertCountEqual(rb, set())