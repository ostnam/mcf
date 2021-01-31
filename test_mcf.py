import unittest
import mcf

class TestCashflows(unittest.TestCase):
    test_flow = mcf.Cashflows(10, 10)
    negative_test_flow = mcf.Cashflows(-10, -10)
    null_single_flow = mcf.Cashflows(0)
    null_multiple_flow = mcf.Cashflows(0, 0)
    mixed_sign_flow = mcf.Cashflows(-10, 10)
    mixed_value_flow = mcf.Cashflows(10, 0, -10)
    added_test_flow = test_flow + test_flow
    added_test_flow2 = test_flow + mcf.Cashflows(10) 


    def test_init(self):
        self.assertEqual(self.test_flow.cashflows, (10, 10),
                "Error initializing positive cash flows")
        self.assertEqual(self.negative_test_flow.cashflows, (-10, -10),
                "Error initializing negative cash flows")
        self.assertEqual(self.mixed_value_flow.cashflows, (10, 0, -10),
                "Error initializing mixed value cash flow")
        self.assertEqual(self.negative_test_flow.cashflows, (-10, -10),
                "Error initializing negative cash flows")
        self.assertEqual(self.null_single_flow.cashflows, (0,),
                "Error initializing single null cash flow")

    def test_add(self):
        self.assertEqual(self.added_test_flow.cashflows, (20, 20),
                "Error adding up two positive cashflows")
        self.assertEqual(self.added_test_flow2.cashflows, (20, 10),
                "Error adding up two positive cashflows of differing length")

    def test_discount(self):
        self.assertEqual(self.test_flow.discount(0.1), 19.09090909090909,
                "Incorrect value discounting positive cashflows with positive discount rate")
        self.assertEqual(self.test_flow.discount(0.0), 20,
                "Incorrect value discounting positive cashflows with 0% discount rate")
        self.assertEqual(self.test_flow.discount(-0.1), 21.11111111111111,
                "Incorrect value discounting positive cashflows with negative discount rate")

        self.assertEqual(self.negative_test_flow.discount(0.1), -19.09090909090909,
                "Incorrect value discounting negative cashflows with positive discount rate")
        self.assertEqual(self.negative_test_flow.discount(0.0), -20,
                "Incorrect value discounting negative cashflows with 0% discount rate")
        self.assertEqual(self.negative_test_flow.discount(-0.1), -21.11111111111111,
                "Incorrect value discounting negative cashflows with negative discount rate")

        self.assertEqual(self.null_single_flow.discount(0.1), 0,
                "Incorrect value discounting single null flow with positive discount rate")
        self.assertEqual(self.null_single_flow.discount(0.0), 0,
                "Incorrect value discounting single null flow with 0% discount rate")
        self.assertEqual(self.null_single_flow.discount(-0.1), 0,
                "Incorrect value discounting single null flow with negative discount rate")

        self.assertEqual(self.mixed_sign_flow.discount(0.1), -0.9090909090909101,
                "Incorrect value discounting mixed sign flows with positive discount rate")
        self.assertEqual(self.mixed_sign_flow.discount(0.0), 0,
                "Incorrect value discounting mixed sign flows with 0% discount rate")
        self.assertEqual(self.mixed_sign_flow.discount(-0.1), 1.1111111111111107,
                "Incorrect value discounting mixed sign flows with negative discount rate")

        self.assertEqual(self.mixed_value_flow.discount(0.1), 1.7355371900826455,
                "Incorrect value discounting mixed value flows with positive discount rate")
        self.assertEqual(self.mixed_value_flow.discount(0.0), 0,
                "Incorrect value discounting mixed value flows with 0% discount rate")
        self.assertEqual(self.mixed_value_flow.discount(-0.1), -2.3456790123456788,
                "Incorrect value discounting mixed value flows with negative discount rate")

    def test_eac(self):
        self.assertEqual(self.test_flow.eac(0.1), 20.999999999999993, "Should be 20.999999999999993")

    def test_pv(self):
        self.assertEqual(self.test_flow.pv(0, 0.1), 10.0, "Should be 10.0")
        self.assertEqual(self.test_flow.pv(1, 0.1), 9.09090909090909, "Should be 9.09090909090909")

    def test_WACC_calculator(self):
        self.assertEqual(mcf.WACC_calculator(0.08, 0.16, 600, 400, 0.1), 0.1072, "Should be 0.1072")

if __name__ == "__main__":
    unittest.main()
