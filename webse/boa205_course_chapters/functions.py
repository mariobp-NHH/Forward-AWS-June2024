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

""" Chapter 3 """
def ch3_materialregnskap(pris_beholdning_1_januar,pris_innkjop_material_i_januar):
    beholdning_material_01_januar_kost= int(500*float(pris_beholdning_1_januar))
    innkjøp_material_i_januar_kost=int(700*float(pris_innkjop_material_i_januar))
    beholdning_material_31_januar_kost=int(600*float(pris_innkjop_material_i_januar))
    virkelig_forbruk_pris=round((int(500*float(pris_beholdning_1_januar))+int(100*float(pris_innkjop_material_i_januar)))/600,2)
    virkelig_forbruk_kost=int(600*virkelig_forbruk_pris)
    standard_kostnader=int(float(pris_beholdning_1_januar)*580)
    virkelig_forbruk= int(float(pris_beholdning_1_januar)*600)
    virkelig_kostnader= int(float(virkelig_forbruk_pris)*600)
    mengdeavvik=standard_kostnader-virkelig_forbruk
    prisavvik=virkelig_forbruk-virkelig_kostnader
    totalavvik=mengdeavvik+prisavvik
    return(beholdning_material_01_januar_kost,innkjøp_material_i_januar_kost,beholdning_material_31_januar_kost,
           virkelig_forbruk_pris,virkelig_forbruk_kost,standard_kostnader,virkelig_forbruk,virkelig_kostnader,
           mengdeavvik,prisavvik,totalavvik)

def ch3_lonnregnskap(standard_lonn, virkelig_timer):
    virkelig_lonn=round(float(264690/int(virkelig_timer)),2)
    standard_kostnader=870*int(standard_lonn)
    virkelig_forbruk=int(standard_lonn)*int(virkelig_timer)
    virkelige_kostnader=int(virkelig_lonn*int(virkelig_timer))
    tidsavvik=standard_kostnader-virkelig_forbruk
    lønnssatsavvik=virkelig_forbruk-virkelige_kostnader
    totalavvik=-(tidsavvik+lønnssatsavvik)
    lønnssatsavvik_komentar=-lønnssatsavvik
    return(virkelig_lonn,standard_kostnader,virkelig_forbruk,virkelige_kostnader,tidsavvik,lønnssatsavvik,totalavvik,lønnssatsavvik_komentar)

def ch3_standard_selv_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon):
    kost_faste_indirekte_tilv=int(3*int(sat_faste_indirekte_tilv))
    kost_variable_indirekte_tilv=int(3*int(sat_variable_indirekte_tilv))
    tilv_per_enhet=int(100+900+kost_faste_indirekte_tilv+kost_variable_indirekte_tilv)
    sat_faste_administrasjon=int(sat_faste_administrasjon)
    selvkost_enhet=tilv_per_enhet+sat_faste_administrasjon
    tilv_per_enhet_bidra=int(100+900+kost_variable_indirekte_tilv)
    return(kost_faste_indirekte_tilv,kost_variable_indirekte_tilv,tilv_per_enhet,sat_faste_administrasjon,
           selvkost_enhet,tilv_per_enhet_bidra)

def ch3_selvksot_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon):
    (kost_faste_indirekte_tilv,kost_variable_indirekte_tilv,tilv_per_enhet,sat_faste_administrasjon,
           selvkost_enhet,tilv_per_enhet_bidra)=ch3_standard_selv_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon)
    indirekte_tilv_sat_s=int(sat_faste_indirekte_tilv)+int(sat_variable_indirekte_tilv)
    indirekte_tilv_kost_s=int(870*indirekte_tilv_sat_s)
    indirekte_tilv_avvik_s=-(45100-indirekte_tilv_kost_s)
    periodens_tilvirkningskostnad_s=29000+261000+indirekte_tilv_kost_s
    endring_ferdige_varer_s=int(20*int(tilv_per_enhet))
    tilv_solgte_s=periodens_tilvirkningskostnad_s-endring_ferdige_varer_s
    tilv_solgte_virkelig_s=339932-endring_ferdige_varer_s
    admin_s=270*int(sat_faste_administrasjon)
    admin_avvik_s=admin_s-31000
    selvkost_solgte_s=tilv_solgte_s+admin_s
    selvkost_solgte_bidra_s=tilv_solgte_virkelig_s+31000
    produktresultat_s=349500-selvkost_solgte_s
    avvik_total_s=indirekte_tilv_avvik_s+admin_avvik_s
    produksjonsresultat_s=produktresultat_s-4832+avvik_total_s
    produksjonsresultat_bidra_s=349500-selvkost_solgte_bidra_s
    return(indirekte_tilv_sat_s,indirekte_tilv_kost_s,indirekte_tilv_avvik_s,periodens_tilvirkningskostnad_s,endring_ferdige_varer_s,
           tilv_solgte_s,tilv_solgte_virkelig_s,admin_s,admin_avvik_s,selvkost_solgte_s,
           selvkost_solgte_bidra_s,produktresultat_s,avvik_total_s,produksjonsresultat_s,produksjonsresultat_bidra_s)

def ch3_bidrakost_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon):
    (kost_faste_indirekte_tilv,kost_variable_indirekte_tilv,tilv_per_enhet,sat_faste_administrasjon,
           selvkost_enhet,tilv_per_enhet_bidra)=ch3_standard_selv_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon)
    indirekte_tilv_kost_b=int(870*int(sat_variable_indirekte_tilv))
    indirekte_tilv_avvik_b=(indirekte_tilv_kost_b-17600)
    periodens_tilvirkningskostnad_b=29000+261000+indirekte_tilv_kost_b
    endring_ferdige_varer_b=int(20*int(tilv_per_enhet_bidra))
    tilv_solgte_b=periodens_tilvirkningskostnad_b-endring_ferdige_varer_b
    tilv_solgte_virkelig_b=312432-endring_ferdige_varer_b
    kalkulert_DB_b=349500-tilv_solgte_b
    virkelig_dekningsbidrag_b=kalkulert_DB_b-4832+indirekte_tilv_avvik_b
    virkelig_dekningsbidrag_virkelige_b=349500-tilv_solgte_virkelig_b
    faste_admin_b=300*int(sat_faste_administrasjon)
    avvik_faste_admin_b=faste_admin_b-31000
    avvik_faste_sum_b=-500+avvik_faste_admin_b
    produksjonsresultat_b=virkelig_dekningsbidrag_b-27000-faste_admin_b+avvik_faste_sum_b
    produksjonsresultat_virkelige_b=virkelig_dekningsbidrag_virkelige_b-27500-31000
    return(indirekte_tilv_kost_b,indirekte_tilv_avvik_b,periodens_tilvirkningskostnad_b,
           endring_ferdige_varer_b,tilv_solgte_b,tilv_solgte_virkelig_b,kalkulert_DB_b,
           virkelig_dekningsbidrag_b,virkelig_dekningsbidrag_virkelige_b,faste_admin_b,
           avvik_faste_admin_b,avvik_faste_sum_b,produksjonsresultat_b,produksjonsresultat_virkelige_b)

