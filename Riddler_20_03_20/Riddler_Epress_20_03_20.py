"""
Riddler Express
A manager is trying to produce sales of his company’s widget, so he instructs his team to hold a sale every morning,
lowering the price of the widget by 10 percent. However, he gives very specific instructions as to what should happen
in the afternoon: Increase the price by 10 percent from the sale price, with the (incorrect) idea that it would
return it to the original price. The team follows his instructions quite literally, lowering and then raising the
price by 10 percent every day.

After N days, the manager walks through the store in the evening, horrified to see that the widgets are marked more
than 50 percent off of their original price. What is the smallest possible value of N?
"""

"""
Answer: One day has a discount to (0.9)(1.1) = 0.99 of original value.
        We thus look for N such that .99^N < 0.5.
        Exact solution is N > Log(0.5)/log(0.99)
"""
from math import log

if __name__ == "__main__":
    print(log(0.5) / log(0.99))
