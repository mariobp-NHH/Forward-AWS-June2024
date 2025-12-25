""" Chapter 2 """
def normal(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser):
    IVM= int(float(DM)*float(IVM_satser))
    IFM= int(float(DM)*float(IFM_satser))
    IVT= int(float(DL)*float(IVT_satser))
    IFT= int(float(DL)*float(IFT_satser))
    T= int(DM)+int(DL)+IVM+IFM+IVT+IFT
    IVA= int(T*float(IVA_satser))
    IFA= int(T*float(IFA_satser))
    selvkost=int(T+IVA+IFA)
    produktresultat=S-selvkost
    return(IVM, IFM,IVT,IFT,T,IVA,IFA,selvkost, produktresultat)

def virkelig(S,DM,DL):
    T= int(DM)+int(DL)+40000+30000+55000+20000
    selvkost=T+35000+30000
    produksjonresultat=int(S)-selvkost
    return(T,selvkost, produksjonresultat)

def dekningsdiff(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser):
    IVMn, IFMn,IVTn,IFTn,Tn,IVAn,IFAn,selvkost_n, produktresultat_n=normal(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser)
    Tv,selvkost_v, produksjonresultat_v=virkelig(S,DM,DL)
    IVMD=IVMn-40000
    IFMD=IFMn-30000
    IVTD=IVTn-55000
    IFTD=IFTn-20000
    IVAD=IVAn-35000
    IFAD=IFAn-30000
    dekningsdifferanser=IVMD+IFMD+IVTD+IFTD+IVAD+IFAD
    return(IVMD,IFMD,IVTD,IFTD,IVAD,IFAD,dekningsdifferanser,produktresultat_n)

def produksjonresultat_normal(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser):
    IVMD,IFMD,IVTD,IFTD,IVAD,IFAD,dekningsdifferanser,produktresultat_n=dekningsdiff(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser)
    produksjonresultat=produktresultat_n+dekningsdifferanser
    return(produksjonresultat)

def avvik(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser, FM_budsjett):
    IVMn, IFMn,IVTn,IFTn,Tn,IVAn,IFAn,selvkost_n, produktresultat_n=normal(S,DM,DL, IVM_satser, IFM_satser,IVT_satser, IFT_satser, IVA_satser, IFA_satser)
    forbruk_avvik_m_v=IVMn-40000
    volumn_avvik_m_f=IFMn-int(FM_budsjett)
    forbruk_avvik_m_f=int(FM_budsjett)-30000
    total_avvik_m_f=IFMn-30000
    return(IVMn,forbruk_avvik_m_v,volumn_avvik_m_f,forbruk_avvik_m_f,total_avvik_m_f)

""" Table 2 """
def produktresultat_selv(S,DM,DL, ITM_satser, ITT_satser, ITA_satser, varer, ferdig_varer):
    ITM= int(float(DM)*float(ITM_satser))
    ITT= int(float(DL)*float(ITT_satser))
    T= int(DM)+int(DL)+ITM+ITT
    T_ferdiger=T+int(varer)
    T_salgte=T_ferdiger-int(ferdig_varer)
    ITA= int(T_salgte*float(ITA_satser))
    selvkost=int(T_salgte+ITA)
    produktresultat=S-selvkost
    return(ITM,ITT,T, T_ferdiger, T_salgte, ITA,selvkost, produktresultat)

def virkelig_selv(S,DM,DL,varer, ferdig_varer):
    T= int(DM)+int(DL)+3500000+19500000
    T_ferdiger=T+int(varer)
    T_salgte=T_ferdiger-int(ferdig_varer)
    selvkost=T_salgte+6850000
    produksjonresultat=int(S)-selvkost
    return(T,T_ferdiger,T_salgte,selvkost, produksjonresultat)

def dekningsdiff_produksjonresultat_selv(S,DM,DL, ITM_satser, ITT_satser, ITA_satser, varer, ferdig_varer):
    ITM,ITT,T, T_ferdiger, T_salgte, ITA,selvkost, produktresultat=produktresultat_selv(S,DM,DL, ITM_satser, ITT_satser, ITA_satser, varer, ferdig_varer)
    T,T_ferdiger,T_salgte,selvkost, produksjonresultat = virkelig_selv(S,DM,DL,varer, ferdig_varer)
    DM=ITM-3500000
    DT=ITT-19500000
    DA=ITA-6850000
    D=DM+DT+DA
    produksjonresultat=produktresultat+D
    return(DM,DT,DA,D,produksjonresultat)

def produktresultat_bidra(S,DM,DL, IVM_satser, IFM_satser, IVT_satser, IFT_satser, IVA_satser, IFA_satser, varer, ferdig_varer):
    IVM= int(float(DM)*float(IVM_satser))
    IVT= int(float(DL)*float(IVT_satser))
    T= int(DM)+int(DL)+IVM+IVT
    T_ferdiger=int(T+int(varer))
    T_salgte=T_ferdiger-int(ferdig_varer)
    IVA=int(T_salgte*float(IVA_satser))
    salgmerkost=int(T_salgte+IVA)
    kalkulert_dekningsbidra=int(S-salgmerkost)
    """ Start Dekningsdiff """
    DVM=int(IVM-1000000)
    DVT=int(IVT-8000000)
    DVA=int(IVA-0)
    sumDV=int(DVM+DVT+DVA)
    """ End Dekningsdiff """
    virkelig_dekningsbidrag=int(kalkulert_dekningsbidra+sumDV)
    IFM= int(float(DM)*float(IFM_satser))
    IFT= int(float(DL)*float(IFT_satser))
    IFA= int(T_salgte*float(IFA_satser))
    """ Start Dekningsdiff """
    DFM= int(IFM-2500000)
    DFT= int(IFT-11500000)
    DFA= int(IFA-6850000)
    sumDF=int(DFM+DFT+DFA)
    """ End Dekningsdiff """
    produktresultat=int(virkelig_dekningsbidrag-IFM-IFT-IFA+sumDF)
    """ Virkelig """
    T_v=17000000+27000000+1000000+8000000
    T_ferdiger_v=int(T_v+int(varer))
    T_salgte_v=int(T_ferdiger_v-int(ferdig_varer))
    virkelig_dekningsbidrag_v=int(S-T_salgte_v)
    produktresultat_v=int(virkelig_dekningsbidrag_v-2500000-11500000-6850000)
    return(IVM, IVT,T,T_ferdiger, T_salgte,IVA,salgmerkost,kalkulert_dekningsbidra,
           DVM,DVT,DVA,sumDV,virkelig_dekningsbidrag,IFM,IFT,IFA,DFM,DFT,DFA,
           sumDF,produktresultat,T_v,T_ferdiger_v,T_salgte_v,virkelig_dekningsbidrag_v,produktresultat_v)

    