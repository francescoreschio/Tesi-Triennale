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

#Non va bene---------------------------------------------------
def FlattenAndArray(Station, Sector, Wheel):

  Station_count = ConvertToKHz(np.bincount(ak.flatten(Station) - 1))    #Inizia da 1 e non da 0
  Sector_count = ConvertToKHz(np.bincount(ak.flatten(Sector)))
  Wheel_count = ConvertToKHz(np.bincount(ak.flatten(Wheel) + 2))        #Possiede numeri negativi -2, -1

  CMS = ak.Array([Station_count, Sector_count, Wheel_count])

  return CMS
#-------------------------------------------------------------

#Funzione per creare grafico bidimensionale
def BiDimHist(DimRow, DimCol, feature1, feature2):                 #Feature1, Feature 2 rappresentano Wheel, Sector o Station
  BiDimMatrix = np.zeros((DimRow, DimCol), dtype = 'int32')

  for i in range(len(feature1)):
    for j in range(len(feature1[i])):
       BiDimMatrix[feature1[i][j]][feature2[i][j]] += 1
      
  return BiDimMatrix





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

