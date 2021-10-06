import unittest
from validate import validateUP

class Validtest(unittest.Testcase):
    def testval1(self):
        self.assertEqual(validateUP('Shashank', 'Sha@1999'), True)

    def testval2(self):
        self.assertEqual(validateUP('S', 'Sha@1999'), False)

    def testval3(self):
        self.assertEqual(validateUP('Sha', 'Sha5'), False)

    def testval4(self):
        self.assertEqual(validateUP('Sha6','S'), False)

    def testval5(self):
        self.assertEqual(validateUP(9809,'Sha@1999'), False)

    def testval6(self):
        self.assertEqual(validateUP('Shashank', 6899), False)

    def setUp(self):
            print("setup")

    def teardown(self):
            print("Teardown")

    @classmethod
    def setUpClass(self)-> print("setup class"):
        pass