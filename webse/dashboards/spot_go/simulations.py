import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

def quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, cases):
    """
    This function calculates the dispatch in the spot and GO markets for supplier
    1 and 2. It is assumed that the transmission line is always congested in the
    spot market, while the quantities in the GO market depend on whether or not
    the transmission line is taken into account in the GO market. 
    
    Note that the first number in the quantity variables refers to the branch in 
    the spot market, the second number refers to the branch in the GO market, 
    while the last number refers to the supplier.

    Parameters
    ----------
    a1 : float
        Demand in spot market in node 1 (high-demand node).
    a2 : float
        Demand in spot market in node 2 (low-demand node).
    a1_go : float
        Demand in GO market in node 1 (high-demand node).
    a2_go : float
        Demand in GO market in node 2 (low-demand node).
    T : float
        Capacity of transmission line.
    alpha1 : float
        Share of production capacity of supplier 1 that qualifies for GOs.
    alpha2 : float
        Share of production capacity of supplier 2 that qualifies for GOs.
    restriction : bool
        True if there is transmission line restriction in GO market, False otherwise.

    Returns
    -------
    q11 : float
        Quantity of supplier 1 in branch 1 spot.
    q12 : float
        Quantity of supplier 2 in branch 1 spot.
    q1go11 : float
        Quantity of supplier 1 in branch 1 spot and branch 1 go.
    q1go12 : float
        Quantity of supplier 2 in branch 1 spot and branch 1 go.
    q1go21 : float
        Quantity of supplier 1 in branch 1 spot and branch 2 go.
    q1go22 : float
        Quantity of supplier 2 in branch 1 spot and branch 2 go.
    q21 : float
        Quantity of supplier 1 in branch 2 spot.
    q22 : float
        Quantity of supplier 2 in branch 2 spot.
    q2go11 : float
        Quantity of supplier 1 in branch 2 spot and branch 1 go.
    q2go12 : float
        Quantity of supplier 2 in branch 2 spot and branch 1 go.
    q2go21 : float
        Quantity of supplier 1 in branch 2 spot and branch 2 go.
    q2go22 : float
        Quantity of supplier 2 in branch 2 spot and branch 2 go.

    """
    # Branch 1 spot
    q11 = ah + T
    q12 = al - T
    # Branch 2 spot
    q21 = ah - T
    q22 = al + T
    if cases == 'case1':
        # Banch 1 spot, branch 1 go1
        q1go11 = min(al_go + ah_go, alpha1*q11)
        q1go12 = max(0, al_go + ah_go - (alpha1*q11))
        # Banch 1 spot, branch 2 go1
        q1go21 = max(0, al_go + ah_go - (alpha2*q12))
        q1go22 = min(al_go + ah_go, alpha2*q12)
        # Banch 2 spot, branch 1 go2
        q2go11 = min(al_go + ah_go, alpha1*q21)
        q2go12 = max(0, al_go + ah_go - (alpha1*q21))
        # Banch 2 spot, branch 2 go2
        q2go21 = max(0, al_go + ah_go - (alpha2*q22))
        q2go22 = min(al_go + ah_go, alpha2*q22)
    elif cases == 'case2':
        # Banch 1 spot, branch 1 go1
        q1go11 = min(al_go + ah_go, ah_go + T, alpha1*q11)
        q1go12 = max(0, al_go - T, al_go + ah_go - (alpha1*q11))
        # Banch 1 spot, branch 2 go1
        q1go21 = max(0, ah_go - T, al_go + ah_go - (alpha2*q12))
        q1go22 = min(al_go + ah_go, al_go + T, alpha2*q12)

        # Banch 2 spot, branch 1 go2
        q2go11 = min(al_go + ah_go, ah_go + T, alpha1*q21)
        q2go12 = max(0, al_go - T, al_go + ah_go - (alpha1*q21))
        # Banch 2 spot, branch 2 go2
        q2go21 = max(0, ah_go - T, al_go + ah_go - (alpha2*q22))
        q2go22 = min(al_go + ah_go, al_go + T, alpha2*q22)
    # else:

    return q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22

def bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch):
    """
    This function calculates the lower bounds of the price support for the two
    suppliers in each branch of the spot market. See lemma 2 in the paper.
    
    Note that the first number in the quantity variables refers to the branch in 
    the spot market, the second number refers to the branch in the GO market, 
    while the last number refers to the supplier.

    Parameters
    ----------
    q1go11 : float
        Quantity of supplier 1 in branch 1 spot and branch 1 go.
    q1go12 : float
        Quantity of supplier 2 in branch 1 spot and branch 1 go.
    q1go21 : float
        Quantity of supplier 1 in branch 1 spot and branch 2 go.
    q1go22 : float
        Quantity of supplier 2 in branch 1 spot and branch 2 go.
    q2go11 : float
        Quantity of supplier 1 in branch 2 spot and branch 1 go.
    q2go12 : float
        Quantity of supplier 2 in branch 2 spot and branch 1 go.
    q2go21 : float
        Quantity of supplier 1 in branch 2 spot and branch 2 go.
    q2go22 : float
        Quantity of supplier 2 in branch 2 spot and branch 2 go.
    pmaxgo : float
        Price cap in GO market.
    branch : int
        Branch 1 in spot market if 1, branch 2 otherwise.

    Returns
    -------
    b1 : float
        Lower bound of price support for supplier 1 in GO market.
    b2 : float
        Lower bound of price support for supplier 2 in GO market.
    b : float
        Lower bound of price support in GO market.

    """
    # Branch 1: p1s<=p2s:
    if branch == 1:
        b1 = pmaxgo * q1go21 / q1go11
        b2 = pmaxgo * q1go12 / q1go22
        b = max(b1, b2)
    # Branch 2: p1s>p2s:
    else:
        b1 = pmaxgo * q2go21 / q2go11
        b2 = pmaxgo * q2go12 / q2go22
        b = max(b1, b2)

    return b1, b2, b

def CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, bgo, pmaxgo, branch):
    """
    This function calculates the cumulative distribution functions for both
    suppliers in both branches of the spot market. See proposition 1 in the paper.

    Note that the first number in the quantity variables refers to the branch in 
    the spot market, the second number refers to the branch in the GO market, 
    while the last number refers to the supplier.
 
    Parameters
    ----------
    q1go11 : float
        Quantity of supplier 1 in branch 1 spot and branch 1 go.
    q1go12 : float
        Quantity of supplier 2 in branch 1 spot and branch 1 go.
    q1go21 : float
        Quantity of supplier 1 in branch 1 spot and branch 2 go.
    q1go22 : float
        Quantity of supplier 2 in branch 1 spot and branch 2 go.
    q2go11 : float
        Quantity of supplier 1 in branch 2 spot and branch 1 go.
    q2go12 : float
        Quantity of supplier 2 in branch 2 spot and branch 1 go.
    q2go21 : float
        Quantity of supplier 1 in branch 2 spot and branch 2 go.
    q2go22 : float
        Quantity of supplier 2 in branch 2 spot and branch 2 go.
    N : int
        Length of price vector and CDFs.
    bgo : float
        Lower bound of price support in GO market.
    pmaxgo : float
        Price cap in GO market.
    branch : int
        Branch 1 in spot market if 1, branch 2 otherwise.

    Returns
    -------
    F1 : array
        CDF of supplier 1 in GO market.
    F2 : array
        CDF of supplier 2 in GO market.
    p : array
        Price vector.

    """
    eps = (pmaxgo - bgo) / N
    p = np.zeros(N + 1)
    F_h = np.zeros(N + 1)
    F_l = np.zeros(N + 1)

    if branch == 1:
        for i in range(N + 1):
            p[i] = bgo + eps * (i)
            F_h[i] = ((p[i] - bgo) * q1go22) / (p[i] * (q1go22 - q1go12))
            F_l[i] = ((p[i] - bgo) * q1go11) / (p[i] * (q1go11 - q1go21))
    else:
        for i in range(N + 1):
            p[i] = bgo + eps * (i)
            F_h[i] = ((p[i] - bgo) * q2go22) / (p[i] * (q2go22 - q2go12))
            F_l[i] = ((p[i] - bgo) * q2go11) / (p[i] * (q2go11 - q2go21))
    F_h[N] = 1
    F_l[N] = 1
    return F_h, F_l, p

def bounds_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, b1go, b2go, pmaxs):
    """
    This function calculates the lower bounds of the price support for the two
    suppliers in the spot market. See lemma 3 in the paper.
    
    Note that the first number in the quantity variables refers to the branch in 
    the spot market, the second number refers to the branch in the GO market, 
    while the last number refers to the supplier. 

    Parameters
    ----------
    q11 : float
        Quantity of supplier 1 in branch 1 spot.
    q12 : float
        Quantity of supplier 2 in branch 1 spot.
    q21 : float
        Quantity of supplier 1 in branch 2 spot.
    q22 : float
        Quantity of supplier 2 in branch 2 spot.
    q1go11 : float
        Quantity of supplier 1 in branch 1 spot and branch 1 go.
    q1go22 : float
        Quantity of supplier 2 in branch 1 spot and branch 2 go.
    q2go11 : float
        Quantity of supplier 1 in branch 2 spot and branch 1 go.
    q2go22 : float
        Quantity of supplier 2 in branch 2 spot and branch 2 go.
    b1go : float
        Lower bound of price support in GO market in branch 1 spot (go1).
    b2go : float
        Lower bound of price support in GO market in branch 2 spot (go2).
    pmaxs : float
        Price cap in spot market.

    Returns
    -------
    b1 : float
        Lower bound of price support of supplier 1 in spot market.
    b2 : float
        Lower bound of price support of supplier 2 in spot market.
    b : float
        Lower bound of price support in spot market.

    """
    b1 = ((pmaxs * q21) + (b2go * q2go11) - (b1go * q1go11)) / q11
    b2 = ((pmaxs * q12) + (b1go * q1go22) - (b2go * q2go22)) / q22
    b = max(b1, b2)
    return b1, b2, b

def CDF_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, N, bs, b1go, b2go, pmaxs):
    """
    This function calculates the cumulative distribution functions for both
    suppliers the spot market. See proposition 2 in the paper.

    Note that the first number in the quantity variables refers to the branch in 
    the spot market, the second number refers to the branch in the GO market, 
    while the last number refers to the supplier.
 
    Parameters
    ----------
    q11 : float
        Quantity of supplier 1 in branch 1 spot.
    q12 : float
        Quantity of supplier 2 in branch 1 spot.
    q21 : float
        Quantity of supplier 1 in branch 2 spot.
    q22 : float
        Quantity of supplier 2 in branch 2 spot.
    q1go11 : float
        Quantity of supplier 1 in branch 1 spot and branch 1 go.
    q1go22 : float
        Quantity of supplier 2 in branch 1 spot and branch 2 go.
    q2go11 : float
        Quantity of supplier 1 in branch 2 spot and branch 1 go.
    q2go22 : float
        Quantity of supplier 2 in branch 2 spot and branch 2 go.
    N : int
        Length of price vector and CDFs.
    bs : float
        Lower bound of price support in spot market.
    b1go : float
        Lower bound of price support in GO market in branch 1 spot (go1).
    b2go : float
        Lower bound of price support in GO market in branch 2 spot (go2).
    pmaxs : float
        Price cap in spot market.

    Returns
    -------
    F1 : array
        CDF of supplier 1 in spot market.
    F2 : array
        CDF of supplier 2 in spot market.
    p : array
        Price vector.

    """
    eps = (pmaxs - bs) / N
    p = np.zeros(N + 1)
    F_h = np.zeros(N + 1)
    F_l = np.zeros(N + 1)
    for i in range(N + 1):
        p[i] = bs + eps * (i)
        F_h[i] = ((p[i] - bs) * q22) / ((p[i] * (q22 - q12)) + (b2go * q2go22 - b1go * q1go22))
        F_l[i] = ((p[i] - bs) * q11) / ((p[i] * (q11 - q21)) + (b1go * q1go11 - b2go * q2go11))

    F_h[N] = 1
    F_l[N] = 1
    return F_h, F_l, p

def exp_price(F_h, F_l, p):
    """
    This function calculates the expected price in the spot market for each 
    of the suppliers.

    Parameters
    ----------
    F1 : array
        CDF of supplier 1 in spot market.
    F2 : array
        CDF of supplier 2 in spot market.
    p : array
        Price vector.

    Returns
    -------
    E1 : float
        Expected bid of supplier 1 in spot market.
    E2 : float
        Expected bid of supplier 2 in spot market.

    """
    F_h_diff = np.diff(F_h)
    F_l_diff = np.diff(F_l)

    E_h = sum(p[1:] * F_h_diff)
    E_l = sum(p[1:] * F_l_diff)

    return E_h, E_l

def consumer_surplus_spot(al, ah, El, Eh, pmax):
    CS= ((pmax-El)*al) +((pmax-Eh)*ah)
    return CS

