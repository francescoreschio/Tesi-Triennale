from UtilityAndConst import *
import uproot
import matplotlib.pyplot as plt
import mplhep as hep

hep.style.use("CMS")


#Funzioni

def OpenRootFile(file, features):
  with uproot.open(file) as f:
    evs = f["bmtfNtuplizer/Events"]
    awk_array = evs.arrays(features, library="ak")

  return awk_array


def ConvertToHz(counts, n_ls = 1):
  return counts / n_ls / ONE_LUMI_IN_S / 1e3

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

