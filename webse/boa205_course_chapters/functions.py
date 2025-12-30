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


def ch2a_selv(endring_varer_i_arbeid_102, endring_ferdige_varer_101):
    im_102_s=10500
    im_103_s=6750
    im_104_s=3000
    im_sum_s=20250
    dm_s=im_sum_s-20000
    il1_102_s=30000
    il1_103_s=12500
    il1_104_s=5500
    il1_sum_s=48000
    dl1_s=il1_sum_s-50000
    il2_102_s=60500
    il2_103_s=19800
    il2_104_s=8800
    il2_sum_s=89100
    dl2_s=il2_sum_s-95000
    kalkulert_tilv_102_s=70000+60000+55000+im_102_s+il1_102_s+il2_102_s
    kalkulert_tilv_103_s=45000+25000+18000+im_103_s+il1_103_s+il2_103_s
    kalkulert_tilv_104_s=20000+11000+8000+im_104_s+il1_104_s+il2_104_s
    kalkulert_tilv_sum_s=135000+96000+81000+im_sum_s+il1_sum_s+il2_sum_s
    kalkulert_tilv_ferdig_102_s=kalkulert_tilv_102_s+int(endring_varer_i_arbeid_102)
    kalkulert_tilv_ferdig_103_s=kalkulert_tilv_103_s
    kalkulert_tilv_ferdig_104_s=kalkulert_tilv_104_s
    kalkulert_tilv_ferdig_sum_s=kalkulert_tilv_sum_s+int(endring_varer_i_arbeid_102)
    kalkulert_tilv_ferdig_virkelige_s=477000+int(endring_varer_i_arbeid_102)
    endring_ferdige_varer_s=int(endring_ferdige_varer_101)-kalkulert_tilv_ferdig_104_s
    kalkulert_tilv_solgte_101_s=int(endring_ferdige_varer_101)
    kalkulert_tilv_solgte_102_s=kalkulert_tilv_ferdig_102_s
    kalkulert_tilv_solgte_103_s=kalkulert_tilv_ferdig_103_s
    kalkulert_tilv_solgte_104_s=0
    kalkulert_tilv_solgte_sum_s=kalkulert_tilv_solgte_101_s+kalkulert_tilv_solgte_102_s+kalkulert_tilv_solgte_103_s+kalkulert_tilv_solgte_104_s
    kalkulert_tilv_solgte_virkelige_s=kalkulert_tilv_ferdig_virkelige_s+endring_ferdige_varer_s
    salgs_adm_101_s=int(kalkulert_tilv_solgte_101_s*0.098)
    salgs_adm_102_s=int(kalkulert_tilv_solgte_102_s*0.098)
    salgs_adm_103_s=int(kalkulert_tilv_solgte_103_s*0.098)
    salgs_adm_104_s=int(kalkulert_tilv_solgte_104_s*0.098)
    salgs_adm_sum_s=int(kalkulert_tilv_solgte_sum_s*0.098)
    d_salgs_adm_s=salgs_adm_sum_s-50000
    kalkulert_selvkost_101_s=kalkulert_tilv_solgte_101_s+salgs_adm_101_s
    kalkulert_selvkost_102_s=kalkulert_tilv_solgte_102_s+salgs_adm_102_s
    kalkulert_selvkost_103_s=kalkulert_tilv_solgte_103_s+salgs_adm_103_s
    kalkulert_selvkost_104_s=kalkulert_tilv_solgte_104_s+salgs_adm_104_s
    kalkulert_selvkost_sum_s=kalkulert_tilv_solgte_sum_s+salgs_adm_sum_s
    kalkulert_selvkost_virkelige_s=kalkulert_tilv_solgte_virkelige_s+50000
    produktresultat_101_s=150000-kalkulert_selvkost_101_s
    produktresultat_102_s=290000-kalkulert_selvkost_102_s
    produktresultat_103_s=130000-kalkulert_selvkost_103_s
    produktresultat_104_s=0-kalkulert_selvkost_104_s
    produktresultat_sum_s=produktresultat_101_s+produktresultat_102_s+produktresultat_103_s
    d_sum_s=dm_s+dl1_s+dl2_s+d_salgs_adm_s
    produksjonresultat_s=produktresultat_sum_s+d_sum_s
    produksjonresultat_virkelige_s=570000-kalkulert_selvkost_virkelige_s
    return(im_102_s,im_103_s,im_104_s,im_sum_s,dm_s,il1_102_s,il1_103_s,il1_104_s,il1_sum_s,dl1_s,il2_102_s,il2_103_s,il2_104_s,il2_sum_s,
           dl2_s,kalkulert_tilv_102_s,kalkulert_tilv_103_s,kalkulert_tilv_104_s,kalkulert_tilv_sum_s,
           kalkulert_tilv_ferdig_102_s,kalkulert_tilv_ferdig_103_s,kalkulert_tilv_ferdig_104_s,kalkulert_tilv_ferdig_sum_s,
           kalkulert_tilv_ferdig_virkelige_s,endring_ferdige_varer_s,
           kalkulert_tilv_solgte_101_s,kalkulert_tilv_solgte_102_s,kalkulert_tilv_solgte_103_s,
           kalkulert_tilv_solgte_104_s,kalkulert_tilv_solgte_sum_s,kalkulert_tilv_solgte_virkelige_s,
           salgs_adm_101_s,salgs_adm_102_s,salgs_adm_103_s,salgs_adm_104_s,salgs_adm_sum_s,d_salgs_adm_s,
           kalkulert_selvkost_101_s,kalkulert_selvkost_102_s,kalkulert_selvkost_103_s,
           kalkulert_selvkost_104_s,kalkulert_selvkost_sum_s,kalkulert_selvkost_virkelige_s,
           produktresultat_101_s,produktresultat_102_s,produktresultat_103_s,produktresultat_104_s,
           produktresultat_sum_s,d_sum_s,produksjonresultat_s,produksjonresultat_virkelige_s)