def ch3_differanse_table(sat_faste_indirekte_tilv,sat_variable_indirekte_tilv,sat_faste_administrasjon):
    (indirekte_tilv_sat_s,indirekte_tilv_kost_s,indirekte_tilv_avvik_s,periodens_tilvirkningskostnad_s,endring_ferdige_varer_s,
    tilv_solgte_s,tilv_solgte_virkelig_s,admin_s,admin_avvik_s,selvkost_solgte_s,
    selvkost_solgte_bidra_s,produktresultat_s,avvik_total_s,
    produksjonsresultat_s,produksjonsresultat_bidra_s)=ch3_selvksot_table(sat_faste_indirekte_tilv,
            sat_variable_indirekte_tilv,sat_faste_administrasjon)

    (indirekte_tilv_kost_b,indirekte_tilv_avvik_b,periodens_tilvirkningskostnad_b,
    endring_ferdige_varer_b,tilv_solgte_b,tilv_solgte_virkelig_b,kalkulert_DB_b,
    virkelig_dekningsbidrag_b,virkelig_dekningsbidrag_virkelige_b,faste_admin_b,
    avvik_faste_admin_b,avvik_faste_sum_b,produksjonsresultat_b,
    produksjonsresultat_virkelige_b)=ch3_bidrakost_table(sat_faste_indirekte_tilv,
            sat_variable_indirekte_tilv,sat_faste_administrasjon)
    
    differanse1=produksjonsresultat_s-produksjonsresultat_b
    differanse2=endring_ferdige_varer_s-endring_ferdige_varer_b
    return(differanse1,differanse2)


def ch3_virkelige_t4(sat_faste_indirekte_tilv_t4,sat_variable_indirekte_tilv_t4,sat_faste_administrasjon_t4):
    standard_kostnad_var=(290*3)*int(sat_variable_indirekte_tilv_t4)
    effektivitets_avvik=standard_kostnad_var-17300
    forbruksavvik_var=17300-17600
    totalt_avvik_var=standard_kostnad_var-17600
    standard_kostnad_faste=(290*3)*int(sat_faste_indirekte_tilv_t4)
    volumavvik_faste=standard_kostnad_faste-27000
    forbruksavvik_faste=27000-27500
    totalt_avvik_faste=standard_kostnad_faste-27500
    standard_kostnad_admin=(270)*int(sat_faste_administrasjon_t4)
    volumavvik_admin=standard_kostnad_admin-30000
    forbruksavvik_admin=30000-31000
    totalt_avvik_admin=standard_kostnad_admin-31000
    return(standard_kostnad_var,effektivitets_avvik,forbruksavvik_var,totalt_avvik_var,
        standard_kostnad_faste,volumavvik_faste,forbruksavvik_faste,totalt_avvik_faste,
        standard_kostnad_admin,volumavvik_admin,forbruksavvik_admin,totalt_avvik_admin)

""" Chapter 4 """
def ch4_t1_budsjett(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega):
    inntekter_alfa=5000*int(budsjettert_pris_produkt_alfa)
    inntekter_omega=8000*int(budsjettert_pris_produkt_omega)
    inntekter_totalt=inntekter_alfa+inntekter_omega
    return(inntekter_alfa,inntekter_omega,inntekter_totalt)

def ch4_t1_virkelige(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega):
    virkelige_pris_alfa=round(49200/int(virkelig_salg_i_enheter_alfa),1)
    virkelige_pris_omega=round(84000/int(virkelig_salg_i_enheter_omega),1)
    virkelige_DB_alfa=round(25200/int(virkelig_salg_i_enheter_alfa),1)
    virkelige_DB_omega=round(42000/int(virkelig_salg_i_enheter_omega),1)
    return(virkelige_pris_alfa,virkelige_pris_omega,virkelige_DB_alfa,virkelige_DB_omega)

def ch4_t1_salgspris(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega,
    virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega):
    (virkelige_pris_alfa,virkelige_pris_omega,virkelige_DB_alfa,virkelige_DB_omega)=ch4_t1_virkelige(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)
    salgsprisavvik_alfa=int((virkelige_pris_alfa-int(budsjettert_pris_produkt_alfa))*int(virkelig_salg_i_enheter_alfa))
    salgsprisavvik_omega=int((virkelige_pris_omega-int(budsjettert_pris_produkt_omega))*int(virkelig_salg_i_enheter_omega))
    salgsprisavvik_total=salgsprisavvik_alfa+salgsprisavvik_omega
    return(salgsprisavvik_alfa,salgsprisavvik_omega,salgsprisavvik_total)

def ch4_t1_deknigsbidrag(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega):
    (virkelige_pris_alfa,virkelige_pris_omega,
     virkelige_DB_alfa,virkelige_DB_omega)=ch4_t1_virkelige(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)
    deknigsbidragavvik_alfa=int((virkelige_DB_alfa-4)*int(virkelig_salg_i_enheter_alfa))
    deknigsbidragavvik_omega=int((virkelige_DB_omega-6)*int(virkelig_salg_i_enheter_omega))
    deknigsbidragavvik_total=deknigsbidragavvik_alfa+deknigsbidragavvik_omega
    return(deknigsbidragavvik_alfa,deknigsbidragavvik_omega,deknigsbidragavvik_total)

