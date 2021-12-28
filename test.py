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
        self.assertEqual(vanity_advance.generate("+46244"), ['4-magi', 'inch-4', 'I-magi', 'inch-I', 'go-ahi'])
        self.assertEqual(vanity_advance.generate("46244"), ['4-magi', 'inch-4', 'I-magi', 'inch-I', 'go-ahi'])
        self.assertEqual(vanity_advance.generate("+6086657"), ['+60-tools', '+608-mols', '+60-took-R', '+60-tool-R', '+60-U-mols'])
        self.assertEqual(vanity_advacne.generate("+13569377"), ['+1-flowers', '+1-flower-R', '+1-3-lowers', '+1-flower-7', '+1-el-oyers'])
        self.assertEqual(vanity_advance.generate("+120605"), [])
                
if __name__ == '__main__':
    unittest.main()
