"""
This document includes all the european payoffs for both call and put options
"""

def payoff_call(St, X):
    """
    Call option payoff
    """
    return (St - X + abs(St - X)) / 2

def call_buyer_profit(St, X, c = 0):
    """
    Call buyer profit
    """
    payoff = payoff_call(St, X)
    return payoff - c

def call_seller_profit(St, X, c = 0):
    """
    Call seller profit
    """
    payoff = payoff_call(St, X)
    return c - payoff

def payoff_put(St, X):
    """
    Put option payoff
    """
    return (abs(X - St) + X - St) / 2

def put_buyer_profit(St, X, p = 0):
    """
    Put buyer profit
    """
    put_payoff = payoff_put(St, X)
    return put_payoff - p

def put_seller_profit(St, X, p):
    """
    Put seller profit
    """
    put_payoff = payoff_put(St, X)
    return p - put_payoff