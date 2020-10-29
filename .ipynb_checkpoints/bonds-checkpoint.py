import scipy.optimize as optimize

def bond_price(par, T, y, cpn, freq = 2):
    """
    Getting the bond price from:
    par: par value of the bond
    T: time to maturity for the bond
    y = yield to maturity of the bond
    cpn = coupon of the bond
    freq = frequency of coupon payment, by default it is semi-annual (2)
    """
    freq = float (freq)
    n = T * float (freq) #Number of periods
    coupon = cpn / 100 * par / freq
    dt = [(i + 1) / freq for i in range(int(n))]
    price = sum([coupon/(1 + y / freq) ** (freq * t) for t in dt]) + par / (1 + y / freq) ** (n)
    return price

def bond_ytm(price, par, T, cpn, freq = 2, guess = 0.5):
    """
    For this we leverage the bond_price function:
    price: price of the bond
    par: par value of the bond
    T: time to maturity for the bond
    y: yield to maturity of the bond
    cpn: coupon of the bond
    freq: frequency of coupon payment
    guess: guess
    """
    p_func = lambda y: bond_price(par, T, y, cpn, freq = 2) - price
    return optimize.newton(p_func, guess)
    
def dirty_price(d, year_days, par, T, y, cpn, freq=2):
    """
    Calculates the dirty price. First calculate the accrued interest.
    d: number of days since the last payment
    year_days: based on convention
    """
    coupon = cpn / 100 * par / freq #calculates the period coupon
    accrued_interest = (d / year_days) * coupon
    price = bond_price(par, T, y, cpn, freq)
    dirty_price = price + accrued_interest
    return dirty_price

def key_rate_dur(y, par, T, cpn, freq, dy = 0.01):
    y_min = y - dy
    y_max = y + dy
    price = bond_price(par, T, y, cpn, freq)
    price_min = bond_price(par, T, y_min, cpn, freq)
    price_max = bond_price(par, T, y_max, cpn, freq)
    
    krd = (price_min - price_max) / (2 * price * dy)
    return krd
    