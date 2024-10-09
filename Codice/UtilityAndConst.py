import numpy as np
import uproot 
import awkward as ak
import os 

dir = "/Users/francescolarovere/Documents/Tesi-Triennale/Dati"
os.chdir(dir)



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


#Stubs-------------------------------------------------------------------------------------------------------------



StubsPerOrbitLS133 = np.array([ 1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	1,	0,	3,	2,
                                1,	2,	5,	4,	3,	2,	5,	1,	6,	4,	8,	6,	9,	8,	13,	20,	25,	18,
                                18,	19,	24,	28,	38,	33,	37,	47,	40,	58,	55,	82,	73,	79,	76,	97,	81,	105,
                                103,	126,	138,	124,	153,	153,	158,	186,	186,	192,	200,	210,	233,	219,	225,	244,	267,	272,
                                268,	258,	268,	257,	279,	285,	287,	290,	308,	304,	302,	340,	290,	294,	280,	287,	342,	299,
                                309,	302,	308,	306,	311,	311,	294,	292,	256,	265,	254,	254,	250,	234,	209,	210,	201,	198,
                                192,	170,	179,	161,	159,	136,	141,	144,	111,	127,	93,	99,	100,	88,	92,	85,	76,	65,
                                69,	59,	58,	43,	48,	43,	32,	29,	34,	35,	27,	29,	20,	13,	24,	18,	13,	11,
                                10,	9,	3,	9,	14,	10,	7,	4,	3,	9,	7,	5,	5,	3,	2,	5,	1,	2,
                                0,	4,	2,	0,	1,	0,	0,	0,	0,	1,])

StubsPerOrbitLS263 = np.array([ 1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	1,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	1,	0,	1,	2,
                                3,	0,	1,	0,	4,	4,	3,	5,	4,	2,	3,	9,	8,	6,	11,	20,	21,	17,
                                22,	14,	15,	19,	26,	35,	34,	38,	35,	46,	53,	58,	55,	59,	75,	72,	90,	108,
                                111,	118,	111,	155,	126,	112,	161,	144,	167,	179,	147,	182,	221,	224,	188,	236,	228,	240,
                                263,	267,	247,	279,	262,	289,	286,	321,	303,	318,	345,	303,	300,	299,	321,	289,	253,	303,
                                291,	328,	298,	298,	303,	310,	276,	296,	267,	253,	236,	257,	233,	227,	247,	219,	229,	202,
                                211,	191,	216,	158,	172,	175,	166,	179,	128,	130,	125,	121,	104,	117,	93,	103,	81,	90,
                                63,	60,	73,	56,	43,	61,	46,	43,	44,	43,	25,	28,	35,	23,	22,	21,	17,	14,
                                9,	27,	12,	8,	15,	6,	12,	6,	9,	1,	2,	3,	8,	5,	4,	3,	1,	1,
                                4,	3,	2,	2,	1,	1,	0,	0,	1,	0,])

StubsPerOrbitLS264 = np.array([ 1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	1,	1,	0,	0,
                                0,	0,	2,	6,	1,	3,	4,	3,	2,	4,	4,	4,	7,	9,	12,	8,	15,	17,
                                19,	20,	28,	26,	34,	39,	34,	35,	57,	44,	56,	55,	70,	68,	79,	95,	86,	89,
                                143,	118,	131,	129,	144,	144,	162,	162,	162,	174,	185,	196,	207,	225,	235,	232,	234,	250,
                                238,	238,	241,	274,	278,	274,	301,	289,	295,	314,	275,	348,	312,	305,	308,	295,	336,	266,
                                306,	334,	325,	288,	269,	294,	297,	282,	270,	274,	231,	245,	263,	238,	222,	210,	207,	197,
                                199,	163,	173,	188,	150,	152,	164,	146,	142,	120,	120,	120,	106,	99,	79,	98,	75,	103,
                                67,	54,	62,	69,	54,	45,	57,	54,	38,	31,	27,	34,	22,	29,	24,	16,	18,	22,
                                12,	17,	12,	14,	9,	9,	15,	8,	3,	5,	7,	4,	3,	3,	3,	3,	0,	2,
                                3,	3,	0,	1,	2,	1,	0,	0,	0,	1,])

