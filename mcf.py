def discount_cf(cashflow, discount_rate):
    """Calculates the NPV of a list of cashflows, with a single discount rate. It is assumed that the first cashflow occurs immediately and thus isn't discounted. The discount rate must be in the format 0.1 for 10%."""
    npv = 0.0
    try:
        for i in range(0, len(cashflow)):
            current_flow = cashflow[i]
            npv = npv + (current_flow / (discount_rate + 1) ** i)
    except:
        "\n Something went wrong while discounting the cash flows. Your cashflow format might be incorrect, I recommend using a list of floats."
    return npv


def WACC_calculator(return_on_debt, return_on_equity, debt_market_value, equity_market_value, corporate_tax_rate):
    """Returns an after-tax WACC. Percents must be in the format 0.1 for 10%"""
    total_capital_value = equity_market_value + debt_market_value
    WACC = (return_on_debt * (1 - corporate_tax_rate)*(debt_market_value/total_capital_value) + (return_on_equity * (equity_market_value/total_capital_value)))
    return WACC 

def equivalent_annual_cashflow(cashflow, discount_rate):
    """Returns the EAC of a list of cashflows. Discount rate must be in the format 0.1 for 10%."""
    NPV = discount_cf(cashflow, discount_rate)
    project_duration = len(cashflow) - 1
    annuity = (1-(1/((1+discount_rate) ** project_duration))) / (discount_rate)
    EAC = NPV/annuity
    return EAC
