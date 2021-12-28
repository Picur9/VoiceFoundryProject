import unittest
import twl
import vanity
import vanity_advance

class TestVanityPhone(unittest.TestCase):
    def test_twl(self):
        self.assertEqual(twl.check("word"), True)
        self.assertEqual(twl.check("ntaword"), False)

    def test_vanity(self):
        self.assertEqual(vanity.generate("+46244"), ['4magi', 'go2hi', 'hm2hi', 'ho2hi', 'in2hi'])
        self.assertEqual(vanity.generate("46244"), ['4magi', 'go2hi', 'hm2hi', 'ho2hi', 'in2hi'])
        self.assertEqual(vanity.generate("+6086657"), ['60tools', '608mols', '60took7', '60tool7', '608mol7'])
        self.assertEqual(vanity.generate("+13569377"), ['1flowers', '13lowers', '1el6yeps', '1el6zeps', '1elm9err'])

     def test_vanity_advance(self):
        self.assertEqual(vanity.generate("+46244"), ['4magi', 'go2hi', 'hm2hi', 'ho2hi', 'in2hi'])
        self.assertEqual(vanity.generate("46244"), ['4magi', 'go2hi', 'hm2hi', 'ho2hi', 'in2hi'])
        self.assertEqual(vanity.generate("+6086657"), ['60tools', '608mols', '60took7', '60tool7', '608mol7'])
        self.assertEqual(vanity.generate("+13569377"), ['1flowers', '13lowers', '1el6yeps', '1el6zeps', '1elm9err'])
        
        
if __name__ == '__main__':
    unittest.main()
