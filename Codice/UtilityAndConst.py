import uproot 
import awkward as ak


#Utility
stub_features = ['orbit', 'bx', 'nStubs', 'stubHwPhi', 'stubHwPhiB', 'stubHwQual', 'stubHwEta', 'stubHwQEta', 'stubStation', 'stubWheel', 'stubSector', 'stubTag']
bmtf_features = ['nBmtfMuons', 'bmtfHwPt', 'bmtfHwPtu', 'bmtfHwPhi', 'bmtfHwEta', 'bmtfPt', 'bmtfPtu', 'bmtfPhi', 'bmtfEta', 'bmtfHwSign', 'bmtfSignValid', 'bmtfDXY', 'bmtfHwQual', 'bmtfProcessor']
gmt_features  = ['nGmtMuons', 'gmtHwPt', 'gmtHwPtu', 'gmtHwPhi', 'gmtHwEta', 'gmtHwPhiAtVtx', 'gmtHwEtaAtVtx', 'gmtPt', 'gmtPtu', 'gmtPhi', 'gmtEta', 'gmtPhiAtVtx', 'gmtEtaAtVtx', 'gmtCharge', 'gmtDXY', 'gmtQual', 'gmtTfIndex']



#Costanti
ONE_LUMI_IN_ORBITS = 2**18
ONE_ORBIT_IN_BX    = 3564
ONE_BX_IN_NS       = 25

ONE_LUMI_IN_NS = ONE_LUMI_IN_ORBITS * ONE_ORBIT_IN_BX * ONE_BX_IN_NS
ONE_LUMI_IN_S = ONE_LUMI_IN_NS / 1e9

