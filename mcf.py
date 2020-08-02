def discount_cf(cashflow, discount_rate):
    """Calculates the NPV of a list of cashflows, with a single discount rate. It is assumed that the first cashflow occurs immediately and thus isn't discounted."""
    npv = 0.0
    dr_format_error = "\n Check the format of your discount rate. I recommend this format: 1.1"
    if type(discount_rate) == str:
            if "%" in discount_rate:
                try:
                    adjusted_discount_rate = float(discount_rate.replace("%", ""))
                except:
                    dr_format_error
            else:
                try:
                    adjusted_discount_rate = float(discount_rate)
                except:
                    dr_format_error
    else:
        adjusted_discount_rate = discount_rate
    if adjusted_discount_rate < 1.0:
        adjusted_discount_rate = adjusted_discount_rate + 1
    try:
        for i in range(0, len(cashflow)):
            current_flow = cashflow[i]
            npv = npv + (current_flow / (adjusted_discount_rate) ** i)
    except:
        "\n Something went wrong while discounting the cash flows. Your cashflow format might be incorrect, I recommend using a list of floats."
    return(npv)


def WACC_calculator(ReturnOnDebt, ReturnOnEquity, DebtMarketValue, EquityMarketValue, CorporateTaxRate):
    