StubsPerOrbitLS306 = np.array([ 1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
                                0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	3,	2,	3,	0,
                                2,	3,	5,	5,	9,	4,	0,	9,	4,	11,	8,	9,	9,	18,	18,	27,	24,	19,
                                21,	27,	29,	32,	46,	46,	56,	64,	54,	67,	76,	82,	69,	104,	90,	93,	110,	116,
                                114,	139,	141,	138,	150,	166,	164,	194,	183,	216,	221,	217,	234,	250,	261,	260,	295,	281,
                                285,	282,	250,	291,	265,	300,	289,	291,	312,	323,	305,	310,	302,	312,	307,	311,	333,	308,
                                300,	285,	271,	288,	294,	268,	286,	266,	263,	262,	230,	218,	242,	219,	197,	200,	180,	179,
                                186,	182,	167,	130,	133,	151,	135,	148,	101,	92,	101,	82,	86,	60,	85,	86,	57,	62,
                                43,	52,	49,	38,	47,	33,	34,	27,	27,	21,	23,	23,	20,	19,	16,	15,	17,	8,
                                9,	14,	8,	6,	5,	7,	7,	4,	7,	3,	7,	1,	4,	1,	0,	0,	2,	1,
                                0,	1,	2,	2,	1,	1,	0,	0,	0,	1,])

#importing Phi distribution per sector for each file:

PhiDistributionLS133 = ak.from_parquet('PhiDistributionLS133.parquet')
PhiDistributionLS263 = ak.from_parquet('PhiDistributionLS263.parquet')
PhiDistributionLS264 = ak.from_parquet('PhiDistributionLS264.parquet')
PhiDistributionLS306 = ak.from_parquet('PhiDistributionLS306.parquet')  


#----------------BMTF---------------------------------------------------------------------------------------

BmtfPerOrbitLS133 = np.array([1,	0,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,	0,	7,
                              4,	11,	20,	30,	61,	83,	130,	199,	278,	385,	494,	644,	726,	798,
                              961,	1044,	1067,	1172,	1201,	1131,	998,	928,	938,	800,	658,	610,	457,	385,
                              335,	229,	178,	151,	112,	82,	45,	47,	29,	17,	10,	10,	5,	1,
                              0,	1,	0,	0,	0,	0, 1])

BmtfPerOrbitLS263 = np.array([1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	
                              3,	11,	19,	22,	47,	68,	128,	170,	270,	343,	430,	585,	690,	829,	
                              891,	979,	1129,	1164,	1142,	1089,	1069,	991,	925,	779,	753,	646,	523,	426,	
                              342,	251,	223,	142,	130,	93,	47,	36,	34,	15,	14,	13,	3,	6,	
                              0,	3,	0,	0,	0,	1, 0])


BmtfPerOrbitLS264 = np.array([1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	2,	4,	
                              8,	10,	15,	29,	47,	94,	122,	208,	269,	381,	493,	565,	677,	803,	
                              928,	1041,	1069,	1120,	1137,	1082,	1115,	1019,	915,	809,	721,	634,	476,	386,	
                              296,	275,	207,	152,	108,	77,	63,	47,	21,	17,	13,	6,	6,	3,	
                              5,	1, 0, 0, 0, 0, 0])


BmtfPerOrbitLS306 = np.array([1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	
                              6,	14,	25,	45,	60,	81,	130,	187,	335,	392,	501,	612,	765,	850,	
                              984,	1032,	1100,	1190,	1184,	1153,	1046,	960,	861,	784,	652,	563,	464,	389,	
                              301,	215,	188,	112,	95,	66,	49,	27,	15,	10,	15,	6,	1,	2,	
                              2,	0,	1,	1, 0, 0, 0])


#Importing BMTF Phi distribution per sector for each file:
BmtfPhiDistributionLS133 = ak.from_parquet('BmtfPhiDistributionLS133.parquet')
BmtfPhiDistributionLS263 = ak.from_parquet('BmtfPhiDistributionLS263.parquet')
BmtfPhiDistributionLS264 = ak.from_parquet('BmtfPhiDistributionLS264.parquet')
BmtfPhiDistributionLS306 = ak.from_parquet('BmtfPhiDistributionLS306.parquet')  


#-----------------------------------DELTAR----------------------------------

BX_BMTF_LS133 = ak.from_parquet('BX_BMTF_LS133.parquet')
BX_GMT_LS133 = ak.from_parquet('BX_GMT_LS133.parquet')