def ch4_t1_volumavvik(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega):
    volumavvik_alfa=(int(virkelig_salg_i_enheter_alfa)-5000)*4
    volumavvik_omega=(int(virkelig_salg_i_enheter_omega)-8000)*6
    volumavvik_total=volumavvik_alfa+volumavvik_omega
    return(volumavvik_alfa,volumavvik_omega,volumavvik_total)

def ch4_t1_resultatavvik(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega,
    virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega):
    (salgsprisavvik_alfa,salgsprisavvik_omega,
     salgsprisavvik_total)=ch4_t1_salgspris(budsjettert_pris_produkt_alfa,budsjettert_pris_produkt_omega,
    virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)
    (volumavvik_alfa,volumavvik_omega,volumavvik_total)=ch4_t1_volumavvik(virkelig_salg_i_enheter_alfa,virkelig_salg_i_enheter_omega)
    salgets_resultatavvik_alfa=salgsprisavvik_alfa+volumavvik_alfa
    salgets_resultatavvik_omega=salgsprisavvik_omega+volumavvik_omega
    salgets_resultatavvik_total=salgets_resultatavvik_alfa+salgets_resultatavvik_omega
    return(salgets_resultatavvik_alfa,salgets_resultatavvik_omega,salgets_resultatavvik_total)

def ch4_t2_resultatavvik(budsjettert_pris_tex,budsjettert_pris_mex,budsjettert_DB_tex,budsjettert_DB_mex):
    prisavvik_tex=(85-int(budsjettert_pris_tex))*2800
    prisavvik_mex=(55-int(budsjettert_pris_mex))*2400
    prisavvik_total=prisavvik_tex+prisavvik_mex
    volumavvik_tex=(2800-3000)*int(budsjettert_DB_tex)
    volumavvik_mex=(2400-1600)*int(budsjettert_DB_mex)
    volumavvik_total=volumavvik_tex+volumavvik_mex
    salgets_resultatavvik_tex=prisavvik_tex+volumavvik_tex
    salgets_resultatavvik_mex=prisavvik_mex+volumavvik_mex
    salgets_resultatavvik_total=salgets_resultatavvik_tex+salgets_resultatavvik_mex
    return(prisavvik_tex,prisavvik_mex,prisavvik_total,volumavvik_tex,volumavvik_mex,
           volumavvik_total,salgets_resultatavvik_tex,salgets_resultatavvik_mex,salgets_resultatavvik_total)

def ch4_t3_virkelig_budsjettert(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032):
    virkelig_pris_3031=int(189000/int(virkelig_salgsvolum_3031))
    virkelig_pris_3032=int(318750/int(virkelig_salgsvolum_3032))
    return(virkelig_pris_3031,virkelig_pris_3032)

def ch4_t3_salgsprisavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032):
    (virkelig_pris_3031,virkelig_pris_3032)=ch4_t3_virkelig_budsjettert(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032)
    salgsprisavvik_3031=round((virkelig_pris_3031-1100)*int(virkelig_salgsvolum_3031),2)
    salgsprisavvik_3032=round((virkelig_pris_3032-1300)*int(virkelig_salgsvolum_3032),2)
    salgsprisavvik_total=salgsprisavvik_3031+salgsprisavvik_3032
    return(salgsprisavvik_3031,salgsprisavvik_3032,salgsprisavvik_total)

def ch4_t3_volumsavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032,db_3031,db_3032):
    volumavvik_3031=round((int(virkelig_salgsvolum_3031)-200)*int(db_3031),2)
    volumavvik_3032=round((int(virkelig_salgsvolum_3032)-200)*int(db_3032),2)
    volumavvik_total=volumavvik_3031+volumavvik_3032
    return(volumavvik_3031,volumavvik_3032,volumavvik_total)

def ch4_t3_salgetsavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032,db_3031,db_3032):
    (salgsprisavvik_3031,salgsprisavvik_3032,salgsprisavvik_total)=ch4_t3_salgsprisavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032)
    (volumavvik_3031,volumavvik_3032,volumavvik_total)=ch4_t3_volumsavvik(virkelig_salgsvolum_3031,virkelig_salgsvolum_3032,db_3031,db_3032)
    salgets_3031=salgsprisavvik_3031+volumavvik_3031
    salgets_3032=salgsprisavvik_3032+volumavvik_3032
    salgets_total=salgets_3031+salgets_3032
    return(salgets_3031,salgets_3032,salgets_total)

