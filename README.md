# mCF
mCF is a library of common financial functions that I wrote in python3 for myself.

## CashFlows class
You can create a new cashflow instance with mcf.CashFlows().

    In[1]: import mcf
    In[2]: x = [10, 10]
    In[3]: y = mcf.CashFlows(x)
    In[4]: y.cashflows
    Out[4]: [10, 10]

I recommend using a list of integers or floats as input.
The first cashflow is considered as occurring "right now", and thus not discounted. 
### CashFlows methods
#### CashFlows.discount(discount_rate)
Returns the NPV of the cashflows at the specified discount rate. The discount rate should be in the format 0.10 for 10%.

    In[5]: y.discount(0.1)
    Out[5]: 19.09090909090909

#### CashFlows.eac(discount_rate)
Returns the equivalent annual cost of the cashflows at the specified discount rate.

    In[6]: y.eac(0.1)
    Out[6]: 20.999999999999993

#### CashFlows.pv(n, discount_rate)
Returns the present value of the n+1^th cash flow at the specified discount rate.

    In[7]: y.pv(0, 0.1)
    Out[7]: 10.0
    In[8]: y.pv(1, 0.1)  
    Out[8]: 9.09090909090909  

## Other functions
### WACC_calculator(return_on_debt, return_on_equity, debt_market_value, equity_market_value, corporate_tax_rate)
Returns an after-tax WACC.

The rates should be in the 0.\* format.