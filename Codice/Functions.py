from UtilityAndConst import *
import uproot
import numpy as np
import matplotlib.pyplot as plt
import awkward as ak
import mplhep as hep

hep.style.use("CMS")


#--------------------------------------Funzioni ------------------------------------------------------------#

def OpenRootFile(file, features):
  with uproot.open(file) as f:
    evs = f["bmtfNtuplizer/Events"]
    awk_array = evs.arrays(features, library="ak")

  return awk_array


def ConvertToKHz(counts, n_ls = 1):
  return counts / n_ls / ONE_LUMI_IN_S / 1e3


def ConvertToHz(counts, n_ls = 1):
  return counts / n_ls / ONE_LUMI_IN_S

  

#Funzione per trovare il numero di stubs per orbit 
def StubsPerOrbit(BX, nStubs):
   
  '''Spiegazione: il primo ciclo for permette di ricavare l'argomento all'interno dell'array BX in cui avviene l'orbita;
  Il secondo ciclo invece somma tutte le stub dell'orbita corrispondente, facendone il bincount'''

  BxPerOrbit = [0]

  for i in range(len(BX) - 1):
    if (BX[i] > BX[i + 1]):
       BxPerOrbit.append(i)

  StubsPerOrbit = np.zeros(len(BxPerOrbit), dtype='int16')
  
  for i in range(len(BxPerOrbit) - 1):
    StubsPerOrbit[i] = np.sum(nStubs[BxPerOrbit[i] : BxPerOrbit[i + 1]])

  StubsPerOrbit_BC = np.bincount(StubsPerOrbit)

#361 è il numero minimo corrispondente a LS306
  return StubsPerOrbit_BC#[:316]



#Funzione per distribuzione degli angoli in funzione del sector 
def PhiPerSector(Phi, Sector):

  PhiDistribution = [[] for _ in range(12)]

  for i in range(len(Phi)):
    PhiDistribution[Sector[i]].append(Phi[i])

  return ak.Array(PhiDistribution)
  


def ArrayConcatenation(LS133, LS263, LS264, LS306):

  Distribution = [[] for _ in range(12)]

  for i in range(12):
    Distribution[i] = np.concatenate((LS133[i], LS263[i], LS264[i], LS306[i]))

  return ak.Array(Distribution)



def CheckChargeAndMomentum(SignValid, Sign, Pt, Ptu):
  NotValidSign = np.where(SignValid == 0)[0]

  NotSign = [Sign[NotValidSign[i]] for i in range(len(NotValidSign))]
  NotPt = [Pt[NotValidSign[i]] for i in range(len(NotValidSign))]
  #NotPtu = [Ptu[NotValidSign[i]] for i in range(len(NotValidSign))]

  return NotSign, NotPt



def Bins(Start, Stop, NOB, Data):
  #Inizio, fine del'intervallo, e NumbmerOfBins

  Range = np.linspace(Start, Stop, NOB)

  Indicies = np.digitize(Data, Range, right=True)
  #Ritorna gli indici di Data nel corripondente bin definito prima

  return Range, Indicies  



def WeightedBiDimHist(NumRow, NumCol, Index1, Index2, Weights):

  BiDimHist = np.zeros((NumRow, NumCol))

  np.add.at(BiDimHist, (Index1, Index2), Weights)
  
  return BiDimHist










#--------------------------------------Funzioni per la grafica------------------------------------------------------------#
a = 28
def draw_cms_label(ax: plt.Axes, label: str = "Preliminary", rlabel: str = "L1T Scouting 2024 (1.8 $pb^{-1}$ , 13.6 TeV)", 
                   fontsize: int = a, data: bool = True):
    
    hep.cms.label(
        ax       = ax,
        data     = data,
        label    = label,
        rlabel   = rlabel,
        fontsize = fontsize
    )

def MOREdraw_cms_label(ax: plt.Axes, label: str = "Preliminary", rlabel: str = "L1T Scouting 2024 (6.38 $pb^{-1}$ , 13.6 TeV)", 
                  fontsize: int = a, data: bool = True):
  
  hep.cms.label(
      ax       = ax,
      data     = data,
      label    = label,
      rlabel   = rlabel,
      fontsize = fontsize
  )

def set_label_font(ax: plt.Axes, fontsize: int = a):
    
    ax.set_xlabel(ax.get_xlabel(), fontsize = fontsize)
    ax.set_ylabel(ax.get_ylabel(), fontsize = fontsize)
    
    
def set_tick_font(ax: plt.Axes, fontsize: int = a):
    
    ax.tick_params(axis = "x", labelsize = fontsize, which = "major")
    ax.tick_params(axis = "y", labelsize = fontsize, which = "major")
    
    
def draw_grid(ax: plt.Axes, which: str = "major", axis: str = "both", alpha: float = 0.2, color: str = "gray", ls: str = "-"):
    
    ax.grid(True, which = which, axis = axis, alpha = alpha, color = color, ls = ls)
    ax.set_axisbelow(True)

