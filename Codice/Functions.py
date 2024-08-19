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


#Funzione per creare grafico bidimensionale
def BiDimHist(DimRow, DimCol, feature1, feature2):                 #Feature1, Feature 2 rappresentano Wheel, Sector o Station
  BiDimMatrix = np.zeros((DimRow, DimCol), dtype = 'int32')

  for i in range(len(feature1)):
    for j in range(len(feature1[i])):
       BiDimMatrix[feature1[i][j]][feature2[i][j]] += 1
      
  return BiDimMatrix

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


#--------------------------------------Funzioni per la grafica------------------------------------------------------------#
def draw_cms_label(ax: plt.Axes, label: str = "Preliminary", rlabel: str = "L1DS", fontsize: int = 28, data: bool = True):
    
    hep.cms.label(
        ax       = ax,
        data     = data,
        label    = label,
        rlabel   = rlabel,
        fontsize = fontsize
    )

def set_label_font(ax: plt.Axes, fontsize: int = 28):
    
    ax.set_xlabel(ax.get_xlabel(), fontsize = fontsize)
    ax.set_ylabel(ax.get_ylabel(), fontsize = fontsize)
    
    
def set_tick_font(ax: plt.Axes, fontsize: int = 28):
    
    ax.tick_params(axis = "x", labelsize = fontsize, which = "major")
    ax.tick_params(axis = "y", labelsize = fontsize, which = "major")
    
    
def draw_grid(ax: plt.Axes, which: str = "major", axis: str = "both", alpha: float = 0.2, color: str = "gray", ls: str = "-"):
    
    ax.grid(True, which = which, axis = axis, alpha = alpha, color = color, ls = ls)
    ax.set_axisbelow(True)