def consumer_surplus_go(al, ah, El, Eh, pmax):
    CS= (pmax-((El+Eh)/2))*(al+ah)
    return CS

def profit(b, q1, q2):
    pi1 = b*q1
    pi2 = b*q2
    return pi1, pi2

def plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, alpha1, alpha2, cases, branch):
    a2_lst = np.linspace(7, 8, 100)

    E_h_lst = []
    E_l_lst = []
    CS_lst = []
    pi1_lst = []
    pi2_lst = []
    W_lst = []

    if branch == 1:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2, ah_go, al_go, T, alpha1, alpha2, cases)
            b1, b2, bgo1 = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch)
            F_hgo1, F_lgo1, pgo1 = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, bgo1, pmaxgo, branch)
            E_h, E_l = exp_price(F_hgo1, F_lgo1, pgo1)
            CS = consumer_surplus_go(al_go, ah_go, E_l, E_h, pmaxgo)
            pi1, pi2 = profit(bgo1, q1go11, q1go22)
            W = CS+pi1+pi2
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)
            CS_lst.append(CS)
            pi1_lst.append(pi1)
            pi2_lst.append(pi2)
            W_lst.append(W)
    elif branch == 2:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2, ah_go, al_go, T, alpha1, alpha2, cases)
            b1, b2, bgo2 = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch)
            F_hgo1, F_lgo1, pgo1 = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, bgo2, pmaxgo, branch)
            E_h, E_l = exp_price(F_hgo1, F_lgo1, pgo1)
            CS = consumer_surplus_go(al_go, ah_go, E_l, E_h, pmaxgo)
            pi1, pi2 = profit(bgo2, q2go11, q2go22)
            W = CS + pi1 + pi2
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)
            CS_lst.append(CS)
            pi1_lst.append(pi1)
            pi2_lst.append(pi2)
            W_lst.append(W)
    elif branch == 0:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2, ah_go, al_go, T, alpha1, alpha2, cases)
            b11go, b12go, b1go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch=1)
            b21go, b22go, b2go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch=2)
            b1sgo, b2sgo, bsgo = bounds_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, b1go, b2go, pmaxs)
            F1sgo, F2sgo, psgo = CDF_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, N, bsgo, b1go, b2go, pmaxs)
            E_h, E_l = exp_price(F1sgo, F2sgo, psgo)
            CS = consumer_surplus_spot(a2, ah, E_l, E_h, pmaxs)
            pi1, pi2 = profit(bsgo, q11, q22)
            W = CS + pi1 + pi2
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)
            CS_lst.append(CS)
            pi1_lst.append(pi1)
            pi2_lst.append(pi2)
            W_lst.append(W)
    else:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2, ah_go, al_go, T, alpha1, alpha2, cases)
            b1s, b2s, bs = bounds_spot(q11, q12, q21, q22, 0, 0, 0, 0, 0, 0, pmaxs)
            F1s, F2s, ps = CDF_spot(q11, q12, q21, q22, 0, 0, 0, 0, N, bs, 0, 0, pmaxs)
            E_h, E_l = exp_price(F1s, F2s, ps)
            CS = consumer_surplus_spot(a2, ah, E_l, E_h, pmaxs)
            pi1, pi2 = profit(bs, q11, q22)
            W = CS + pi1 + pi2
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)
            CS_lst.append(CS)
            pi1_lst.append(pi1)
            pi2_lst.append(pi2)
            W_lst.append(W)

    return E_h_lst, E_l_lst, a2_lst, CS_lst, pi1_lst, pi2_lst, W_lst

