# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:44:10 2021

@author: s14761
"""

import numpy as np

def determine_area(al, ah):
    if al+ah <= 60:
        area = 'B'
        area_num = 1
    else:
        area = 'C'
        area_num = 0
    return area, area_num

def CDF_dis_ex_ante(al, ah, kl, kh, T, P, N): 
    area, area_num = determine_area(al, ah)
    
    p = np.zeros(N+1)
    Fh = np.zeros(N+1)
    Fl = np.zeros(N+1)
    
    #Area B:
    if area_num == 1:
        q11s = al+ah
        q12s = 0
        q21s = ah-T
        q22s = al+T
        b1 = (P*q21s)/q11s
        b2 = (P*q12s)/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/(p[i]*(q22s-q12s))
            Fl[i]=((p[i]-b)*q11s)/(p[i]*(q11s-q21s))
    #Area C:        
    else:
        q11s = kh
        q12s = al+ah-kl
        q21s = ah-T
        q22s = al+T
        b1 = (P*q21s)/q11s
        b2 = (P*q12s)/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/(p[i]*(q22s-q12s))
            Fl[i]=((p[i]-b)*q11s)/(p[i]*(q11s-q21s))
    Fh[N] = 1
    Fl[N] =1    
    return Fh, Fl, p, b

def CDF_dis_ex_post(al, ah, kl, kh, T, P, N):  
    area, area_num = determine_area(al, ah)
    p = np.zeros(N+1)
    Fh = np.zeros(N+1)
    Fl = np.zeros(N+1)
    
    #Area B:
    if area_num == 1:
        q11s = al+ah
        q12s = 0
        q21s = 0
        q21r = (ah-T)-q21s
        q22s = al+ah
        q22r = q22s-(al+T)
        b1 = (P*(q21s+q21r))/q11s
        b2 = (P*(q12s)+(0*q22r))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/((p[i]*q22s-0*q22r)-(p[i]*q12s))
            if i == 0:
                Fl[i]=0
            else:
                Fl[i]=((p[i]-b)*q11s)/((p[i]*q11s)-(p[i]*q21s+P*q21r))
    #Area C:        
    else:
        q11s = kh
        q12s = al+ah-kh
        q21s = al+ah-kl
        q21r = (ah-T)-q21s
        q22s = kl
        q22r = q22s-(al+T)
        b1 = (P*(q21s+q21r))/q11s
        b2 = (P*(q12s)+(0*q22r))/q22s
        b = max(b1,b2)
        eps = (P-b)/N  
        for i in range(N+1):
            p[i]=b+eps*(i)
            Fh[i]=((p[i]-b)*q22s)/((p[i]*q22s-0*q22r)-(p[i]*q12s))
            Fl[i]=((p[i]-b)*q11s)/((p[i]*q11s)-(p[i]*q21s+P*q21r))
    Fh[N] = 1
    Fl[N] =1    
    return Fh, Fl, p, b

def welfare_ex_ante(Fh, Fl, p, al, ah, T, kl, kh, P):
    area, area_num = determine_area(al, ah)
    
    Fh_diff = np.diff(Fh)
    Fl_diff = np.diff(Fl)
    
    Eh = sum (p[1:]*Fh_diff)
    El = sum (p[1:]*Fl_diff)
    
    E = (El*al/(al+ah))+(Eh*ah/(al+ah))
    CS_capita = P-E
    CS_aggregate = CS_capita*(al+ah)
    
    #Area B:
    if area_num == 1:
        q11s = al+ah
        q12s = 0
        q21s = ah-T
        q22s = al+T
        b1 = (P*q21s)/q11s
        b2 = (P*q12s)/q22s
        b = max(b1,b2)
        pil = b*q22s
        pih = b*q11s
        pi_aggregate = pil+pih
    else:
        q11s = kh
        q12s = al+ah-kl
        q21s = ah-T
        q22s = al+T
        b1 = (P*q21s)/q11s
        b2 = (P*q12s)/q22s
        b = max(b1,b2)
        pil = b*q22s
        pih = b*q11s
        pi_aggregate = pil+pih
    
    welfare_aggregate = CS_aggregate + pi_aggregate
    
    return Eh, El, E, CS_capita, CS_aggregate, pil, pih, pi_aggregate, welfare_aggregate

def welfare_ex_post(Fh, Fl, p, al, ah, T, kl, kh, P):
    area, area_num = determine_area(al, ah)
    Fh_diff = np.diff(Fh)
    Fl_diff = np.diff(Fl)
    
    Eh = sum (p[1:]*Fh_diff)
    El = sum (p[1:]*Fl_diff)
    
    E = (El*al/(al+ah))+(Eh*ah/(al+ah))
    CS_capita = P-E
    CS_aggregate = CS_capita*(al+ah)
    
    #Area B:
    if area_num == 1:
        q11s = al+ah
        q12s = 0
        q21s = 0
        q21r = (ah-T)-q21s
        q22s = al+ah
        q22r = q22s-(al+T)
        b1 = (P*(q21s+q21r))/q11s
        b2 = (P*(q12s)+(0*q22r))/q22s
        b = max(b1,b2)
        pil = b*q22s
        pih = b*q11s
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    else:
        q11s = kh
        q12s = al+ah-kh
        q21s = al+ah-kl
        q21r = (ah-T)-q21s
        q22s = kl
        q22r = q22s-(al+T)
        b1 = (P*(q21s+q21r))/q11s
        b2 = (P*(q12s)+(0*q22r))/q22s
        b = max(b1,b2)
        pil = b*q22s
        pih = b*q11s
        pi_aggregate = pil+pih
        CS_capita_adjusted = CS_capita-(b*q22r/(al+ah))
        CS_aggregate_adjusted = CS_capita_adjusted*(al+ah)
    
    welfare_aggregate = CS_aggregate + pi_aggregate
    welfare_aggregate_adjusted = CS_aggregate_adjusted + pi_aggregate
    
    return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted

def d_simulate_model(al, ah, kl, kh, T, P, N, model, auction):
    
    if auction == 'discriminatory':    
        if model == 'no':
            Fh, Fl, p, b_no = CDF_dis_ex_ante(al, ah, kl, kh, T, P, N)
            Eh, El, E, CS_capita, CS_aggregate, pil, pih, pi_aggregate, welfare_aggregate = welfare_ex_ante(Fh, Fl, p, al, ah, T, kl, kh, P) 
            return Eh, El, E, CS_capita, CS_aggregate, pil, pih, pi_aggregate, welfare_aggregate
        else:
            Fh, Fl, p, b_no = CDF_dis_ex_post(al, ah, kl, kh, T, P, N)
            Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = welfare_ex_post(Fh, Fl, p, al, ah, T, kl, kh, P)
            return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted
    else:
        if model == 'no':
            Fh, Fl, p, b_no = CDF_dis_ex_ante(al, ah, kl, kh, T, P, N)
            Eh, El, E, CS_capita, CS_aggregate, pil, pih, pi_aggregate, welfare_aggregate = welfare_ex_ante(Fh, Fl, p, al, ah, T, kl, kh, P) 
            return Eh, El, E, CS_capita, CS_aggregate, pil, pih, pi_aggregate, welfare_aggregate
        else:
            Fh, Fl, p, b_no = CDF_dis_ex_post(al, ah, kl, kh, T, P, N)
            Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = welfare_ex_post(Fh, Fl, p, al, ah, T, kl, kh, P)
            return Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted


def plot_welfare_ex_ante(al, kl, kh, T, P, N, N2):
    ah_lst = np.linspace(41, 99, N2)
    
    Eh_lst = []
    El_lst = []
    E_lst = []
    CS_capita_lst = []
    CS_aggregate_lst = []
    pil_lst = []
    pih_lst = []
    pi_aggregate_lst = []
    welfare_aggregate_lst = []
    
    for ah in ah_lst:
        Fh, Fl, p, b = CDF_dis_ex_ante(al, ah, kl, kh, T, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = welfare_ex_post(Fh, Fl, p, al, ah, T, kl, kh, P)
        Eh, El, E, CS_capita, CS_aggregate, pil, pih, pi_aggregate, welfare_aggregate = welfare_ex_ante(Fh, Fl, p, al, ah, T, kl, kh, P)
        Eh_lst.append(Eh)
        El_lst.append(El)
        E_lst.append(E)
        CS_capita_lst.append(CS_capita)
        CS_aggregate_lst.append(CS_aggregate)
        pil_lst.append(pil)
        pih_lst.append(pih)
        pi_aggregate_lst.append(pi_aggregate)
        welfare_aggregate_lst.append(welfare_aggregate)
        
    return ah_lst, Eh_lst, El_lst, E_lst, CS_capita_lst, CS_aggregate_lst, pil_lst, pih_lst, pi_aggregate_lst, welfare_aggregate_lst

def plot_welfare_ex_post(al, kl, kh, T, P, N, N2):
    ah_lst = np.linspace(41, 99, N2)
    
    Eh_lst = []
    El_lst = []
    E_lst = []
    CS_capita_lst = []
    CS_capita_adjusted_lst = []
    CS_aggregate_lst = []
    CS_aggregate_adjusted_lst = []
    pil_lst = []
    pih_lst = []
    pi_aggregate_lst = []
    welfare_aggregate_lst = []
    welfare_aggregate_adjusted_lst = []

    
    for ah in ah_lst:
        Fh, Fl, p, b = CDF_dis_ex_post(al, ah, kl, kh, T, P, N)
        Eh, El, E, CS_capita, CS_capita_adjusted, CS_aggregate, CS_aggregate_adjusted, pil, pih, pi_aggregate, welfare_aggregate, welfare_aggregate_adjusted = welfare_ex_post(Fh, Fl, p, al, ah, T, kl, kh, P)
        Eh_lst.append(Eh)
        El_lst.append(El)
        E_lst.append(E)
        CS_capita_lst.append(CS_capita)
        CS_capita_adjusted_lst.append(CS_capita_adjusted)
        CS_aggregate_lst.append(CS_aggregate)
        CS_aggregate_adjusted_lst.append(CS_aggregate_adjusted)
        pil_lst.append(pil)
        pih_lst.append(pih)
        pi_aggregate_lst.append(pi_aggregate)
        welfare_aggregate_lst.append(welfare_aggregate)
        welfare_aggregate_adjusted_lst.append(welfare_aggregate_adjusted)
        
    return ah_lst, Eh_lst, El_lst, E_lst, CS_capita_lst, CS_capita_adjusted_lst, CS_aggregate_lst, CS_aggregate_adjusted_lst, pil_lst, pih_lst, pi_aggregate_lst, welfare_aggregate_lst, welfare_aggregate_adjusted_lst

if __name__=='__main__': 
    
    #Colors
    '''
    colors = {
        "charcoal": "#264653ff",
        "persian-green": "#2a9d8fff",
        "orange-yellow-crayola": "#e9c46aff",
        "sandy-brown": "#f4a261ff",
        "burnt-sienna": "#e76f51ff"}
    '''
    colors = {
        "c": "#264653ff",
        "p-g": "#2a9d8fff",
        "o-y-c": "#e9c46aff",
        "s-b": "#f4a261ff",
        "b-s": "#e76f51ff"}
        
    #Parameters
    al = 15
    ah = 50
    kl = 60
    kh = 60
    T = 40
    P = 7
    N = 100
    N2 = 400


    ####################################
    ### Discriminatory price auction ###
    ####################################
    

    ##Call the functions
    #Determine the area
    area, area_num = determine_area(al, ah)
    #d_strategies_nodal
    Fh_nodal, Fl_nodal, p_nodal, b_nodal = CDF_dis_ex_ante(al, ah, kl, kh, T, P, N)
    Eh_nodal, El_nodal, E_nodal, CS_capita_nodal, CS_aggregate_nodal, pil_nodal, pih_nodal, pi_aggregate_nodal, welfare_aggregate_nodal = welfare_ex_ante(Fh_nodal, Fl_nodal, p_nodal, al, ah, T, kl, kh, P) 
    #d_strategies_zonal
    Fh_zonal, Fl_zonal, p_zonal, b_zonal = CDF_dis_ex_post(al, ah, kl, kh, T, P, N)
    Eh_zonal, El_zonal, E_zonal, CS_capita_zonal, CS_capita_adjusted_zonal, CS_aggregate_zonal, CS_aggregate_adjusted_zonal, pil_zonal, pih_zonal, pi_aggregate_zonal, welfare_aggregate_zonal, welfare_aggregate_adjusted_zonal = welfare_ex_post(Fh_zonal, Fl_zonal, p_zonal, al, ah, T, kl, kh, P) 
    #Welfare nodal
    ah_lst_nodal, Eh_lst_nodal, El_lst_nodal, E_lst_nodal, CS_capita_lst_nodal, CS_aggregate_lst_nodal, pil_lst_nodal, pih_lst_nodal, pi_aggregate_lst_nodal, welfare_aggregate_lst_nodal = plot_welfare_ex_ante(al, kl, kh, T, P, N, N2)
    #Welfare zonal
    ah_lst_zonal, Eh_lst_zonal, El_lst_zonal, E_lst_zonal, CS_capita_lst_zonal, CS_capita_adjusted_lst_zonal, CS_aggregate_lst_zonal, CS_aggregate_adjusted_lst_zonal, pil_lst_zonal, pih_lst_zonal, pi_aggregate_lst_zonal, welfare_aggregate_lst_zonal, welfare_aggregate_adjusted_lst_zonal = plot_welfare_ex_post(al, kl, kh, T, P, N, N2)
    
    #####################################################
    ### Discriminatory price auction: nodal vs. zonal ###
    #####################################################  
    ##Plot the functions
    import matplotlib.pyplot as plt
    
    #d_strategies paper
    fig, ax = plt.subplots(ncols = 3, figsize = (20, 9))
    #Axes1. no
    ax[0].plot(p_nodal, Fh_nodal, label = 'Fh_nodal',  color = colors["c"])
    ax[0].plot(p_nodal, Fl_nodal, label = 'Fl_nodal', color = colors["p-g"])
    ax[0].plot([Eh_nodal,Eh_nodal], [0,1], label = 'Eh_nodal',  color = colors["c"])
    ax[0].plot([El_nodal,El_nodal], [0,1], label = 'El_nodal', color = colors["p-g"])
    ax[0].plot([E_nodal,E_nodal], [0,1], label = 'E_nodal', color = colors["o-y-c"])
    ax[0].text(4.55, 0.8, "$F_h^{no}(b)$", fontsize=18)
    ax[0].text(4.55, 0.95, "$F_l^{no}(b)$", fontsize=18)
    ax[0].text(1.25, 1.01, "$E_l^{no}$", fontsize=18)
    ax[0].text(2.2, 1.01, "$E^{no}$", fontsize=18)
    ax[0].text(2.9, 1.01, "$E_h^{no}$", fontsize=18)
    ax[0].set_ylim(0, 1.1)
    ax[0].set(xticks=[0, b_nodal, P], xticklabels=['0', '${b}^{no}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[0].set_ylabel('$\\theta_h$', fontsize=18)
    ax[0].set_xlabel('$\\theta_l$', fontsize=18)
    ax[0].set_title('strategies nodal', fontsize=20)
    #Axes2. no vs. zo
    ax[1].plot(p_nodal, Fh_nodal, label = 'Fh_nodal',  color = colors["c"])
    ax[1].plot(p_nodal, Fl_nodal, label = 'Fl_nodal', color = colors["p-g"])
    ax[1].plot([Eh_nodal,Eh_nodal], [0,1], label = 'Eh_nodal',  color = colors["c"])
    ax[1].plot([El_nodal,El_nodal], [0,1], label = 'El_nodal', color = colors["p-g"])
    ax[1].plot([E_nodal,E_nodal], [0,1], label = 'E_nodal', color = colors["o-y-c"])
    ax[1].text(4.55, 0.8, "$F_h^{no}(b)$", fontsize=18)
    ax[1].text(4.55, 0.95, "$F_l^{no}(b)$", fontsize=18)
    ax[1].text(1.25, 1.01, "$E_l^{no}$", fontsize=18)
    ax[1].text(2.2, 1.01, "$E^{no}$", fontsize=18)
    ax[1].text(2.9, 1.01, "$E_h^{no}$", fontsize=18)
        
    ax[1].plot(p_zonal, Fh_zonal, label = 'Fh_zonal',  color = colors["c"], alpha=0.3)
    ax[1].plot(p_zonal, Fl_zonal, label = 'Fl_zonal', color = colors["p-g"], alpha=0.3)
    ax[1].plot([Eh_zonal,Eh_zonal], [0,1], label = 'Eh_zonal',  color = colors["c"], alpha=0.3)
    ax[1].plot([El_zonal,El_zonal], [0,1], label = 'El_zonal', color = colors["p-g"], alpha=0.3)
    ax[1].plot([E_zonal,E_zonal], [0,1], label = 'E_zonal', color = colors["o-y-c"], alpha=0.3)
    ax[1].set_ylim(0, 1.1)
    ax[1].set(xticks=[0, b_nodal, b_zonal, P], xticklabels=['0', '${b}^{no}$', '${b}^{zo}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[1].set_ylabel('$\\theta_h$', fontsize=18)
    ax[1].set_xlabel('$\\theta_l$', fontsize=18)
    ax[1].set_title('strategies nodal vs. zonal', fontsize=20)
    #Axes3. zo
    ax[2].plot(p_zonal, Fh_zonal, label = 'Fh_zonal',  color = colors["c"], alpha=0.3)
    ax[2].plot(p_zonal, Fl_zonal, label = 'Fl_zonal', color = colors["p-g"], alpha=0.3)
    ax[2].plot([Eh_zonal,Eh_zonal], [0,1], label = 'Eh_zonal',  color = colors["c"], alpha=0.3)
    ax[2].plot([El_zonal,El_zonal], [0,1], label = 'El_zonal', color = colors["p-g"], alpha=0.3)
    ax[2].plot([E_zonal,E_zonal], [0,1], label = 'E_zonal', color = colors["o-y-c"], alpha=0.3)
    ax[2].text(4.55+1.2, 0.75, "$F_h^{zo}(b)$", fontsize=18, alpha=1)
    ax[2].text(4.55+1.2, 1.01, "$F_l^{zo}(b)$", fontsize=18, alpha=1)
    ax[2].text(1.25+1.2, 1.01, "$E_l^{zo}$", fontsize=18, alpha=1)
    ax[2].text(2.2+1.2, 1.01, "$E^{zo}$", fontsize=18, alpha=1)
    ax[2].text(2.9+1.2, 1.01, "$E_h^{zo}$", fontsize=18, alpha=1)
    ax[2].set_ylim(0, 1.1)
    ax[2].set(xticks=[0, b_zonal, P], xticklabels=['0', '${b}^{zo}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax[2].set_ylabel('$\\theta_h$', fontsize=18)
    ax[2].set_xlabel('$\\theta_l$', fontsize=18)
    ax[2].set_title('strategies zonal', fontsize=20)
    plt.show()
    
    #d_welfare paper
    fig, ax = plt.subplots(ncols = 4, figsize = (20, 9))
    #Axes1. E
    ax[0].plot(ah_lst_nodal, Eh_lst_nodal, label = 'Eh_lst_nodal', color = colors["c"], alpha=1)
    ax[0].plot(ah_lst_nodal, El_lst_nodal, label = 'El_lst_nodal', color = colors["p-g"], alpha=1)
    ax[0].plot(ah_lst_nodal, E_lst_nodal, label = 'E_lst_nodal', color = colors["o-y-c"], alpha=1) 
    ax[0].plot(ah_lst_zonal, Eh_lst_zonal, label = 'Eh_lst_zonal', color = colors["c"], alpha=0.3)
    ax[0].plot(ah_lst_zonal, El_lst_zonal, label = 'El_lst_zonal', color = colors["p-g"], alpha=0.3)
    ax[0].plot(ah_lst_zonal, E_lst_zonal, label = 'E_lst_zonal', color = colors["o-y-c"], alpha=0.3)
    
    ax[0].text(40, 1.4, "$E^{no}$", fontsize=18)
    ax[0].text(40, 0.78, "$E_h^{no}$", fontsize=18)
    ax[0].text(40, 2.5, "$E_l^{no}$", fontsize=18)

    ax[0].set_ylim(0.75, 7.5)
    ax[0].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[1, 7], yticklabels=['1', 'P'])
    ax[0].set_xlabel('$\\theta_h$', fontsize=18)
    ax[0].set_ylabel('expected price', fontsize=18)
    ax[0].yaxis.set_label_coords(-0.02, 0.5)
    ax[0].set_title('expected price no vs. zo', fontsize=20)
    #Axes2. CS_adjusted
    ax[1].plot(ah_lst_nodal, CS_aggregate_lst_nodal, label = 'CS_aggregate_lst_nodal', color = colors["b-s"], alpha=1)
    ax[1].plot(ah_lst_nodal, CS_aggregate_lst_nodal, label = 'CS_aggregate_lst_nodal', color = colors["c"], alpha=1)
    ax[1].plot(ah_lst_zonal, CS_aggregate_adjusted_lst_zonal, label = 'CS_aggregate_adjusted_lst_zonal', color = colors["b-s"], alpha=0.3)
    ax[1].plot(ah_lst_zonal, CS_aggregate_lst_zonal, label = 'CS_aggregate_lst_zonal', color = colors["c"], alpha=0.3)
    
    ax[1].text(75, 150, "$CS^{no}$", fontsize=18)
    ax[1].text(43, 150, "$CS_{adjusted}^{no}$", fontsize=18)
    
    ax[1].set_ylim(0, 350)
    ax[1].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[0, 350], yticklabels=['0', '350'])
    ax[1].set_xlabel('$\\theta_h$', fontsize=18)
    ax[1].set_ylabel('CS adjusted', fontsize=18)
    ax[1].yaxis.set_label_coords(-0.02, 0.5)
    ax[1].set_title('CS adjusted no vs. zo', fontsize=20)
    #Axes3. profits
    ax[2].plot(ah_lst_nodal, pih_lst_nodal, label = 'pih_lst_nodal', color = colors["c"], alpha=1)
    ax[2].plot(ah_lst_nodal, pil_lst_nodal, label = 'pil_lst_nodal', color = colors["p-g"], alpha=1)
    #ax[2].plot(ah_lst_zonal, pih_lst_zonal, label = 'pih_lst_zonal', color = colors["c"], alpha=0.3)
    ax[2].plot(ah_lst_zonal, pil_lst_zonal, label = 'pil_lst_zonal', color = colors["p-g"], alpha=0.3)
    
    ax[2].text(70, 140, "$\pi_l^{no}$", fontsize=18)
    ax[2].text(50, 140, "$\pi_h^{no}$", fontsize=18)
    
    ax[2].set_ylim(0, 420)
    ax[2].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[0, 420], yticklabels=['0', '420'])
    ax[2].set_xlabel('$\\theta_h$', fontsize=18)
    ax[2].set_ylabel('profits', fontsize=18)
    ax[2].yaxis.set_label_coords(-0.02, 0.5)
    ax[2].set_title('profits no vs. zo', fontsize=20)
    #Axes4. welfare
    ax[3].plot(ah_lst_nodal, welfare_aggregate_lst_nodal, label = 'CS_aggregate_lst_nodal', color = colors["b-s"], alpha=1)
    ax[3].plot(ah_lst_nodal, welfare_aggregate_lst_nodal, label = 'CS_aggregate_lst_nodal', color = colors["c"], alpha=1)
    ax[3].plot(ah_lst_zonal, welfare_aggregate_adjusted_lst_zonal, label = 'CS_aggregate_adjusted_lst_zonal', color = colors["b-s"], alpha=0.3)
    ax[3].plot(ah_lst_zonal, welfare_aggregate_lst_zonal, label = 'CS_aggregate_lst_zonal', color = colors["c"], alpha=0.3)
    
    ax[3].text(43, 500, "$welfare^{no}$", fontsize=18)
    ax[3].text(65, 440, "$welfare_{adjusted}^{no}$", fontsize=18)
    
    ax[3].set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[250, 800], yticklabels=['250', '800'])
    ax[3].set_xlabel('$\\theta_h$', fontsize=18)
    ax[3].set_ylabel('welfare adjusted', fontsize=18)
    ax[3].yaxis.set_label_coords(-0.02, 0.5)
    ax[3].set_title('welfare adjusted no vs. zo', fontsize=20)
    plt.show()
    
    
    #Strategies (presentation)
    fig, ax = plt.subplots(figsize = (20, 9))
    ax.plot(p_nodal, Fh_nodal, color = colors["c"])
    ax.plot(p_nodal, Fl_nodal, color = colors["p-g"])
    ax.plot([Eh_nodal,Eh_nodal], [0,1],  color = colors["c"])
    ax.plot([El_nodal,El_nodal], [0,1],  color = colors["p-g"])
    ax.plot([E_nodal,E_nodal], [0,1],  color = colors["o-y-c"])
    ax.text(4.55, 0.85, "$F_h^{no}(b)$", fontsize=18)
    ax.text(6.5, 1.01, "$F_l^{no}(b)$", fontsize=18)
    ax.text(El_nodal-0.05, 1.01, "$E_l^{no}$", fontsize=18)
    ax.text(E_nodal-0.05, 1.01, "$E^{no}$", fontsize=18)
    ax.text(Eh_nodal+0.05, 1.01, "$E_h^{no}$", fontsize=18)
        
    ax.plot(p_zonal, Fh_zonal,  color = colors["c"], alpha=0.3)
    ax.plot(p_zonal, Fl_zonal,  color = colors["p-g"], alpha=0.3)
    ax.plot([Eh_zonal,Eh_zonal], [0,1],  color = colors["c"], alpha=0.3)
    ax.plot([El_zonal,El_zonal], [0,1],  color = colors["p-g"], alpha=0.3)
    ax.plot([E_zonal,E_zonal], [0,1],  color = colors["o-y-c"], alpha=0.3)
    ax.set_ylim(0, 1.1)
    ax.set(xticks=[0, b_nodal, b_zonal, P], xticklabels=['0', '${b}^{no}$', '${b}^{zo}$', 'P'],
              yticks=[0, 1], yticklabels=['0', '1'])
    ax.set_ylabel('$CDF$', fontsize=18)
    ax.yaxis.set_label_coords(-0.01, 0.5)
    ax.set_xlabel('$price$', fontsize=18)
    ax.set_title('strategies nodal vs. zonal ($\\theta_l=15$, $\\theta_h=50$, $k_l=k_h=60$, $T=40$)', fontsize=20)
    
    #CS adjusted (presentation)
    fig, ax = plt.subplots(figsize = (20, 9))
    ax.plot(ah_lst_nodal, CS_aggregate_lst_nodal, color = colors["b-s"], alpha=1)
    ax.plot(ah_lst_zonal, CS_aggregate_adjusted_lst_zonal, color = colors["b-s"], alpha=0.3)
    ax.plot([ah,ah], [0,370], label = 'ah',  color = colors["c"], alpha=0.3)
    ax.text(ah+0.5, 320, "$\\theta_h$", fontsize=18)
    ax.text(75, 150, "$CS^{nodal}$", fontsize=18)
    ax.text(63, 150, "$CS_{adjusted}^{zonal}$", fontsize=18)
    ax.set_ylim(0, 370)
    ax.set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[0, 370], yticklabels=['0', '370'])
    ax.set_xlabel('$\\theta_h$', fontsize=18)
    ax.set_ylabel('CS adjusted zonal vs. CS nodal', fontsize=18)
    ax.yaxis.set_label_coords(-0.01, 0.5)
    ax.set_title('CS adjusted zonal vs. CS nodal ($\\theta_l=15$, $\\theta_h=50$, $k_l=k_h=60$, $T=40$)', fontsize=20)
    
    #pil, pih (presentation)
    fig, ax = plt.subplots(figsize = (20, 9))
    ax.plot(ah_lst_nodal, pil_lst_nodal, color = colors["o-y-c"], alpha=1)
    ax.plot(ah_lst_zonal, pil_lst_zonal, color = colors["o-y-c"], alpha=0.3)
    ax.plot([ah,ah], [0,370], label = 'ah',  color = colors["c"], alpha=0.3)
    ax.text(ah+0.5, 320, "$\\theta_h$", fontsize=18)
    ax.text(75, 200, "$\pi_l^{nodal}$", fontsize=18)
    ax.text(58, 150, "$\pi_l^{zonal}$", fontsize=18)
    ax.set_ylim(0, 370)
    ax.set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[0, 370], yticklabels=['0', '370'])
    ax.set_xlabel('$\\theta_h$', fontsize=18)
    ax.set_ylabel('$\pi_l^{zonal}$ vs. $\pi_l^{nodal}$', fontsize=18)
    ax.yaxis.set_label_coords(-0.01, 0.5)
    ax.set_title('$\pi_l^{zonal}$ vs. $\pi_l^{nodal}$ ($\\theta_l=15$, $\\theta_h=50$, $k_l=k_h=60$, $T=40$)', fontsize=20)
    
    #welfare adjusted (presentation)
    fig, ax = plt.subplots(figsize = (20, 9))
    ax.plot(ah_lst_nodal, welfare_aggregate_lst_nodal,  color = colors["p-g"], alpha=1)
    ax.plot(ah_lst_zonal, welfare_aggregate_adjusted_lst_zonal,  color = colors["p-g"], alpha=0.3)
    ax.plot([ah,ah], [0,800], label = 'ah',  color = colors["c"], alpha=0.3)
    ax.text(ah+0.5, 750, "$\\theta_h$", fontsize=18)
    ax.text(62, 550, "$welfare^{nodal}$", fontsize=18)
    ax.text(77, 600, "$welfare_{adjusted}^{zonal}$", fontsize=18)
    ax.set_ylim(350, 820)
    ax.set(xticks=[41, 70, 99], xticklabels=['41', '70', '99'],
              yticks=[350, 820], yticklabels=['350', '820'])
    ax.set_xlabel('$\\theta_h$', fontsize=18)
    ax.set_ylabel('welfare adjusted zonal vs. welfare nodal', fontsize=18)
    ax.yaxis.set_label_coords(-0.01, 0.5)
    ax.set_title('welfare adjusted zonal vs. welfare nodal ($\\theta_l=15$, $\\theta_h=50$, $k_l=k_h=60$, $T=40$)', fontsize=20)
   
    #Heatcolor map
    N2 = 100
    ah_lst = np.linspace(99, 41, N2)
    al_lst = np.linspace(1, 19, N2)
    
    #Initialize no
    El_lst_no = []
    Eh_lst_no = []
    E_lst_no = []
    CS_aggregate_lst_no = []
    pil_lst_no = []
    pih_lst_no = []
    pi_aggregate_lst_no = []
    welfare_aggregate_lst_no = []
    
    #Initialize zo
    El_lst_zo = []
    Eh_lst_zo = []
    E_lst_zo = []
    CS_aggregate_adjusted_lst_zo = []
    pil_lst_zo = []
    pih_lst_zo = []
    pi_aggregate_lst_zo = []
    welfare_aggregate_adjusted_lst_zo = []

    for ah in ah_lst:
            
        #temp_lst_no = []
        temp_El_lst_no = []
        temp_Eh_lst_no = []
        temp_E_lst_no = []
        temp_CS_aggregate_lst_no = []
        temp_pil_lst_no = []
        temp_pih_lst_no = []
        temp_pi_aggregate_lst_no = []
        temp_welfare_aggregate_lst_no = []
        
        #temp_lst_zo = []
        temp_El_lst_zo = []
        temp_Eh_lst_zo = []
        temp_E_lst_zo = []
        temp_CS_aggregate_adjusted_lst_zo = []
        temp_pil_lst_zo = []
        temp_pih_lst_zo = []
        temp_pi_aggregate_lst_zo = []
        temp_welfare_aggregate_adjusted_lst_zo = []
      
        for al in al_lst:
            Eh_no, El_no, E_no, CS_capita_no, CS_aggregate_no, pil_no, pih_no, pi_aggregate_no, welfare_aggregate_no = d_simulate_model(al, ah, kl, kh, T, P, N, model = 'no', auction='discriminatory')
            Eh_zo, El_zo, E_zo, CS_capita_zo, CS_capita_adjusted_zo, CS_aggregate_zo, CS_aggregate_adjusted_zo, pil_zo, pih_zo, pi_aggregate_zo, welfare_aggregate_zo, welfare_aggregate_adjusted_zo = d_simulate_model(al, ah, kl, kh, T, P, N, model = 'zo', auction='discriminatory')
            
            #Append no
            temp_El_lst_no.append(El_no)
            temp_Eh_lst_no.append(Eh_no)
            temp_E_lst_no.append(E_no)
            temp_CS_aggregate_lst_no.append(CS_aggregate_no)
            temp_pil_lst_no.append(pil_no)
            temp_pih_lst_no.append(pih_no)
            temp_pi_aggregate_lst_no.append(pi_aggregate_no)
            temp_welfare_aggregate_lst_no.append(welfare_aggregate_no)
            
            #Append zo
            temp_El_lst_zo.append(El_zo)
            temp_Eh_lst_zo.append(Eh_zo)
            temp_E_lst_zo.append(E_zo)
            temp_CS_aggregate_adjusted_lst_zo.append(CS_aggregate_adjusted_zo)
            temp_pil_lst_zo.append(pil_zo)
            temp_pih_lst_zo.append(pih_zo)
            temp_pi_aggregate_lst_zo.append(pi_aggregate_zo)
            temp_welfare_aggregate_adjusted_lst_zo.append(welfare_aggregate_adjusted_zo)
            
        #Append lst_no
        El_lst_no.append(temp_El_lst_no)
        Eh_lst_no.append(temp_Eh_lst_no)
        E_lst_no.append(temp_E_lst_no)
        CS_aggregate_lst_no.append(temp_CS_aggregate_lst_no)
        pil_lst_no.append(temp_pil_lst_no)
        pih_lst_no.append(temp_pih_lst_no)
        pi_aggregate_lst_no.append(temp_pi_aggregate_lst_no)
        welfare_aggregate_lst_no.append(temp_welfare_aggregate_lst_no)
        
        #Append lst_zo
        El_lst_zo.append(temp_El_lst_zo)
        Eh_lst_zo.append(temp_Eh_lst_zo)
        E_lst_zo.append(temp_E_lst_zo)
        CS_aggregate_adjusted_lst_zo.append(temp_CS_aggregate_adjusted_lst_zo)
        pil_lst_zo.append(temp_pil_lst_zo)
        pih_lst_zo.append(temp_pih_lst_zo)
        pi_aggregate_lst_zo.append(temp_pi_aggregate_lst_zo)
        welfare_aggregate_adjusted_lst_zo.append(temp_welfare_aggregate_adjusted_lst_zo)
    
    #Array no
    El_array_no = np.array(El_lst_no)
    Eh_array_no = np.array(Eh_lst_no)
    E_array_no = np.array(E_lst_no)
    CS_aggregate_array_no = np.array(CS_aggregate_lst_no)
    pil_array_no = np.array(pil_lst_no)
    pih_array_no = np.array(pih_lst_no)
    pi_aggregate_array_no = np.array(pi_aggregate_lst_no)
    welfare_aggregate_array_no = np.array(welfare_aggregate_lst_no)
    
    #Array zo
    El_array_zo = np.array(El_lst_zo)
    Eh_array_zo = np.array(Eh_lst_zo)
    E_array_zo = np.array(E_lst_zo)
    CS_aggregate_adjusted_array_zo = np.array(CS_aggregate_adjusted_lst_zo)
    pil_array_zo = np.array(pil_lst_zo)
    pih_array_zo = np.array(pih_lst_zo)
    pi_aggregate_array_zo = np.array(pi_aggregate_lst_zo)
    welfare_aggregate_adjusted_array_zo = np.array(welfare_aggregate_adjusted_lst_zo)
    
    #Array diff
    El_diff = El_array_no - El_array_zo
    Eh__diff = Eh_array_no - Eh_array_zo
    E_diff = E_array_no -E_array_zo
    #CS. Prior belief: CS_no>CS_zo
    CS_aggregate_adjusted_diff = CS_aggregate_array_no - CS_aggregate_adjusted_array_zo
    pil_diff = pil_array_no - pil_array_zo
    pih_diff = pih_array_no - pih_array_zo
    #pi. Prior belief: pi_no>pi_zo
    pi_aggregate_diff = pi_aggregate_array_no - pi_aggregate_array_zo
    #welfare. Prior belief: welfare_no>welfare_zo
    welfare_aggregate_adjusted_diff = welfare_aggregate_array_no - welfare_aggregate_adjusted_array_zo
   
    #Heat color CS
    fig, ax = plt.subplots(figsize = (20, 9))
    vmin_CS =  CS_aggregate_adjusted_diff.min()
    vmax_CS =  CS_aggregate_adjusted_diff.max()
    c1 = ax.pcolormesh(al_lst, ah_lst, CS_aggregate_adjusted_diff, cmap = 'viridis', vmin = vmin_CS, vmax = vmax_CS)
    ax.set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax.set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax.set_ylabel('$\\theta_h$', fontsize=18)
    ax.set_xlabel('$\\theta_l$', fontsize=18)
    ax.set_title('CS (nodal-zonal)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c1, cax=cbar_ax)
    
    #Heat color pil
    fig, ax = plt.subplots(figsize = (20, 9))
    vmin_pil =  pil_diff.min()
    vmax_pil =  pil_diff.max()
    c1 = ax.pcolormesh(al_lst, ah_lst, pil_diff, cmap = 'viridis', vmin = vmin_pil, vmax = vmax_pil)
    ax.set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax.set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax.set_ylabel('$\\theta_h$', fontsize=18)
    ax.set_xlabel('$\\theta_l$', fontsize=18)
    ax.set_title('$\\pi_l$ (nodal-zonal)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c1, cax=cbar_ax)
    
    #Heat color pih
    fig, ax = plt.subplots(figsize = (20, 9))
    vmin_pih =  pih_diff.min()
    vmax_pih =  pih_diff.max()
    c1 = ax.pcolormesh(al_lst, ah_lst, pih_diff, cmap = 'viridis', vmin = vmin_pil, vmax = vmax_pil)
    ax.set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax.set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax.set_ylabel('$\\theta_h$', fontsize=18)
    ax.set_xlabel('$\\theta_l$', fontsize=18)
    ax.set_title('$\\pi_h$ (nodal-zonal)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c1, cax=cbar_ax)
    
    #Heat color welfare 
    fig, ax = plt.subplots(figsize = (20, 9))
    vmin_w =  welfare_aggregate_adjusted_diff.min()
    vmax_w =  welfare_aggregate_adjusted_diff.max()
    c1 = ax.pcolormesh(al_lst, ah_lst, welfare_aggregate_adjusted_diff, cmap = 'viridis', vmin = vmin_w, vmax = vmax_w)
    ax.set_position([0.05+(0.85/4)*1, 0.15, 0.15, 0.7])
    ax.set(xticks=[1, 5, 10, 15, 19], xticklabels=['1', '5', '10', '15', '19'],
              yticks=[41, 50, 60, 70, 80, 90, 99], yticklabels=['41', '50', '60', '70', '80', '90', '99'])
    ax.set_ylabel('$\\theta_h$', fontsize=18)
    ax.set_xlabel('$\\theta_l$', fontsize=18)
    ax.set_title('welfare (nodal-zonal)', fontsize=20)
    cbar_ax = fig.add_axes([0.05+(0.85/4)*1+(0.15)+0.01, 0.15, 0.01, 0.7])
    fig.colorbar(c1, cax=cbar_ax)