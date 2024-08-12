from UtilityAndConst import *
import uproot


#Funzioni
def ConvertToHz(counts, n_ls = 1):
  return counts / n_ls / ONE_LUMI_IN_S / 1e3

def OpenRootFile(file, features):
  with uproot.open(file) as f:
    evs = f["bmtfNtuplizer/Events"]
    awk_array = evs.arrays(features, library="ak")

  return awk_array