def ch2a_bidra(endring_varer_i_arbeid_102, endring_ferdige_varer_101):
    im_102_b=3500
    im_103_b=2250
    im_104_b=1000
    im_sum_b=6750
    dm_b=im_sum_b-8000
    il1_102_b=12000
    il1_103_b=5000
    il1_104_b=2200
    il1_sum_b=19200
    dl1_b=il1_sum_b-20000
    il2_102_b=30250
    il2_103_b=9900
    il2_104_b=4400
    il2_sum_b=44550
    dl2_b=il2_sum_b-40000
    d_total_b=dm_b+dl1_b+dl2_b
    kalkulert_tilv_102_b=70000+60000+55000+im_102_b+il1_102_b+il2_102_b
    kalkulert_tilv_103_b=45000+25000+18000+im_103_b+il1_103_b+il2_103_b
    kalkulert_tilv_104_b=20000+11000+8000+im_104_b+il1_104_b+il2_104_b
    kalkulert_tilv_sum_b=135000+96000+81000+im_sum_b+il1_sum_b+il2_sum_b
    kalkulert_tilv_ferdig_102_b=kalkulert_tilv_102_b+int(endring_varer_i_arbeid_102)
    kalkulert_tilv_ferdig_103_b=kalkulert_tilv_103_b
    kalkulert_tilv_ferdig_104_b=kalkulert_tilv_104_b
    kalkulert_tilv_ferdig_sum_b=kalkulert_tilv_sum_b+int(endring_varer_i_arbeid_102)
    kalkulert_tilv_ferdig_virkelige_b=477000+int(endring_varer_i_arbeid_102)
    endring_ferdige_varer_b=int(endring_ferdige_varer_101)-kalkulert_tilv_ferdig_104_b
    kalkulert_tilv_solgte_101_b=int(endring_ferdige_varer_101)
    kalkulert_tilv_solgte_102_b=kalkulert_tilv_ferdig_102_b
    kalkulert_tilv_solgte_103_b=kalkulert_tilv_ferdig_103_b
    kalkulert_tilv_solgte_104_b=0
    kalkulert_tilv_solgte_sum_b=kalkulert_tilv_solgte_101_b+kalkulert_tilv_solgte_102_b+kalkulert_tilv_solgte_103_b+kalkulert_tilv_solgte_104_b
    kalkulert_tilv_solgte_virkelige_b=kalkulert_tilv_ferdig_virkelige_b+endring_ferdige_varer_b
    merkost_solgte_varer_101_b=kalkulert_tilv_solgte_101_b
    merkost_solgte_varer_102_b=kalkulert_tilv_solgte_102_b
    merkost_solgte_varer_103_b=kalkulert_tilv_solgte_103_b
    merkost_solgte_varer_104_b=kalkulert_tilv_solgte_104_b
    merkost_solgte_varer_sum_b=kalkulert_tilv_solgte_sum_b
    merkost_solgte_varer_virkelige_b=135000+96000+81000+8000+20000+40000+endring_ferdige_varer_b+int(endring_varer_i_arbeid_102)
    kalkulert_dekningsbidrag_101_b=150000-merkost_solgte_varer_101_b
    kalkulert_dekningsbidrag_102_b=290000-merkost_solgte_varer_102_b
    kalkulert_dekningsbidrag_103_b=130000-merkost_solgte_varer_103_b
    kalkulert_dekningsbidrag_104_b=0-merkost_solgte_varer_104_b
    kalkulert_dekningsbidrag_sum_b=570000-merkost_solgte_varer_sum_b
    virkelig_dekningsbidrag_b=kalkulert_dekningsbidrag_sum_b+d_total_b
    virkelig_dekningsbidrag_virkelige_b=570000-merkost_solgte_varer_virkelige_b
    produksjonresultat_virkelige_b=virkelig_dekningsbidrag_virkelige_b-12000-30000-55000-50000
    return(im_102_b,im_103_b,im_104_b,im_sum_b,dm_b,il1_102_b,il1_103_b,il1_104_b,il1_sum_b,dl1_b,il2_102_b,il2_103_b,il2_104_b,il2_sum_b,
           dl2_b,kalkulert_tilv_102_b,kalkulert_tilv_103_b,kalkulert_tilv_104_b,kalkulert_tilv_sum_b,
           kalkulert_tilv_ferdig_102_b,kalkulert_tilv_ferdig_103_b,kalkulert_tilv_ferdig_104_b,kalkulert_tilv_ferdig_sum_b,
           kalkulert_tilv_ferdig_virkelige_b,endring_ferdige_varer_b,
           kalkulert_tilv_solgte_101_b,kalkulert_tilv_solgte_102_b,kalkulert_tilv_solgte_103_b,
           kalkulert_tilv_solgte_104_b,kalkulert_tilv_solgte_sum_b,kalkulert_tilv_solgte_virkelige_b,
           merkost_solgte_varer_101_b,merkost_solgte_varer_102_b,merkost_solgte_varer_103_b,merkost_solgte_varer_104_b,
           merkost_solgte_varer_sum_b,merkost_solgte_varer_virkelige_b,kalkulert_dekningsbidrag_101_b,
           kalkulert_dekningsbidrag_102_b,kalkulert_dekningsbidrag_103_b,kalkulert_dekningsbidrag_104_b,
           kalkulert_dekningsbidrag_sum_b,d_total_b,virkelig_dekningsbidrag_b,virkelig_dekningsbidrag_virkelige_b,
           produksjonresultat_virkelige_b)
