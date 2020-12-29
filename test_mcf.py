import unittest
import mcf

class TestCashflows(unittest.TestCase):
    test_flow = mcf.Cashflows(10, 10)
    def test_init(self):
        self.assertEqual(self.test_flow.cashflows, (10, 10), "Should be (100, 150)")

    def test_discount(self):
        self.assertEqual(self.test_flow.discount(0.1), 19.09090909090909, "Should be 19.09090909090909")

    def test_eac(self):
        self.assertEqual(self.test_flow.eac(0.1), 20.999999999999993, "Should be 20.999999999999993")

    def test_pv(self):
        self.assertEqual(self.test_flow.pv(0, 0.1), 10.0, "Should be 10.0")
        self.assertEqual(self.test_flow.pv(1, 0.1), 9.09090909090909, "Should be 9.09090909090909")

    def test_WACC_calculator(self):
        self.assertEqual(mcf.WACC_calculator(0.08, 0.16, 600, 400, 0.1), 0.1072, "Should be 0.1072")

if __name__ == "__main__":
    unittest.main()