BX_BMTF_LS263 = ak.from_parquet('BX_BMTF_LS263.parquet')
BX_GMT_LS263 = ak.from_parquet('BX_GMT_LS263.parquet')

BX_BMTF_LS264 = ak.from_parquet('BX_BMTF_LS264.parquet')
BX_GMT_LS264 = ak.from_parquet('BX_GMT_LS264.parquet')

BX_BMTF_LS306 = ak.from_parquet('BX_BMTF_LS306.parquet')
BX_GMT_LS306 = ak.from_parquet('BX_GMT_LS306.parquet')


#-----------------------------------PRIMO METODO----------------------------------


DeltaR_BMTF_LS133 = ak.from_parquet('DeltaR_BMTF_LS133.parquet')
IndexDist_BMTF_LS133 = ak.from_parquet('IndexDist_BMTF_LS133.parquet')

DeltaR_BMTF_LS263 = ak.from_parquet('DeltaR_BMTF_LS263.parquet')
IndexDist_BMTF_LS263 = ak.from_parquet('IndexDist_BMTF_LS263.parquet')

DeltaR_BMTF_LS264 = ak.from_parquet('DeltaR_BMTF_LS264.parquet')
IndexDist_BMTF_LS264 = ak.from_parquet('IndexDist_BMTF_LS264.parquet')

DeltaR_BMTF_LS306 = ak.from_parquet('DeltaR_BMTF_LS306.parquet')
IndexDist_BMTF_LS306 = ak.from_parquet('IndexDist_BMTF_LS306.parquet')


DeltaPhi_BMTF_LS133 = ak.from_parquet('DeltaPhi_BMTF_LS133.parquet')
DeltaEta_BMTF_LS133 = ak.from_parquet('DeltaEta_BMTF_LS133.parquet')

DeltaPhi_BMTF_LS263 = ak.from_parquet('DeltaPhi_BMTF_LS263.parquet')  
DeltaEta_BMTF_LS263 = ak.from_parquet('DeltaEta_BMTF_LS263.parquet')

DeltaPhi_BMTF_LS264 = ak.from_parquet('DeltaPhi_BMTF_LS264.parquet')  
DeltaEta_BMTF_LS264 = ak.from_parquet('DeltaEta_BMTF_LS264.parquet')

DeltaPhi_BMTF_LS306 = ak.from_parquet('DeltaPhi_BMTF_LS306.parquet')  
DeltaEta_BMTF_LS306 = ak.from_parquet('DeltaEta_BMTF_LS306.parquet')



#-----------------------------------SECONDO METODO------------------------------------


'''DeltaR_GMT_LS133 = ak.from_parquet('DeltaR_GMT_LS133.parquet')
IndexDist_GMT_LS133 = ak.from_parquet('IndexDist_GMT_LS133.parquet')

DeltaR_GMT_LS263 = ak.from_parquet('DeltaR_GMT_LS263.parquet')
IndexDist_GMT_LS263 = ak.from_parquet('IndexDist_GMT_LS263.parquet')

DeltaR_GMT_LS264 = ak.from_parquet('DeltaR_GMT_LS264.parquet')
IndexDist_GMT_LS264 = ak.from_parquet('IndexDist_GMT_LS264.parquet')

DeltaR_GMT_LS306 = ak.from_parquet('DeltaR_GMT_LS306.parquet')
IndexDist_GMT_LS306 = ak.from_parquet('IndexDist_GMT_LS306.parquet')


DeltaPhi_GMT_LS133 = ak.from_parquet('DeltaPhi_GMT_LS133.parquet')
DeltaEta_GMT_LS133 = ak.from_parquet('DeltaEta_GMT_LS133.parquet')

DeltaPhi_GMT_LS263 = ak.from_parquet('DeltaPhi_GMT_LS263.parquet')  
DeltaEta_GMT_LS263 = ak.from_parquet('DeltaEta_GMT_LS263.parquet')

DeltaPhi_GMT_LS264 = ak.from_parquet('DeltaPhi_GMT_LS264.parquet')  
DeltaEta_GMT_LS264 = ak.from_parquet('DeltaEta_GMT_LS264.parquet')

DeltaPhi_GMT_LS306 = ak.from_parquet('DeltaPhi_GMT_LS306.parquet')  
DeltaEta_GMT_LS306 = ak.from_parquet('DeltaEta_GMT_LS306.parquet')'''

										
														