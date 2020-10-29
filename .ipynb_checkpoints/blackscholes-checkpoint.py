from scipy import stats
import numpy as np

def bs_call(S, X, T, r, sigma):
    """
    S = initial stock price
    X = strike price of call
    T = time to maturity
    r = risk free rate
    sigma = volatility
    """
    d1 = ( np.log(S/X) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * stats.norm.cdf(d1) - X * np.exp(-r * T)*stats.norm.cdf(d2)

def bs_put(S, X, T, r, sigma):
    """
    S = initial stock price
    X = strike price of put
    T = time to maturity
    r = risk free rate
    sigma = volatility
    """
    d1 = ( np.log(S/X) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return X * np.exp(-r*T)*stats.norm.cdf(-d2) - S * stats.norm.cdf(-d1)

def binomial_grid(n):
    """
    The following code was included within the documentation, however it is only good for visualizing a binomial set up for a call/put price, and not anything further. 
    """
    G = nx.Graph()
    for i in range(0, n+1):
        for j in range(1, i+2):
            if i<n:
                G.add_edge((i, j), (i+1, j))
                G.add_edge((i, j), (i+1, j+1))
    posG = {}
    for node in G.nodes():
        posG[node] = (node[0], n+2+node[0] - 2 * node[1])
    nx.draw(G, pos = posG)
    
def delta_call(S, X, T, r, sigma):
    """
    Calculates the delta of a BS-European-Call option
    """
    d1 = ( np.log(S/X) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    return stats.norm.cdf(d1)

def delta_put(S, X, T, r, sigma):
    """
    Calculates the delta of a BS-European-Put option
    """
    d1 = ( np.log(S/X) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    return (-stats.norm.cdf(-d1))

def binomial_call(S, X, r, T, sigma, n = 100):
    dT = T / n
    u = np.exp(sigma * np.sqrt(dT))
    d = 1.0 / u
    a = np.exp(r * dT)
    p = (a - d) / (u - d)
    v = [[0.0 for j in range(i+1)] for i in range(n+1)]
    for j in range(i + 1):
        v[n][j] = max(s * u**j * d**(n - j) - x, 0.0)
    for i in range(n-1, -1, -1):
        for j in range(i + 1):
            v[i][j]=exp(-r*deltaT)*(p*v[i+1][j+1]+(1.0-p)*v[i+1][j])
    return v[0][0]