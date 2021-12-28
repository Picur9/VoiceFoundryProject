import unittest
import twl
import vanity_advance

class TestVanityPhone(unittest.TestCase):
    def test_twl(self):
        self.assertEqual(twl.check("word"), True)
        self.assertEqual(twl.check("ntaword"), False)

    def test_vanity(self):
        self.assertEqual(vanity.generate("+46244"), ['4-magi', 'inch-4', 'I-magi', 'inch-I', 'go-ahi'])
        self.assertEqual(vanity.generate("46244"), ['4-magi', 'inch-4', 'I-magi', 'inch-I', 'go-ahi'])
        self.assertEqual(vanity.generate("+6086657"), ['+60-tools', '+608-mols', '+60-took-R', '+60-tool-R', '+60-U-mols'])
        self.assertEqual(vanity.generate("+13569377"), ['+1-flowers', '+1-flower-R', '+1-3-lowers', '+1-flower-7', '+1-el-oyers'])
        self.assertEqual(vanity.generate("+120605"), [])

if __name__ == '__main__':
    unittest.main()
