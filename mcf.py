class Cashflows:
    def __init__(self, *cashflows):
        self.cashflows = cashflows

    def __add__(self, other):
        """Returns a new instance with the value of their cashflows for each period added together""" 
        length = max(len(self.cashflows), len(other.cashflows))
        result = []
        for i in range(length):
            sum = 0
            for j in (self, other):
                try:
                    sum += j.cashflows[i]
                except:
                    pass
            result.append(sum)
        return Cashflows(*result)

    def discount(self, discount_rate):
        """Calculates the NPV of a list of cashflows, with a single discount rate. It is assumed that the first cashflow occurs immediately and thus isn't discounted. The discount rate must be in the format 0.1 for 10%."""
        npv = 0.0
        cashflow = self.cashflows
        try:
            for i in range(0, len(cashflow)):
                current_flow = cashflow[i]
                npv += (current_flow / ((discount_rate + 1) ** i))
        except:
            print("\n Something went wrong while discounting the cash flows. Your cashflow format might be incorrect, I recommend using a list of floats.")
        return npv

    def eac(self, discount_rate):
        """Returns the EAC of the cashflows at the specified discount rate. Discount rate must be in the format 0.1 for 10%."""
        NPV = self.discount(discount_rate)
        project_duration = len(self.cashflows) - 1
        annuity = (1-(1/((1+discount_rate) ** project_duration))) / (discount_rate)
        EACvalue = NPV/annuity
        return EACvalue

    def pv(self, n, discount_rate):
        """Returns the present value of the cashflow i"""
        present_value = (self.cashflows[n] / ((discount_rate + 1) ** n))
        return present_value


def WACC_calculator(return_on_debt, return_on_equity, debt_market_value, equity_market_value, corporate_tax_rate):
    """Returns an after-tax WACC. Percents must be in the format 0.1 for 10%"""
    total_capital_value = equity_market_value + debt_market_value
    WACC = (return_on_debt * (1 - corporate_tax_rate)*(debt_market_value/total_capital_value) + (return_on_equity * (equity_market_value/total_capital_value)))
    return WACC 