if __name__=='__main__': 
    
    #Symmetric. Result 1: no-constraint vs. constraint.
    #%reset -f
    
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    ah = 7
    al = 7
    ah_go = 3
    al_go = 3
    kh = 12
    kl = 12
    alpha1 =1
    alpha2 = 1
    plot = 'strategies'
    cases = 'case1'
    T = 2
    pmaxs = 7
    pmaxgo = 2
    N = 100
    N2 = 400
    
    #Case 1
    q11_case1, q12_case1, q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q21_case1, q22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case1')
    #GO1:
    b11go_case1, b12go_case1, b1go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=1)
    F1go1_case1, F1go2_case1, pgo1_case1 = CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b1go_case1, pmaxgo, branch=1)
    E1go1_case1, E1go2_case1 = exp_price(F1go1_case1, F1go2_case1, pgo1_case1)
    #GO2:
    b21go_case1, b22go_case1, b2go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=2)
    F2go1_case1, F2go2_case1, pgo2_case1= CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b2go_case1, pmaxgo, branch=2)
    E2go1_case1, E2go2_case1 = exp_price(F2go1_case1, F2go2_case1, pgo2_case1)
    #Spot
    b1sgo_case1, b2sgo_case1, bsgo_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, b1go_case1, b2go_case1, pmaxs)
    F1sgo_case1, F2sgo_case1, psgo_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, N, bsgo_case1, b1go_case1, b2go_case1, pmaxs)
    E1sgo_case1, E2sgo_case1 = exp_price(F1sgo_case1, F2sgo_case1, psgo_case1)
    b1s_case1, b2s_case1, bs_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case1, F2s_case1, ps_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, N, bs_case1, 0, 0, pmaxs)
    E1s_case1, E2s_case1 = exp_price(F1s_case1, F2s_case1, ps_case1)

    
    #Case 2
    q11_case2, q12_case2, q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q21_case2, q22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case2')
    #GO1:
    b11go_case2, b12go_case2, b1go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=1)
    F1go1_case2, F1go2_case2, pgo1_case2 = CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b1go_case2, pmaxgo, branch=1)
    E1go1_case2, E1go2_case2 = exp_price(F1go1_case2, F1go2_case2, pgo1_case2)
    #GO2:
    b21go_case2, b22go_case2, b2go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=2)
    F2go1_case2, F2go2_case2, pgo2_case2= CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b2go_case2, pmaxgo, branch=2)
    E2go1_case2, E2go2_case2 = exp_price(F2go1_case2, F2go2_case2, pgo2_case2)
    #Spot
    b1sgo_case2, b2sgo_case2, bsgo_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, b1go_case2, b2go_case2, pmaxs)
    F1sgo_case2, F2sgo_case2, psgo_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, N, bsgo_case2, b1go_case2, b2go_case2, pmaxs)
    E1sgo_case2, E2sgo_case2 = exp_price(F1sgo_case2, F2sgo_case2, psgo_case2)
    b1s_case2, b2s_case2, bs_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case2, F2s_case2, ps_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, N, bs_case2, 0, 0, pmaxs)
    E1s_case2, E2s_case2 = exp_price(F1s_case2, F2s_case2, ps_case2)

    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    
    #Case 1
    ax[0].plot(ps_case1, F1s_case1, color = colors["c"], alpha=1)
    ax[0].plot([E1s_case1, E1s_case1], [0,1], color = colors["c"], alpha=1)
    ax[0].plot(ps_case1, F2s_case1, color = colors["p-g"], alpha=1)
    ax[0].plot([E2s_case1, E2s_case1], [0,1], color = colors["p-g"], alpha=1)
    ax[0].text(E1s_case1+0.1, 0.98, "$E_1^{s}=E_2^{s}=5.15$", color = colors["p-g"], fontsize=18)
    ax[0].text(E1s_case1+0.3, 0.6, "$F_1^{s}(p^s)=F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)
    
    ax[0].plot(psgo_case1, F1sgo_case1, color = colors["s-b"], alpha=1)
    ax[0].plot([E1sgo_case1, E1sgo_case1], [0,1], color = colors["s-b"], alpha=1)
    ax[0].plot(psgo_case1, F2sgo_case1, color = colors["b-s"], alpha=1)
    ax[0].plot([E2sgo_case1, E2sgo_case1], [0,1], color = colors["b-s"], alpha=1)
    ax[0].text(E1sgo_case1-1.2, 0.98, "$E_1^{sgo}=E_2^{sgo}=5.13$", color = colors["b-s"], fontsize=18)
    ax[0].text(E1sgo_case1-1.6, 0.5, "$F_1^{sgo}(p^{sgo})=F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18)
    
    ax[0].set_xlim(3.5, 7.5)
    ax[0].set_ylim(0, 1.05)
    ax[0].set(xticks=[3.5, bsgo_case1-0.05, bs_case1+0.05, pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].tick_params(bottom = False)
    ax[0].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[0].set_yticklabels(['0', '1'], fontsize=16)
    ax[0].set_ylabel('$F^{s}(p^s)$, $F^{sgo}(p^{sgo})$', fontsize=18)
    ax[0].set_xlabel('$p^{s}$, $p^{sgo}$', fontsize=18)
    ax[0].set_title("GO, no constraint", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Case 2
    ax[1].plot(ps_case2, F1s_case2, color = colors["c"], alpha=1)
    ax[1].plot([E1s_case2, E1s_case2], [0,1], color = colors["c"], alpha=1)
    ax[1].plot(ps_case2, F2s_case2, color = colors["p-g"], alpha=1)
    ax[1].plot([E2s_case2, E2s_case2], [0,1], color = colors["p-g"], alpha=1)
    ax[1].text(E1s_case2+0.1, 0.98, "$E_1^{s}=E_2^{s}=5.15$", color = colors["p-g"], fontsize=18)
    ax[1].text(E1s_case2+0.3, 0.6, "$F_1^{s}(p^s)=F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)

    ax[1].plot(psgo_case2, F1sgo_case2, color = colors["s-b"], alpha=1)
    ax[1].plot([E1sgo_case2, E1sgo_case2], [0,1], color = colors["s-b"], alpha=1)
    ax[1].plot(psgo_case2, F2sgo_case2, color = colors["b-s"], alpha=1)
    ax[1].plot([E2sgo_case2, E2sgo_case2], [0,1], color = colors["b-s"], alpha=1)
    ax[1].text(E1sgo_case2-1.2, 0.98, "$E_1^{sgo}=E_2^{sgo}=5.15$", color = colors["b-s"], fontsize=18)
    ax[1].text(E1sgo_case2-1.6, 0.5, "$F_1^{sgo}(p^{sgo})=F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18)

    ax[1].set_xlim(3.5, 7.5)
    ax[1].set_ylim(0, 1.05)
    ax[1].set(xticks=[3.5, bsgo_case2, bs_case2, pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[1].set_yticklabels(['0', '1'], fontsize=16)
    ax[1].set_ylabel('$F^{s}(p^s)$, $F^{sgo}(p^{sgo})$', fontsize=18)
    ax[1].set_xlabel('$p^{s}$, $p^{sgo}$', fontsize=18)
    ax[1].set_title("GO, constraint", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Symmetric. Result 2: Low demand GO.
    #%reset -f
    
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    ah = 7
    al = 7
    ah_go = 2.5
    al_go = 2.5
    kh = 12
    kl = 12
    alpha1 =1
    alpha2 = 1
    plot = 'strategies'
    cases = 'case1'
    T = 2
    pmaxs = 7
    pmaxgo = 2
    N = 100
    N2 = 400
    
    #Case 1
    q11_case1, q12_case1, q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q21_case1, q22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case1')
    #GO1:
    b11go_case1, b12go_case1, b1go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=1)
    F1go1_case1, F1go2_case1, pgo1_case1 = CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b1go_case1, pmaxgo, branch=1)
    E1go1_case1, E1go2_case1 = exp_price(F1go1_case1, F1go2_case1, pgo1_case1)
    #GO2:
    b21go_case1, b22go_case1, b2go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=2)
    F2go1_case1, F2go2_case1, pgo2_case1= CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b2go_case1, pmaxgo, branch=2)
    E2go1_case1, E2go2_case1 = exp_price(F2go1_case1, F2go2_case1, pgo2_case1)
    #Spot
    b1sgo_case1, b2sgo_case1, bsgo_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, b1go_case1, b2go_case1, pmaxs)
    F1sgo_case1, F2sgo_case1, psgo_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, N, bsgo_case1, b1go_case1, b2go_case1, pmaxs)
    E1sgo_case1, E2sgo_case1 = exp_price(F1sgo_case1, F2sgo_case1, psgo_case1)
    b1s_case1, b2s_case1, bs_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case1, F2s_case1, ps_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, N, bs_case1, 0, 0, pmaxs)
    E1s_case1, E2s_case1 = exp_price(F1s_case1, F2s_case1, ps_case1)

    
    #Case 2
    q11_case2, q12_case2, q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q21_case2, q22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case2')
    #GO1:
    b11go_case2, b12go_case2, b1go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=1)
    F1go1_case2, F1go2_case2, pgo1_case2 = CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b1go_case2, pmaxgo, branch=1)
    E1go1_case2, E1go2_case2 = exp_price(F1go1_case2, F1go2_case2, pgo1_case2)
    #GO2:
    b21go_case2, b22go_case2, b2go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=2)
    F2go1_case2, F2go2_case2, pgo2_case2= CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b2go_case2, pmaxgo, branch=2)
    E2go1_case2, E2go2_case2 = exp_price(F2go1_case2, F2go2_case2, pgo2_case2)
    #Spot
    b1sgo_case2, b2sgo_case2, bsgo_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, b1go_case2, b2go_case2, pmaxs)
    F1sgo_case2, F2sgo_case2, psgo_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, N, bsgo_case2, b1go_case2, b2go_case2, pmaxs)
    E1sgo_case2, E2sgo_case2 = exp_price(F1sgo_case2, F2sgo_case2, psgo_case2)
    b1s_case2, b2s_case2, bs_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case2, F2s_case2, ps_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, N, bs_case2, 0, 0, pmaxs)
    E1s_case2, E2s_case2 = exp_price(F1s_case2, F2s_case2, ps_case2)

    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    
    #Case 1
    ax[0].plot(ps_case1, F1s_case1, color = colors["c"], alpha=1)
    ax[0].plot([E1s_case1, E1s_case1], [0,1], color = colors["c"], alpha=1)
    ax[0].plot(ps_case1, F2s_case1, color = colors["p-g"], alpha=1)
    ax[0].plot([E2s_case1, E2s_case1], [0,1], color = colors["p-g"], alpha=1)
    ax[0].text(E1s_case1+0.1, 0.98, "$E_1^{s}=E_2^{s}=5.15$", color = colors["p-g"], fontsize=18)
    ax[0].text(E1s_case1+0.3, 0.6, "$F_1^{s}(p^s)=F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)
    
    ax[0].plot(psgo_case1, F1sgo_case1, color = colors["s-b"], alpha=1)
    ax[0].plot([E1sgo_case1, E1sgo_case1], [0,1], color = colors["s-b"], alpha=1)
    ax[0].plot(psgo_case1, F2sgo_case1, color = colors["b-s"], alpha=1)
    ax[0].plot([E2sgo_case1, E2sgo_case1], [0,1], color = colors["b-s"], alpha=1)
    ax[0].text(E1sgo_case1-1.2, 0.98, "$E_1^{sgo}=E_2^{sgo}=5.15$", color = colors["b-s"], fontsize=18)
    ax[0].text(E1sgo_case1-1.6, 0.5, "$F_1^{sgo}(p^{sgo})=F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18)
    
    ax[0].set_xlim(3.5, 7.5)
    ax[0].set_ylim(0, 1.05)
    ax[0].set(xticks=[3.5, bsgo_case1, bs_case1, pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[0].set_yticklabels(['0', '1'], fontsize=16)
    ax[0].set_ylabel('$F^{s}(p^s)$, $F^{sgo}(p^{sgo})$', fontsize=18)
    ax[0].set_xlabel('$p^{s}$, $p^{sgo}$', fontsize=18)
    ax[0].set_title("GO, no constraint", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Case 2
    ax[1].plot(ps_case2, F1s_case2, color = colors["c"], alpha=1)
    ax[1].plot([E1s_case2, E1s_case2], [0,1], color = colors["c"], alpha=1)
    ax[1].plot(ps_case2, F2s_case2, color = colors["p-g"], alpha=1)
    ax[1].plot([E2s_case2, E2s_case2], [0,1], color = colors["p-g"], alpha=1)
    ax[1].text(E1s_case2+0.1, 0.98, "$E_1^{s}=E_2^{s}=5.15$", color = colors["p-g"], fontsize=18)
    ax[1].text(E1s_case2+0.3, 0.6, "$F_1^{s}(p^s)=F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)

    ax[1].plot(psgo_case2, F1sgo_case2, color = colors["s-b"], alpha=1)
    ax[1].plot([E1sgo_case2, E1sgo_case2], [0,1], color = colors["s-b"], alpha=1)
    ax[1].plot(psgo_case2, F2sgo_case2, color = colors["b-s"], alpha=1)
    ax[1].plot([E2sgo_case2, E2sgo_case2], [0,1], color = colors["b-s"], alpha=1)
    ax[1].text(E1sgo_case2-1.2, 0.98, "$E_1^{sgo}=E_2^{sgo}=5.15$", color = colors["b-s"], fontsize=18)
    ax[1].text(E1sgo_case2-1.6, 0.5, "$F_1^{sgo}(p^{sgo})=F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18)

    ax[1].set_xlim(3.5, 7.5)
    ax[1].set_ylim(0, 1.05)
    ax[1].set(xticks=[3.5, bsgo_case2, bs_case2, pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[1].set_yticklabels(['0', '1'], fontsize=16)
    ax[1].set_ylabel('$F^{s}(p^s)$, $F^{sgo}(p^{sgo})$', fontsize=18)
    ax[1].set_xlabel('$p^{s}$, $p^{sgo}$', fontsize=18)
    ax[1].set_title("GO, constraint", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Symmetric. Result 3: Low demand green capacity.
    #%reset -f
    
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    ah = 7
    al = 7
    ah_go = 3
    al_go = 3
    kh = 12
    kl = 12
    alpha1 =0.9
    alpha2 = 0.9
    plot = 'strategies'
    cases = 'case1'
    T = 2
    pmaxs = 7
    pmaxgo = 2
    N = 100
    N2 = 400
    
    #Case 1
    q11_case1, q12_case1, q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q21_case1, q22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case1')
    #GO1:
    b11go_case1, b12go_case1, b1go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=1)
    F1go1_case1, F1go2_case1, pgo1_case1 = CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b1go_case1, pmaxgo, branch=1)
    E1go1_case1, E1go2_case1 = exp_price(F1go1_case1, F1go2_case1, pgo1_case1)
    #GO2:
    b21go_case1, b22go_case1, b2go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=2)
    F2go1_case1, F2go2_case1, pgo2_case1= CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b2go_case1, pmaxgo, branch=2)
    E2go1_case1, E2go2_case1 = exp_price(F2go1_case1, F2go2_case1, pgo2_case1)
    #Spot
    b1sgo_case1, b2sgo_case1, bsgo_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, b1go_case1, b2go_case1, pmaxs)
    F1sgo_case1, F2sgo_case1, psgo_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, N, bsgo_case1, b1go_case1, b2go_case1, pmaxs)
    E1sgo_case1, E2sgo_case1 = exp_price(F1sgo_case1, F2sgo_case1, psgo_case1)
    b1s_case1, b2s_case1, bs_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case1, F2s_case1, ps_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, N, bs_case1, 0, 0, pmaxs)
    E1s_case1, E2s_case1 = exp_price(F1s_case1, F2s_case1, ps_case1)

    
    #Case 2
    q11_case2, q12_case2, q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q21_case2, q22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case2')
    #GO1:
    b11go_case2, b12go_case2, b1go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=1)
    F1go1_case2, F1go2_case2, pgo1_case2 = CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b1go_case2, pmaxgo, branch=1)
    E1go1_case2, E1go2_case2 = exp_price(F1go1_case2, F1go2_case2, pgo1_case2)
    #GO2:
    b21go_case2, b22go_case2, b2go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=2)
    F2go1_case2, F2go2_case2, pgo2_case2= CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b2go_case2, pmaxgo, branch=2)
    E2go1_case2, E2go2_case2 = exp_price(F2go1_case2, F2go2_case2, pgo2_case2)
    #Spot
    b1sgo_case2, b2sgo_case2, bsgo_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, b1go_case2, b2go_case2, pmaxs)
    F1sgo_case2, F2sgo_case2, psgo_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, N, bsgo_case2, b1go_case2, b2go_case2, pmaxs)
    E1sgo_case2, E2sgo_case2 = exp_price(F1sgo_case2, F2sgo_case2, psgo_case2)
    b1s_case2, b2s_case2, bs_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case2, F2s_case2, ps_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, N, bs_case2, 0, 0, pmaxs)
    E1s_case2, E2s_case2 = exp_price(F1s_case2, F2s_case2, ps_case2)

    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    
    #Case 1
    ax[0].plot(ps_case1, F1s_case1, color = colors["c"], alpha=1)
    ax[0].plot([E1s_case1, E1s_case1], [0,1], color = colors["c"], alpha=1)
    ax[0].plot(ps_case1, F2s_case1, color = colors["p-g"], alpha=1)
    ax[0].plot([E2s_case1, E2s_case1], [0,1], color = colors["p-g"], alpha=1)
    ax[0].text(E1s_case1+0.1, 0.98, "$E_1^{s}=E_2^{s}=5.15$", color = colors["p-g"], fontsize=18)
    ax[0].text(E1s_case1+0.3, 0.6, "$F_1^{s}(p^s)=F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)
    
    ax[0].plot(psgo_case1, F1sgo_case1, color = colors["s-b"], alpha=1)
    ax[0].plot([E1sgo_case1, E1sgo_case1], [0,1], color = colors["s-b"], alpha=1)
    ax[0].plot(psgo_case1, F2sgo_case1, color = colors["b-s"], alpha=1)
    ax[0].plot([E2sgo_case1, E2sgo_case1], [0,1], color = colors["b-s"], alpha=1)
    ax[0].text(E1sgo_case1-1.2, 0.98, "$E_1^{sgo}=E_2^{sgo}=5.10$", color = colors["b-s"], fontsize=18)
    ax[0].text(E1sgo_case1-1.54, 0.5, "$F_1^{sgo}(p^{sgo})=F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18)
    
    ax[0].set_xlim(3.5, 7.5)
    ax[0].set_ylim(0, 1.05)
    ax[0].set(xticks=[3.5, bsgo_case1-0.05, bs_case1+0.05, pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].tick_params(bottom = False)
    ax[0].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[0].set_yticklabels(['0', '1'], fontsize=16)
    ax[0].set_ylabel('$F^{s}(p^s)$, $F^{sgo}(p^{sgo})$', fontsize=18)
    ax[0].set_xlabel('$p^{s}$, $p^{sgo}$', fontsize=18)
    ax[0].set_title("GO, no constraint", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Case 2
    ax[1].plot(ps_case2, F1s_case2, color = colors["c"], alpha=1)
    ax[1].plot([E1s_case2, E1s_case2], [0,1], color = colors["c"], alpha=1)
    ax[1].plot(ps_case2, F2s_case2, color = colors["p-g"], alpha=1)
    ax[1].plot([E2s_case2, E2s_case2], [0,1], color = colors["p-g"], alpha=1)
    ax[1].text(E1s_case2+0.1, 0.98, "$E_1^{s}=E_2^{s}=5.15$", color = colors["p-g"], fontsize=18)
    ax[1].text(E1s_case2+0.3, 0.6, "$F_1^{s}(p^s)=F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)

    ax[1].plot(psgo_case2, F1sgo_case2, color = colors["s-b"], alpha=1)
    ax[1].plot([E1sgo_case2, E1sgo_case2], [0,1], color = colors["s-b"], alpha=1)
    ax[1].plot(psgo_case2, F2sgo_case2, color = colors["b-s"], alpha=1)
    ax[1].plot([E2sgo_case2, E2sgo_case2], [0,1], color = colors["b-s"], alpha=1)
    ax[1].text(E1sgo_case2-1.2, 0.98, "$E_1^{sgo}=E_2^{sgo}=5.13$", color = colors["b-s"], fontsize=18)
    ax[1].text(E1sgo_case2-1.6, 0.5, "$F_1^{sgo}(p^{sgo})=F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18)

    ax[1].set_xlim(3.5, 7.5)
    ax[1].set_ylim(0, 1.05)
    ax[1].set(xticks=[3.5, bsgo_case2-0.07, bs_case2+0.07, pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].tick_params(bottom = False)
    ax[1].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[1].set_yticklabels(['0', '1'], fontsize=16)
    ax[1].set_ylabel('$F^{s}(p^s)$, $F^{sgo}(p^{sgo})$', fontsize=18)
    ax[1].set_xlabel('$p^{s}$, $p^{sgo}$', fontsize=18)
    ax[1].set_title("GO, constraint", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    plt.savefig('superfig.png', dpi=300)
    plt.savefig('superfig.png', dpi=300)
    
    #%reset -f
    
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    ah = 8
    al = 7
    ah_go = 3
    al_go = 3
    kh = 12
    kl = 12
    plot = 'strategies'
    cases = 'case1'
    T = 2
    pmaxs = 7
    pmaxgo = 2
    N = 100
    N2 = 400
    
    #Case 1
    q11_case1, q12_case1, q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q21_case1, q22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case1')
    #GO1:
    b11go_case1, b12go_case1, b1go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=1)
    F1go1_case1, F1go2_case1, pgo1_case1 = CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b1go_case1, pmaxgo, branch=1)
    E1go1_case1, E1go2_case1 = exp_price(F1go1_case1, F1go2_case1, pgo1_case1)
    #GO2:
    b21go_case1, b22go_case1, b2go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=2)
    F2go1_case1, F2go2_case1, pgo2_case1= CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b2go_case1, pmaxgo, branch=2)
    E2go1_case1, E2go2_case1 = exp_price(F2go1_case1, F2go2_case1, pgo2_case1)
    #Spot
    b1sgo_case1, b2sgo_case1, bsgo_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, b1go_case1, b2go_case1, pmaxs)
    F1sgo_case1, F2sgo_case1, psgo_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, N, bsgo_case1, b1go_case1, b2go_case1, pmaxs)
    E1sgo_case1, E2sgo_case1 = exp_price(F1sgo_case1, F2sgo_case1, psgo_case1)
    b1s_case1, b2s_case1, bs_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case1, F2s_case1, ps_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, N, bs_case1, 0, 0, pmaxs)
    E1s_case1, E2s_case1 = exp_price(F1s_case1, F2s_case1, ps_case1)

    
    #Case 2
    q11_case2, q12_case2, q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q21_case2, q22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case2')
    #GO1:
    b11go_case2, b12go_case2, b1go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=1)
    F1go1_case2, F1go2_case2, pgo1_case2 = CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b1go_case2, pmaxgo, branch=1)
    E1go1_case2, E1go2_case2 = exp_price(F1go1_case2, F1go2_case2, pgo1_case2)
    #GO2:
    b21go_case2, b22go_case2, b2go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=2)
    F2go1_case2, F2go2_case2, pgo2_case2= CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b2go_case2, pmaxgo, branch=2)
    E2go1_case2, E2go2_case2 = exp_price(F2go1_case2, F2go2_case2, pgo2_case2)
    #Spot
    b1sgo_case2, b2sgo_case2, bsgo_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, b1go_case2, b2go_case2, pmaxs)
    F1sgo_case2, F2sgo_case2, psgo_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, N, bsgo_case2, b1go_case2, b2go_case2, pmaxs)
    E1sgo_case2, E2sgo_case2 = exp_price(F1sgo_case2, F2sgo_case2, psgo_case2)
    b1s_case2, b2s_case2, bs_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case2, F2s_case2, ps_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, N, bs_case2, 0, 0, pmaxs)
    E1s_case2, E2s_case2 = exp_price(F1s_case2, F2s_case2, ps_case2)

    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    
    #Case 1
    ax[0].plot(ps_case1, F1s_case1, color = colors["c"], alpha=1)
    ax[0].plot([E1s_case1, E1s_case1], [0,1], color = colors["c"], alpha=1)
    ax[0].plot(ps_case1, F2s_case1, color = colors["p-g"], alpha=1)
    ax[0].plot([E2s_case1, E2s_case1], [0,1], color = colors["p-g"], alpha=1)
    ax[0].text(E1s_case1+0.1, 0.98, "$E_1^{s}=5.53$", color = colors["c"], fontsize=18)
    ax[0].text(E2s_case1-0.7, 0.98, "$E_2^{s}=5.37$", color = colors["p-g"], fontsize=18)
    ax[0].text(E1s_case1+0.3, 0.6, "$F_1^{s}(p^s)$", color = colors["c"], fontsize=18)
    ax[0].text(E1s_case1-1, 0.4, "$F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)
    
    ax[0].set_xlim(3.5, 7.5)
    ax[0].set_ylim(0, 1.05)
    ax[0].set(xticks=[3.5,  bs_case1, pmaxs], xticklabels=['3.5', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].set_xticklabels(['3.5',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[0].set_yticklabels(['0', '1'], fontsize=16)
    ax[0].set_ylabel('$F^{s}(p^s)$', fontsize=18)
    ax[0].set_xlabel('$p^{s}$', fontsize=18)
    ax[0].set_title("GO, no constraint (Spot market)", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Case 2
    ax[1].plot(psgo_case1, F1sgo_case1, color = colors["s-b"], alpha=1)
    ax[1].plot([E1sgo_case1, E1sgo_case1], [0,1], color = colors["s-b"], alpha=1)
    ax[1].plot(psgo_case1, F2sgo_case1, color = colors["b-s"], alpha=1)
    ax[1].plot([E2sgo_case1, E2sgo_case1], [0,1], color = colors["b-s"], alpha=1)
    ax[1].text(E1sgo_case1-0.8, 0.98, "$E_1^{sgo}=5.26$", color = colors["s-b"], fontsize=18)
    ax[1].text(E2sgo_case1+0.1, 0.98, "$E_2^{sgo}=5.35$", color = colors["b-s"], fontsize=18)
    ax[1].text(E1sgo_case1-1.1, 0.4, "$F_1^{sgo}(p^{sgo})$", color = colors["s-b"], fontsize=18) 
    ax[1].text(E2sgo_case1+0.3, 0.6, "$F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18) 

    ax[1].set_xlim(3.5, 7.5)
    ax[1].set_ylim(0, 1.05)
    ax[1].set(xticks=[3.5, bsgo_case1,  pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$', 'P'], fontsize=16)
    ax[1].set_yticklabels(['0', '1'], fontsize=16)
    ax[1].set_ylabel('$F^{sgo}(p^{sgo})$', fontsize=18)
    ax[1].set_xlabel('$p^{sgo}$', fontsize=18)
    ax[1].set_title("GO, no constraint (Spot-GO market)", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    plt.savefig('superfig.png', dpi=300)
    plt.savefig('superfig.png', dpi=300)

    #%reset -f
    
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
    ah = 8
    al = 7
    ah_go = 3.5
    al_go = 3
    kh = 12
    kl = 12
    plot = 'strategies'
    cases = 'case1'
    T = 2
    pmaxs = 7
    pmaxgo = 2
    N = 100
    N2 = 400
    
    #Case 1
    q11_case1, q12_case1, q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q21_case1, q22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2, 'case1')
    #GO1:
    b11go_case1, b12go_case1, b1go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=1)
    F1go1_case1, F1go2_case1, pgo1_case1 = CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b1go_case1, pmaxgo, branch=1)
    E1go1_case1, E1go2_case1 = exp_price(F1go1_case1, F1go2_case1, pgo1_case1)
    #GO2:
    b21go_case1, b22go_case1, b2go_case1 = bounds_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, pmaxgo, branch=2)
    F2go1_case1, F2go2_case1, pgo2_case1= CDF_GO(q1go11_case1, q1go12_case1, q1go21_case1, q1go22_case1, q2go11_case1, q2go12_case1, q2go21_case1, q2go22_case1, N, b2go_case1, pmaxgo, branch=2)
    E2go1_case1, E2go2_case1 = exp_price(F2go1_case1, F2go2_case1, pgo2_case1)
    #Spot
    b1sgo_case1, b2sgo_case1, bsgo_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, b1go_case1, b2go_case1, pmaxs)
    F1sgo_case1, F2sgo_case1, psgo_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, q1go11_case1, q1go22_case1, q2go11_case1, q2go22_case1, N, bsgo_case1, b1go_case1, b2go_case1, pmaxs)
    E1sgo_case1, E2sgo_case1 = exp_price(F1sgo_case1, F2sgo_case1, psgo_case1)
    b1s_case1, b2s_case1, bs_case1 = bounds_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case1, F2s_case1, ps_case1 = CDF_spot(q11_case1, q12_case1, q21_case1, q22_case1, 0, 0, 0, 0, N, bs_case1, 0, 0, pmaxs)
    E1s_case1, E2s_case1 = exp_price(F1s_case1, F2s_case1, ps_case1)

    
    #Case 2
    q11_case2, q12_case2, q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q21_case2, q22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2 = quantities(ah, al, ah_go, al_go, T, alpha1, alpha2,'case2')
    #GO1:
    b11go_case2, b12go_case2, b1go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=1)
    F1go1_case2, F1go2_case2, pgo1_case2 = CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b1go_case2, pmaxgo, branch=1)
    E1go1_case2, E1go2_case2 = exp_price(F1go1_case2, F1go2_case2, pgo1_case2)
    #GO2:
    b21go_case2, b22go_case2, b2go_case2 = bounds_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, pmaxgo, branch=2)
    F2go1_case2, F2go2_case2, pgo2_case2= CDF_GO(q1go11_case2, q1go12_case2, q1go21_case2, q1go22_case2, q2go11_case2, q2go12_case2, q2go21_case2, q2go22_case2, N, b2go_case2, pmaxgo, branch=2)
    E2go1_case2, E2go2_case2 = exp_price(F2go1_case2, F2go2_case2, pgo2_case2)
    #Spot
    b1sgo_case2, b2sgo_case2, bsgo_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, b1go_case2, b2go_case2, pmaxs)
    F1sgo_case2, F2sgo_case2, psgo_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, q1go11_case2, q1go22_case2, q2go11_case2, q2go22_case2, N, bsgo_case2, b1go_case2, b2go_case2, pmaxs)
    E1sgo_case2, E2sgo_case2 = exp_price(F1sgo_case2, F2sgo_case2, psgo_case2)
    b1s_case2, b2s_case2, bs_case2 = bounds_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, 0, 0, pmaxs)
    F1s_case2, F2s_case2, ps_case2 = CDF_spot(q11_case2, q12_case2, q21_case2, q22_case2, 0, 0, 0, 0, N, bs_case2, 0, 0, pmaxs)
    E1s_case2, E2s_case2 = exp_price(F1s_case2, F2s_case2, ps_case2)

    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20, 9))
    
    #Case 1
    ax[0].plot(ps_case1, F1s_case1, color = colors["c"], alpha=1)
    ax[0].plot([E1s_case1, E1s_case1], [0,1], color = colors["c"], alpha=1)
    ax[0].plot(ps_case1, F2s_case1, color = colors["p-g"], alpha=1)
    ax[0].plot([E2s_case1, E2s_case1], [0,1], color = colors["p-g"], alpha=1)
    ax[0].text(E1s_case1+0.1, 0.98, "$E_1^{s}=5.53$", color = colors["c"], fontsize=18)
    ax[0].text(E2s_case1-0.7, 0.98, "$E_2^{s}=5.37$", color = colors["p-g"], fontsize=18)
    ax[0].text(E1s_case1+0.3, 0.6, "$F_1^{s}(p^s)$", color = colors["c"], fontsize=18)
    ax[0].text(E1s_case1-1, 0.4, "$F_2^{s}(p^s)$", color = colors["p-g"], fontsize=18)
    
    ax[0].set_xlim(3.5, 7.5)
    ax[0].set_ylim(0, 1.05)
    ax[0].set(xticks=[3.5,  bs_case1, pmaxs], xticklabels=['3.5', r'$\underline{b}^s$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].set_xticklabels(['3.5',r'$\underline{b}^s$', 'P'], fontsize=16)
    ax[0].set_yticklabels(['0', '1'], fontsize=16)
    ax[0].set_ylabel('$F^{s}(p^s)$', fontsize=18)
    ax[0].set_xlabel('$p^{s}$', fontsize=18)
    ax[0].set_title("GO, no constraint (Spot market)", fontsize=20)
    right_side = ax[0].spines["right"]
    top_side = ax[0].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    
    #Case 2
    ax[1].plot(psgo_case1, F1sgo_case1, color = colors["s-b"], alpha=1)
    ax[1].plot([E1sgo_case1, E1sgo_case1], [0,1], color = colors["s-b"], alpha=1)
    ax[1].plot(psgo_case1, F2sgo_case1, color = colors["b-s"], alpha=1)
    ax[1].plot([E2sgo_case1, E2sgo_case1], [0,1], color = colors["b-s"], alpha=1)
    ax[1].text(E1sgo_case1-0.8, 0.98, "$E_1^{sgo}=5.21$", color = colors["s-b"], fontsize=18)
    ax[1].text(E2sgo_case1+0.1, 0.98, "$E_2^{sgo}=5.26$", color = colors["b-s"], fontsize=18)
    ax[1].text(E1sgo_case1-1.1, 0.4, "$F_1^{sgo}(p^{sgo})$", color = colors["s-b"], fontsize=18) 
    ax[1].text(E2sgo_case1+0.3, 0.6, "$F_2^{sgo}(p^{sgo})$", color = colors["b-s"], fontsize=18) 

    ax[1].set_xlim(3.5, 7.5)
    ax[1].set_ylim(0, 1.05)
    ax[1].set(xticks=[3.5, bsgo_case1,  pmaxs], xticklabels=['3.5', r'$\underline{b}^{sgo}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].set_xticklabels(['3.5', r'$\underline{b}^{sgo}$', 'P'], fontsize=16)
    ax[1].set_yticklabels(['0', '1'], fontsize=16)
    ax[1].set_ylabel('$F^{sgo}(p^{sgo})$', fontsize=18)
    ax[1].set_xlabel('$p^{sgo}$', fontsize=18)
    ax[1].set_title("GO, no constraint (Spot-GO market)", fontsize=20)
    right_side = ax[1].spines["right"]
    top_side = ax[1].spines["top"]
    right_side.set_visible(False)
    top_side.set_visible(False)
    plt.savefig('superfig.png', dpi=300)
    plt.savefig('superfig.png', dpi=300)