""" Chapter 5 """
""" def ch5_t1_direkte_lonn(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    direkte_lonn_alfa=int(timer_alfa)*300
    direkte_lonn_beta=int(timer_beta)*300
    return(direkte_lonn_alfa,direkte_lonn_beta)

def ch5_t1_direkte_arbeidstimer(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    direkte_arbeidstimer_alfa=int(enheter_alfa)*int(timer_alfa)
    direkte_arbeidstimer_beta=int(enheter_beta)*int(timer_beta)
    direkte_arbeidstimer_totalt=direkte_arbeidstimer_alfa+direkte_arbeidstimer_beta
    return(direkte_arbeidstimer_alfa,direkte_arbeidstimer_beta,direkte_arbeidstimer_totalt)

def ch5_t1_tilleggssatsen(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (direkte_arbeidstimer_alfa,direkte_arbeidstimer_beta,
    direkte_arbeidstimer_totalt)=ch5_t1_direkte_arbeidstimer(enheter_alfa, enheter_beta, 
    timer_alfa, timer_beta)
    tilleggssatsen_indirekte_lonn=round(2240000/direkte_arbeidstimer_totalt,1)
    return tilleggssatsen_indirekte_lonn

def ch5_t1_kost_tradisjonell(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (direkte_lonn_alfa,direkte_lonn_beta)=ch5_t1_direkte_lonn(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
    tilleggssatsen_indirekte_lonn=ch5_t1_tilleggssatsen(enheter_alfa, enheter_beta, 
        timer_alfa, timer_beta)
    kost_tradisjonell_indirekte_tilv_kostnad_alfa=tilleggssatsen_indirekte_lonn*int(timer_alfa)*10
    kost_tradisjonell_indirekte_tilv_kostnad_beta=tilleggssatsen_indirekte_lonn*int(timer_beta)*10
    kost_tradisjonell_enhetkost_alfa=700+direkte_lonn_alfa+kost_tradisjonell_indirekte_tilv_kostnad_alfa
    kost_tradisjonell_enhetkost_beta=480+direkte_lonn_beta+kost_tradisjonell_indirekte_tilv_kostnad_beta
    return(kost_tradisjonell_indirekte_tilv_kostnad_alfa, kost_tradisjonell_indirekte_tilv_kostnad_beta,
        kost_tradisjonell_enhetkost_alfa, kost_tradisjonell_enhetkost_beta)

def ch5_t1_kost_ABC(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    tilleggssatsen_indirekte_lonn=ch5_t1_tilleggssatsen(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
    kost_ABC_indirekte_lonn_alfa=int(int(enheter_alfa)*int(timer_alfa)*tilleggssatsen_indirekte_lonn)
    kost_ABC_indirekte_lonn_beta=int(int(enheter_beta)*int(timer_beta)*tilleggssatsen_indirekte_lonn)
    kost_ABC_alfa=kost_ABC_indirekte_lonn_alfa+1680000+2912000+588000+504000+2100000
    kost_ABC_beta=kost_ABC_indirekte_lonn_beta+2520000+1568000+1372000+2016000+4900000
    kost_ABC_indirekte_alfa=round(kost_ABC_alfa/int(enheter_alfa),1)
    kost_ABC_indirekte_beta=round(kost_ABC_beta/int(enheter_beta),1)
    kost_ABC_enhetskost_alfa=700+(300*int(timer_alfa))+kost_ABC_indirekte_alfa
    kost_ABC_enhetskost_beta=480+(300*int(timer_beta))+kost_ABC_indirekte_beta
    return(kost_ABC_indirekte_lonn_alfa,kost_ABC_indirekte_lonn_beta,
           kost_ABC_alfa,kost_ABC_beta,kost_ABC_indirekte_alfa,
           kost_ABC_indirekte_beta,kost_ABC_enhetskost_alfa,kost_ABC_enhetskost_beta)

def ch5_t1_sammenlign(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (kost_ABC_indirekte_lonn_alfa,kost_ABC_indirekte_lonn_beta,
           kost_ABC_alfa,kost_ABC_beta,kost_ABC_indirekte_alfa,
           kost_ABC_indirekte_beta,kost_ABC_enhetskost_alfa,kost_ABC_enhetskost_beta)=ch5_t1_kost_ABC(enheter_alfa,
        enheter_beta, timer_alfa, timer_beta)
    (kost_tradisjonell_indirekte_tilv_kostnad_alfa, kost_tradisjonell_indirekte_tilv_kostnad_beta,
        kost_tradisjonell_enhetkost_alfa, 
        kost_tradisjonell_enhetkost_beta)=ch5_t1_kost_tradisjonell(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
    sammenlign_differese_alfa=round(kost_ABC_enhetskost_alfa-kost_tradisjonell_enhetkost_alfa,1)
    sammenlign_differese_beta=round(kost_ABC_enhetskost_beta-kost_tradisjonell_enhetkost_beta,1)
    sammenlign_totalt_alfa=round(sammenlign_differese_alfa*int(enheter_alfa),1)
    sammenlign_totalt_beta=round(sammenlign_differese_beta*int(enheter_beta),1)
    return(sammenlign_differese_alfa,sammenlign_differese_beta,sammenlign_totalt_alfa,
        sammenlign_totalt_beta)
 """

