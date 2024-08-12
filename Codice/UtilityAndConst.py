
#Utility
stub_features = ['orbit', 'bx', 'nStubs', 'stubHwPhi', 'stubHwPhiB', 'stubHwQual', 'stubHwEta', 'stubHwQEta', 'stubStation', 'stubWheel', 'stubSector', 'stubTag']
bmtf_features = ['nBmtfMuons', 'bmtfHwPt', 'bmtfHwPtu', 'bmtfHwPhi', 'bmtfHwEta', 'bmtfPt', 'bmtfPtu', 'bmtfPhi', 'bmtfEta', 'bmtfHwSign', 'bmtfHwSignValid', 'bmtfHwDXY', 'bmtfHwQual', 'bmtfProcessor']
gmt_features  = ['nGmtMuons', 'gmtHwPt', 'gmtHwPtu', 'gmtHwPhi', 'gmtHwEta', 'gmtHwPhiAtVtx', 'gmtHwEtaAtVtx', 'gmtPt', 'gmtPtu', 'gmtPhi', 'gmtEta', 'gmtPhiAtVtx', 'gmtEtaAtVtx', 'gmtCharge', 'gmtDxy', 'gmtQual', 'gmtTfIndex']



#Costanti

FONTSIZE  = 22
FIGSIZE   = (10, 8)

CMS_PALETTE_1 = ["#5790fc", "#f89c20", "#e42536", "#964a8b", "#9c9ca1", "#7a21dd"]
CMS_PALETTE_2 = ["#3f90da", "#ffa90e", "#bd1f01", "#94a4a2", "#832db6", "#a96b59", "#e76300", "#b9ac70", "#717581", "#92dadd"]


ONE_LUMI_IN_ORBITS = 2**18
ONE_ORBIT_IN_BX    = 3564
ONE_BX_IN_NS       = 25

ONE_LUMI_IN_NS = ONE_LUMI_IN_ORBITS * ONE_ORBIT_IN_BX * ONE_BX_IN_NS
ONE_LUMI_IN_S = ONE_LUMI_IN_NS / 1e9

