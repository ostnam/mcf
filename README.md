# mCF
mCF is a library of common financial functions written entirely in python3.

## Functions
### discount\_cf(cashflow, discount\_rate)
Returns the NPV of the cash flows.

I recommend the use a list of floats representing the consecutive cashflows as the "cashflow" argument. 

The first cashflow is considered as occurring "right now", and thus not discounted. 

### WACC_calculator(return_on_debt, return_on_equity, debt_market_value, equity_market_value, corporate_tax_rate)
Returns an after-tax WACC.

The rates should be in the 0.\* format.

### equivalent\_annual\_cashflow(cashflow, discount\_rate)
Returns the equivalent annual cashflow/cost of a list of cashflows.

Just like discount\_cf(),  I recommend using a list of floats representing the consecutive cashflows as the "cashflow" argument.

The first cash flow is considered as occurring "right now" and thus isn't discounted.