def ch5_t1_direkte_lonn(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    direkte_lonn_alfa=round(float(int(timer_alfa)*300),3)
    direkte_lonn_beta=round(float(int(timer_beta)*300),3)
    return(direkte_lonn_alfa,direkte_lonn_beta)

def ch5_t1_direkte_arbeidstimer(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    direkte_arbeidstimer_alfa=round(float(int(enheter_alfa)*int(timer_alfa)),3)
    direkte_arbeidstimer_beta=round(float(int(enheter_beta)*int(timer_beta)),3)
    direkte_arbeidstimer_totalt=round(float(direkte_arbeidstimer_alfa+direkte_arbeidstimer_beta),3)
    return(direkte_arbeidstimer_alfa,direkte_arbeidstimer_beta,direkte_arbeidstimer_totalt)

def ch5_t1_tilleggssatsen(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (direkte_arbeidstimer_alfa,direkte_arbeidstimer_beta,
    direkte_arbeidstimer_totalt)=ch5_t1_direkte_arbeidstimer(enheter_alfa, enheter_beta, 
    timer_alfa, timer_beta)
    tilleggssatsen_indirekte_lonn=round(float(2240000/direkte_arbeidstimer_totalt),3)
    tilleggssatsen_indirekte_lonn_tekst=tilleggssatsen_indirekte_lonn*10
    return (tilleggssatsen_indirekte_lonn,tilleggssatsen_indirekte_lonn_tekst)

def ch5_t1_kost_tradisjonell(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (direkte_lonn_alfa,direkte_lonn_beta)=ch5_t1_direkte_lonn(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
    (tilleggssatsen_indirekte_lonn,tilleggssatsen_indirekte_lonn_tekst)=ch5_t1_tilleggssatsen(enheter_alfa, enheter_beta, 
        timer_alfa, timer_beta)
    kost_tradisjonell_indirekte_tilv_kostnad_alfa=round(float(tilleggssatsen_indirekte_lonn*int(timer_alfa)*10),3)
    kost_tradisjonell_indirekte_tilv_kostnad_beta=round(float(tilleggssatsen_indirekte_lonn*int(timer_beta)*10),3)
    kost_tradisjonell_enhetkost_alfa=round(float(700+direkte_lonn_alfa+kost_tradisjonell_indirekte_tilv_kostnad_alfa),3)
    kost_tradisjonell_enhetkost_beta=round(float(480+direkte_lonn_beta+kost_tradisjonell_indirekte_tilv_kostnad_beta),3)
    return(kost_tradisjonell_indirekte_tilv_kostnad_alfa, kost_tradisjonell_indirekte_tilv_kostnad_beta,
        kost_tradisjonell_enhetkost_alfa, kost_tradisjonell_enhetkost_beta)

def ch5_t1_kost_ABC(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (tilleggssatsen_indirekte_lonn,tilleggssatsen_indirekte_lonn_tekst)=ch5_t1_tilleggssatsen(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
    kost_ABC_indirekte_lonn_alfa=round(float(int(enheter_alfa)*int(timer_alfa)*tilleggssatsen_indirekte_lonn),3)
    kost_ABC_indirekte_lonn_beta=round(float(int(enheter_beta)*int(timer_beta)*tilleggssatsen_indirekte_lonn),3)
    kost_ABC_alfa=round(float(kost_ABC_indirekte_lonn_alfa+1680000+2912000+588000+504000+2100000),3)
    kost_ABC_beta=round(float(kost_ABC_indirekte_lonn_beta+2520000+1568000+1372000+2016000+4900000),3)
    kost_ABC_indirekte_alfa=round(float(kost_ABC_alfa/int(enheter_alfa)),3)
    kost_ABC_indirekte_beta=round(float(kost_ABC_beta/int(enheter_beta)),3)
    kost_ABC_enhetskost_alfa=round(float(700+(300*int(timer_alfa))+kost_ABC_indirekte_alfa),3)
    kost_ABC_enhetskost_beta=round(float(480+(300*int(timer_beta))+kost_ABC_indirekte_beta),3)
    return(kost_ABC_indirekte_lonn_alfa,kost_ABC_indirekte_lonn_beta,
           kost_ABC_alfa,kost_ABC_beta,kost_ABC_indirekte_alfa,
           kost_ABC_indirekte_beta,kost_ABC_enhetskost_alfa,kost_ABC_enhetskost_beta)

def ch5_t1_sammenlign(enheter_alfa, enheter_beta, timer_alfa, timer_beta):
    (kost_ABC_indirekte_lonn_alfa,kost_ABC_indirekte_lonn_beta,
           kost_ABC_alfa,kost_ABC_beta,kost_ABC_indirekte_alfa,
           kost_ABC_indirekte_beta,kost_ABC_enhetskost_alfa,kost_ABC_enhetskost_beta)=ch5_t1_kost_ABC(enheter_alfa,
        enheter_beta, timer_alfa, timer_beta)
    (kost_tradisjonell_indirekte_tilv_kostnad_alfa, kost_tradisjonell_indirekte_tilv_kostnad_beta,
        kost_tradisjonell_enhetkost_alfa, 
        kost_tradisjonell_enhetkost_beta)=ch5_t1_kost_tradisjonell(enheter_alfa, 
        enheter_beta, timer_alfa, timer_beta)
    sammenlign_differese_alfa=round(float(kost_ABC_enhetskost_alfa-kost_tradisjonell_enhetkost_alfa),3)
    sammenlign_differese_beta=round(float(kost_ABC_enhetskost_beta-kost_tradisjonell_enhetkost_beta),3)
    sammenlign_totalt_alfa=round(float(sammenlign_differese_alfa*int(enheter_alfa)),3)
    sammenlign_totalt_beta=round(float(sammenlign_differese_beta*int(enheter_beta)),3)
    return(sammenlign_differese_alfa,sammenlign_differese_beta,sammenlign_totalt_alfa,
        sammenlign_totalt_beta)

def ch5_t2_enheter_totalt(enheter_a, enheter_b, timer_a, timer_b):
    enheter_totalt=int(enheter_a)+int(enheter_b)
    return enheter_totalt

def ch5_t2_enhetskostnad(enheter_a, enheter_b, timer_a, timer_b):
    maskinering_aktivitet_a=round(int(enheter_a)*int(timer_a),1)
    maskinering_kostnad_a=round((maskinering_aktivitet_a*57.97),1)
    sum_indirekte_kostnad_a=round(maskinering_kostnad_a+1120000+1596000+1488000,1)
    indirekte_kostnader_per_enhet_a=round(sum_indirekte_kostnad_a/int(enheter_a),1)
    enhetskostnad_a=round(200+450+indirekte_kostnader_per_enhet_a,1)
    maskinering_aktivitet_b=round(int(enheter_b)*int(timer_b),1)
    maskinering_kostnad_b=round((maskinering_aktivitet_b*57.97),1)
    sum_indirekte_kostnad_b=round(maskinering_kostnad_b+3360000+1064000+992000,1)
    indirekte_kostnader_per_enhet_b=round(sum_indirekte_kostnad_b/int(enheter_b),1)
    enhetskostnad_b=round(250+360+indirekte_kostnader_per_enhet_b,1)
    return(maskinering_aktivitet_a,maskinering_kostnad_a,
        sum_indirekte_kostnad_a,indirekte_kostnader_per_enhet_a, enhetskostnad_a,
        maskinering_aktivitet_b,maskinering_kostnad_b,
        sum_indirekte_kostnad_b,indirekte_kostnader_per_enhet_b, enhetskostnad_b)

def ch6_t1_foregaende_ar(husleie_21, husleie_okning_22, bilkostnader_21, bilkostnader_okning_22):
    fa_husleie_percentage_21=round(int(husleie_21)*100/10350000,2)
    fa_husleie_endring=(int(husleie_okning_22)*12)
    fa_husleie_22=int(husleie_21)+fa_husleie_endring
    fa_husleie_percentage_22=round(fa_husleie_22*100/10867500,2)

    fa_bilkostnader_percentage_21=round(int(bilkostnader_21)*100/10350000,2)
    fa_bilkostnader_endring=int(bilkostnader_okning_22)
    fa_bilkostnader_22=int(bilkostnader_21)+fa_bilkostnader_endring
    fa_bilkostnader_percentage_22=round(fa_bilkostnader_22*100/10867500,2)

    fa_sum_drift_21=6350000+2300000+276000+363216+int(husleie_21)+68300+int(bilkostnader_21)+120000
    fa_sum_drift_percentage_21=round(fa_sum_drift_21*100/10350000)
    fa_sum_drift_22=7063875+2369000+284280+374112+int(fa_husleie_22)+69666+int(fa_bilkostnader_22)+140000
    fa_sum_drift_percentage_22=round(fa_sum_drift_22*100/10867500)
    
    fa_driftresultat_21=10350000-fa_sum_drift_21
    fa_driftresultat_percentage_21=round(fa_driftresultat_21*100/10350000,1)
    fa_driftresultat_22=10867500-fa_sum_drift_22
    fa_driftresultat_percentage_22=round(fa_driftresultat_22*100/10867500,1)

    fa_resultat_21=fa_driftresultat_21-28500
    fa_resultat_percentage_21=round(fa_resultat_21*100/10350000,1)
    fa_resultat_22=fa_driftresultat_22-28927
    fa_resultat_percentage_22=round(fa_resultat_22*100/10867500,1)
    return(fa_husleie_percentage_21,fa_husleie_endring,fa_husleie_22,fa_husleie_percentage_22,
        fa_bilkostnader_percentage_21,fa_bilkostnader_endring,fa_bilkostnader_22,fa_bilkostnader_percentage_22,
        fa_sum_drift_21,fa_sum_drift_percentage_21,fa_sum_drift_22,fa_sum_drift_percentage_22,
        fa_driftresultat_21,fa_driftresultat_percentage_21,fa_driftresultat_22,fa_driftresultat_percentage_22,
        fa_resultat_21,fa_resultat_percentage_21,fa_resultat_22,fa_resultat_percentage_22)

def ch6_t1_maned_budsjett(husleie_21, husleie_okning_22, bilkostnader_21, bilkostnader_okning_22):
    (fa_husleie_percentage_21,fa_husleie_endring,fa_husleie_22,fa_husleie_percentage_22,
    fa_bilkostnader_percentage_21,fa_bilkostnader_endring,fa_bilkostnader_22,fa_bilkostnader_percentage_22,
    fa_sum_drift_21,fa_sum_drift_percentage_21,fa_sum_drift_22,fa_sum_drift_percentage_22,
    fa_driftresultat_21,fa_driftresultat_percentage_21,fa_driftresultat_22,fa_driftresultat_percentage_22,
    fa_resultat_21,fa_resultat_percentage_21,fa_resultat_22,
    fa_resultat_percentage_22)=ch6_t1_foregaende_ar(husleie_21, husleie_okning_22, 
    bilkostnader_21, bilkostnader_okning_22)

    mb_husleie_maned=round(fa_husleie_22/12)
    mb_husleie_kvartal=round(mb_husleie_maned*3)

    mb_bilkostnader_maned=round(fa_bilkostnader_22/12)
    mb_bilkostnader_kvartal=round(mb_bilkostnader_maned*3)

    mb_sum_drift_januar=565110+197417+23690+31176+mb_husleie_maned+5806+mb_bilkostnader_maned+11667
    mb_sum_drift_februar=529791+197417+23690+31176+mb_husleie_maned+5806+mb_bilkostnader_maned+11667
    mb_sum_drift_mars=635749+197417+23690+31176+mb_husleie_maned+5806+mb_bilkostnader_maned+11667
    mb_sum_drift_kvartal=mb_sum_drift_januar+mb_sum_drift_februar+mb_sum_drift_mars

    mb_driftsresultat_januar=869400-mb_sum_drift_januar
    mb_driftsresultat_februar=815063-mb_sum_drift_februar
    mb_driftsresultat_mars=978075-mb_sum_drift_mars
    mb_driftsresultat_kvartal=mb_driftsresultat_januar+mb_driftsresultat_februar+mb_driftsresultat_mars

    mb_resultat_januar=mb_driftsresultat_januar-2411
    mb_resultat_februar=mb_driftsresultat_februar-2411
    mb_resultat_mars=mb_driftsresultat_mars-2411
    mb_resultat_kvartal=mb_resultat_januar+mb_resultat_februar+mb_resultat_mars
    return(mb_husleie_maned,mb_husleie_kvartal,mb_bilkostnader_maned,mb_bilkostnader_kvartal,
        mb_sum_drift_januar,mb_sum_drift_februar,mb_sum_drift_mars,mb_sum_drift_kvartal,
        mb_driftsresultat_januar,mb_driftsresultat_februar,mb_driftsresultat_mars,mb_driftsresultat_kvartal,
        mb_resultat_januar,mb_resultat_februar,mb_resultat_mars,mb_resultat_kvartal)

def ch6_t1_likviditetsbudsjett(husleie_21, husleie_okning_22, bilkostnader_21, bilkostnader_okning_22):

    (mb_husleie_maned,mb_husleie_kvartal,mb_bilkostnader_maned,mb_bilkostnader_kvartal,
    mb_sum_drift_januar,mb_sum_drift_februar,mb_sum_drift_mars,mb_sum_drift_kvartal,
    mb_driftsresultat_januar,mb_driftsresultat_februar,mb_driftsresultat_mars,mb_driftsresultat_kvartal,
    mb_resultat_januar,mb_resultat_februar,mb_resultat_mars,
    mb_resultat_kvartal)=ch6_t1_maned_budsjett(husleie_21, husleie_okning_22, 
    bilkostnader_21, bilkostnader_okning_22)

    l_husleie_maned=mb_husleie_maned
    l_husleie_kvartal=mb_husleie_kvartal

    l_bilkostnader_maned=round(mb_bilkostnader_maned*(1.25),1)
    l_bilkostnader_kvartal=round(mb_bilkostnader_kvartal*(1.25),1)

    l_sum_utbetalinger_januar=690000+197417+65350+l_husleie_maned+7257+l_bilkostnader_maned+215000
    l_sum_utbetalinger_februar=708194+197417+l_husleie_maned+7257+l_bilkostnader_maned+32000+165000
    l_sum_utbetalinger_mars=684313+197417+55672+l_husleie_maned+7257+l_bilkostnader_maned
    l_sum_utbetalinger_kvartal=round(l_sum_utbetalinger_januar+l_sum_utbetalinger_februar+l_sum_utbetalinger_mars,1)

    l_inn_ut_januar=round(1156025-l_sum_utbetalinger_januar,1)
    l_inn_ut_februar=round(1066373-l_sum_utbetalinger_februar,1)
    l_inn_ut_mars=round(1079958-l_sum_utbetalinger_mars,1)
    l_inn_ut_kvartal=round(l_inn_ut_januar+l_inn_ut_februar+l_inn_ut_mars,1)

    l_lik_reserveUB_januar=round(50000+l_inn_ut_januar,1)
    l_lik_reserveIB_februar=round(l_lik_reserveUB_januar,1)
    l_lik_reserveUB_februar=round(l_lik_reserveIB_februar+l_inn_ut_februar,1)
    l_lik_reserveIB_mars=round(l_lik_reserveUB_februar,1)
    l_lik_reserveUB_mars=round(l_lik_reserveIB_mars+l_inn_ut_mars,1)

    return(l_husleie_maned,l_husleie_kvartal,l_bilkostnader_maned,l_bilkostnader_kvartal,
        l_sum_utbetalinger_januar,l_sum_utbetalinger_februar,l_sum_utbetalinger_mars, 
        l_sum_utbetalinger_kvartal,l_inn_ut_januar,l_inn_ut_februar,l_inn_ut_mars,l_inn_ut_kvartal,
        l_lik_reserveUB_januar,l_lik_reserveUB_februar,l_lik_reserveUB_mars,
        l_lik_reserveIB_februar,l_lik_reserveIB_mars)

def ch6_t2_budsjett_2020(varekostnad_19, varekostnad_okning_20, lonn_19, lonn_okning_20):
    b_20_varekostnad_percentage_2019=round(int(varekostnad_19)*100/5000000,1)
    b_20_varekostnad_2020=round(5750000*int(varekostnad_okning_20)/100,1)
    b_20_lonn_percentage_2019=round(int(lonn_19)*100/5000000,1)
    b_20_lonn_2020=round(int(lonn_19)*(1+(int(lonn_okning_20)/100)),1)
    b_20_lonn_percentage_2020=round(b_20_lonn_2020*100/5750000,1)
    b_20_sum_kostnader_2019=round(int(varekostnad_19)+int(lonn_19)+120000+157920+500000+500000+150000,1)
    b_20_sum_kostnader_percentage_2019=round(b_20_sum_kostnader_2019*100/5000000,1)
    b_20_sum_kostnader_2020=round(b_20_varekostnad_2020+b_20_lonn_2020+126000+165816+540000+287500+150000,1)
    b_20_sum_kostnader_percentage_2020=round(b_20_sum_kostnader_2020*100/5750000,1)
    b_20_drit_2019=round(5000000-b_20_sum_kostnader_2019,1)
    b_20_drit_percentage_2019=round(b_20_drit_2019*100/5000000,1)
    b_20_drit_2020=round(5750000-b_20_sum_kostnader_2020,1)
    b_20_drit_percentage_2020=round(b_20_drit_2020*100/5750000,1)
    b_20_resultat_2019=round(b_20_drit_2019-100000,1)
    b_20_drit__percentage_2019=round(b_20_drit_2019*100/5000000)
    b_20_resultat_2020=round(b_20_drit_2020-100000,1)
    b_20_drit__percentage_2020=round(b_20_drit_2020*100/5750000)
    return(b_20_varekostnad_percentage_2019,b_20_varekostnad_2020,
    b_20_lonn_percentage_2019,b_20_lonn_2020,b_20_lonn_percentage_2020,
    b_20_sum_kostnader_2019,b_20_sum_kostnader_percentage_2019,
    b_20_sum_kostnader_2020,b_20_sum_kostnader_percentage_2020,b_20_drit_2019,
    b_20_drit_percentage_2019,b_20_drit_2020,b_20_drit_percentage_2020,
    b_20_resultat_2019,b_20_drit__percentage_2019,b_20_resultat_2020,b_20_drit__percentage_2020)

def ch6_t2_maned_2020(varekostnad_19, varekostnad_okning_20, lonn_19, lonn_okning_20):
    (b_20_varekostnad_percentage_2019,b_20_varekostnad_2020,
    b_20_lonn_percentage_2019,b_20_lonn_2020,b_20_lonn_percentage_2020,
    b_20_sum_kostnader_2019,b_20_sum_kostnader_percentage_2019,
    b_20_sum_kostnader_2020,b_20_sum_kostnader_percentage_2020,b_20_drit_2019,
    b_20_drit_percentage_2019,b_20_drit_2020,b_20_drit_percentage_2020,
    b_20_resultat_2019,b_20_drit__percentage_2019,b_20_resultat_2020,
    b_20_drit__percentage_2020)=ch6_t2_budsjett_2020(varekostnad_19, 
    varekostnad_okning_20, lonn_19, lonn_okning_20)

    m_20_varkostnad_maned=round(b_20_varekostnad_2020/12,1)
    m_20_varkostnad_kvartal=round(m_20_varkostnad_maned*3,1)
    m_20_lonn_maned=round(b_20_lonn_2020/12,1)
    m_20_lonn_kvartal=round(m_20_lonn_maned*3,1)
    m_20_sum_kostnader_maned=round(b_20_sum_kostnader_2020/12,1)
    m_20_sum_kostnader_kvartal=round(m_20_sum_kostnader_maned*3,1)
    m_20_drit_maned=round(b_20_drit_2020/12,1)
    m_20_drit_kvartal=round(m_20_drit_maned*3,1)
    m_20_resultat_maned=round(b_20_resultat_2020/12,1)
    m_20_resultat_kvartal=round(m_20_resultat_maned*3,1)
    return(m_20_varkostnad_maned,m_20_varkostnad_kvartal,
    m_20_lonn_maned,m_20_lonn_kvartal,m_20_sum_kostnader_maned,
    m_20_sum_kostnader_kvartal,m_20_drit_maned,m_20_drit_kvartal,
    m_20_resultat_maned,m_20_resultat_kvartal)

def ch6_t2_utbetal_2020(varekostnad_19, varekostnad_okning_20, lonn_19, lonn_okning_20):
    (m_20_varkostnad_maned,m_20_varkostnad_kvartal,
    m_20_lonn_maned,m_20_lonn_kvartal,m_20_sum_kostnader_maned,
    m_20_sum_kostnader_kvartal,m_20_drit_maned,m_20_drit_kvartal,
    m_20_resultat_maned,m_20_resultat_kvartal)=ch6_t2_maned_2020(varekostnad_19, 
    varekostnad_okning_20, lonn_19, lonn_okning_20)

    u_20_mva_maned=round(m_20_varkostnad_maned*0.25,1)
    u_20_mva_kvartal=round(u_20_mva_maned*3,1)
    u_20_vare_maned=round(m_20_varkostnad_maned+u_20_mva_maned,1)
    u_20_vare_kvartal=round(u_20_vare_maned*3,2)
    u_20_kjop_maned=round(u_20_vare_maned/2,1)
    u_20_sum_utbetal_januar=300000+u_20_kjop_maned
    u_20_totalt_utbetal_kvartal=u_20_sum_utbetal_januar+(2*u_20_vare_maned)
    return(u_20_mva_maned,u_20_mva_kvartal,u_20_vare_maned,u_20_vare_kvartal,
    u_20_kjop_maned,u_20_sum_utbetal_januar,u_20_totalt_utbetal_kvartal)

def ch6_t2_lik_2020(varekostnad_19, varekostnad_okning_20, lonn_19, lonn_okning_20):

    (m_20_varkostnad_maned,m_20_varkostnad_kvartal,
    m_20_lonn_maned,m_20_lonn_kvartal,m_20_sum_kostnader_maned,
    m_20_sum_kostnader_kvartal,m_20_drit_maned,m_20_drit_kvartal,
    m_20_resultat_maned,m_20_resultat_kvartal)=ch6_t2_maned_2020(varekostnad_19, 
    varekostnad_okning_20, lonn_19, lonn_okning_20)

    (u_20_mva_maned,u_20_mva_kvartal,u_20_vare_maned,u_20_vare_kvartal,
    u_20_kjop_maned,u_20_sum_utbetal_januar,
    u_20_totalt_utbetal_kvartal)=ch6_t2_utbetal_2020(varekostnad_19, 
    varekostnad_okning_20, lonn_19, lonn_okning_20)

    lik_20_lonn_januar=round(m_20_lonn_maned-15000,1)
    lik_20_lonn_sum=round(lik_20_lonn_januar+(m_20_lonn_maned*2),1)
    lik_20_sum_utbetaling_januar=(u_20_sum_utbetal_januar+lik_20_lonn_januar+
                    47000+29948+250000)
    lik_20_sum_utbetaling_februar=(u_20_vare_maned+m_20_lonn_maned+29948+33000+208000)
    lik_20_sum_utbetaling_mars=(u_20_vare_maned+m_20_lonn_maned+22560+135000+29948+450000)
    lik_20_sum_utbetaling_sum=(u_20_totalt_utbetal_kvartal+lik_20_lonn_sum+
        69560+135000+89844+450000+208000+250000)
    lik_20_inn_ut_januar=round(563802-lik_20_sum_utbetaling_januar,1)
    lik_20_inn_ut_februar=round(598958-lik_20_sum_utbetaling_februar,1)
    lik_20_inn_ut_mars=round(598958-lik_20_sum_utbetaling_mars,1)
    lik_20_inn_ut_sum=round(1761719-lik_20_sum_utbetaling_sum,1)
    lik_20_UB_januar=round(850000+lik_20_inn_ut_januar,1)
    lik_20_UB_februar=round(lik_20_UB_januar+lik_20_inn_ut_februar,1)
    lik_20_UB_mars=round(lik_20_UB_februar+lik_20_inn_ut_mars,1)
    return(lik_20_lonn_januar,lik_20_lonn_sum, lik_20_sum_utbetaling_januar,
    lik_20_sum_utbetaling_februar,lik_20_sum_utbetaling_mars,lik_20_sum_utbetaling_sum,
    lik_20_inn_ut_januar,lik_20_inn_ut_februar,lik_20_inn_ut_mars,
    lik_20_inn_ut_sum,lik_20_UB_januar,lik_20_UB_februar,lik_20_UB_mars)

def ch6_t2_pavirke(varekostnad_19, varekostnad_okning_20, lonn_19, lonn_okning_20):

    (m_20_varkostnad_maned,m_20_varkostnad_kvartal,
    m_20_lonn_maned,m_20_lonn_kvartal,m_20_sum_kostnader_maned,
    m_20_sum_kostnader_kvartal,m_20_drit_maned,m_20_drit_kvartal,
    m_20_resultat_maned,m_20_resultat_kvartal)=ch6_t2_maned_2020(varekostnad_19, 
        varekostnad_okning_20, lonn_19, lonn_okning_20)
    
    (u_20_mva_maned,u_20_mva_kvartal,u_20_vare_maned,u_20_vare_kvartal,
    u_20_kjop_maned,u_20_sum_utbetal_januar,
    u_20_totalt_utbetal_kvartal)=ch6_t2_utbetal_2020(varekostnad_19, 
        varekostnad_okning_20, lonn_19, lonn_okning_20)
    
    p_varekostnad_maned=m_20_varkostnad_maned
    p_varekjop_maned=round(p_varekostnad_maned-15000,1)
    p_mva=round(1.25*p_varekjop_maned,1)
    p_kjop_maned=round(p_mva/2,1)
    p_sum_utbetaling_februar=round(p_kjop_maned,1)
    p_sum_utbetaling_mars=round(p_kjop_maned*2,1)
    p_sum_utbetaling_UB=round(p_kjop_maned+p_mva,1)
    p_total_utbetaling=round(300000+p_sum_utbetaling_februar+p_sum_utbetaling_mars,1)
    p_lik=round(u_20_totalt_utbetal_kvartal-p_total_utbetaling,1)
    return(p_varekostnad_maned,p_varekjop_maned,p_mva,
    p_kjop_maned,p_sum_utbetaling_februar,p_sum_utbetaling_mars,
    p_sum_utbetaling_UB,p_total_utbetaling,p_lik)

