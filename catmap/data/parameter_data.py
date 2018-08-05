#Define default shomate parameters
shomate_params = {}
shomate_params['H2_g:298-1000'] = [33.066178,-11.363417,11.432816,
        -2.772874,-0.158558,-9.980797,172.707974,0] #NIST
shomate_params['H2_g:1000-2500'] = [18.563083,12.257357,-2.859786,
        0.268238,1.977990,-1.147438,156.288133,0] #NIST
shomate_params['H2_g:2500-6000'] = [43.413560,-4.293079,1.272428,
        -0.096876,-20.533862,-38.515158,162.081354,0] #NIST
shomate_params['CH4_g:298-1300'] = [-0.703029,108.4773,-42.52157,
        5.862788,0.678565,-76.84376,158.7163,-74.87310] #NIST
shomate_params['CH4_g:1300-1600'] = [85.81217,11.26467,-2.114146,
        0.138190,-26.42221,-153.5327,224.4143,-74.87310] #NIST
shomate_params['CO_g:298-1300'] = [25.56759,6.096130,4.054656,
        -2.671201,0.131021,-118.0089,227.3665,-110.5271] #NIST
shomate_params['CO_g:1300-1600'] = [35.15070,1.300095,-0.205921,
        0.013550,-3.282780,-127.8375,231.7120,-110.5271] #NIST
shomate_params['H2O_g:100-500'] = [36.303952, -24.11232, 63.64111, 
        -38.9524, -0.01385, -10.23966, 237.39431, 0.0] #Fitted to JANAF
shomate_params['H2O_g:500-1700'] = [30.09200,6.832514,6.793435,-2.534480,
        0.082139,-250.8810,223.3967,-241.8264] #NIST
shomate_params['H2O_g:1700-6000'] = [41.96426,8.622053,-1.499780,0.098119,
        -11.15764,-272.1797,219.7809,-241.8264] #NIST
shomate_params['CO2_g:298-1200'] = [24.99735,55.18696,-33.69137,7.948387,
        -0.136638,-403.6075,228.2431,-393.5224] #NIST 
shomate_params['CO2_g:1200-6000'] = [58.16639,2.720075,-0.492289,0.038844,
        -6.447293,-425.9186,263.6125,-393.5224] #NIST
shomate_params['O2_g:100-700'] = [31.32234,-20.23531,57.8664,-36.50624,
        -0.007374,-8.903471,246.7945,0.0] #NIST
shomate_params['O2_g:700-2000'] = [30.03235,8.772972,-3.988133,0.788313,
        -0.741599,-11.32468,236.1663,0.0] #NIST
shomate_params['O2_g:2000-6000'] = [20.91111,10.72071,-2.020498,0.146449,
        9.245722,5.337651,237.6185,0.0] #NIST
shomate_params['NH3_g:298-1400'] = [19.99563,49.77119,-15.37599,1.921168,
        0.189174,-53.30667,203.8591,-45.89806] #NIST
shomate_params['N2_g:100-500'] = [28.98641,1.853978,-9.647459,16.63537,
        0.000117,-8.671914,226.4168,0.0] #NIST
shomate_params['N2_g:500-2000'] = [19.50583,19.88705,-8.598535,1.369784,
        0.527601,-4.935202,212.3900,0.0] #NIST
shomate_params['N2O_g:298-1400'] = [27.67988,51.14898,-30.64454,6.847911,
        -0.157906,71.24934,238.6164,82.04824] #NIST
shomate_params['NO2_g:298-1200'] = [16.10857,75.89525,-54.38740,14.30777,
        0.239423,26.17464,240.5386,33.09502] #NIST
shomate_params['NO_g:298-1200'] = [23.83491,12.58878,-1.139011,-1.497459,
        0.214194,83.35783,237.1219,90.29114] #NIST
shomate_params['NO3_g:298-1200'] = [11.22316,166.3889,-148.4458,47.40598,
            -0.176791,61.00858,221.7679,71.12800] #NIST
shomate_params['HNO2_g:298-1200'] = [24.89974,91.37563,-64.84614,17.92007,
            -0.134737,-88.13596,254.2671,-76.73498] #NIST
shomate_params['HNO3_g:298-1200'] = [19.63229,153.9599,-115.8378,32.87955,
        -0.249114,-146.8818,247.7049,-134.3060] #NIST
shomate_params['HCN_g:298-1200'] = [32.69373,22.59205,-4.369142,-0.407697,
        -0.282399,123.4811,233.2597,135.1432] #NIST
shomate_params['CH2CH2_g:298-1200'] = [-6.387880,184.4019,-112.9718,
        28.49593,0.315540,48.17332,163.1568,52.46694] #NIST
shomate_params['CH2O_g:298-1500'] = [5.193767,93.23249,-44.85457,7.882279,
        0.551175,-119.3591,202.4663,-115.8972] #NIST
shomate_params['CH3OH_g:298-1500'] = [-1.0845814245433651, 153.2463565199489, 
        -79.530503596182541, 16.471302393160109, 0.52203346015332153, 
        -4.897417024069, 199.18937455061121, 0.0]
shomate_params['C5H4O2_g:100-1500'] = [-16.36694, 0.46958, -0.000331925,
        0.0000000850912, 198590.9145, -1661.34999, -15.68938, 12461.34999] #Added by N. Shan, KSU from NIST/CRC
shomate_params['C5H6O2_g:100-1500'] = [-18.57626, 0.50733, -0.000335824, 0.0000000828263,
        231619.2141, -6357.53523, 2.75692, 7057.53523] #Added by N. Shan, KSU from NIST/CRC
shomate_params['C5H6O_g:50-1500'] = [1.26847, 0.35388, -0.000173962, 0.0000000287427,
        48401.71207, -5691.94893, -85.38991, 7191.94893] #Added by N. Shan, KSU from NIST/CRC
shomate_params['Cl2_g:298-1000'] = [33.05060, 12.22940, -12.06510, 4.385330, -0.159494,
        -10.83480, 259.0290, 0.000000] #Added by M. Andersen, TUM from NIST
shomate_params['HCl_g:298-1200'] = [32.12392, -13.45805, 19.86852, -6.853936, -0.049672,
        -101.6206, 228.6866, -92.31201] #Added by M. Andersen, TUM from NIST
#Fitted to values from CRC Handbook of Chemistry and Physics 91st Ed.
#H constrained to 0
shomate_params['CH3CH2OH_g:298-1500'] = [-4.7367880805894265, 271.96181550301463, 
        -169.34946529216657, 43.738601536085334, 0.24643430702178773, 
        -9.8282808291878609, 203.33256226170749, 0.0]
#Fitted to values from CRC Handbook of Chemistry and Physics 91st Ed.
#H constrained to 0
shomate_params['CH3CHO_g:298-1500'] = [4.8037386340099095, 185.92002366990326, 
        -99.108461090201203, 20.614739190690159, 0.27708025485586463, 
        -8.5666000407909451, 220.00244674443837, 0.0]
#Fitted to values from CRC Handbook of Chemistry and Physics 91st Ed.
#H constrained to 0
shomate_params['HCOOH_g:298-1500'] = [3.8027523042252258, 
        153.66217894746168, -84.640467738169264, 16.297377707561505, 
        0.27720649972633382, -6.16527, 212.9698972559699, 0] 
#Fitted to values from Chao et. al. as referenced in NIST.
#H constrained to 0


#Define default ideal gas parameters
ideal_gas_params = {
        'H2_g':[2,'linear',0],
        'N2_g':[2,'linear',0],
        'O2_g':[2,'linear',1.0],
        'H2O_g':[2,'nonlinear',0],
        'CO_g':[1,'linear',0],
        'CH4_g':[12,'nonlinear',0],
        'NH3_g':[3,'nonlinear',0],
        'CH3OH_g':[1,'nonlinear',0],
        'CH3CH2OH_g':[1,'nonlinear',0],
        'CO2_g':[2,'linear',0],
        'CH2O_g':[2,'nonlinear',0],
        'HCOOH_g':[1,'nonlinear',0],
        'CH2CH2_g':[4,'nonlinear',0],
        'CH3CHCH2_g':[1,'nonlinear',0], #propene
        'CH3CH2CHCH2_g':[1,'nonlinear',0], #1-butene
        'CH3CHCHCH3_g':[2,'nonlinear',0], #2-butene, ok for both trans and cis
        'CH3CH3CCH2_g':[2,'nonlinear',0], #isobutene
        'pe_g':[2,'linear',0], # fictitious gas molecule corresponding to proton electron pair
        'C2H2_g':[2,'linear',0],
        'C2H4_g':[4,'nonlinear',0],
        'C2H6_g':[6,'nonlinear',0],
        'C3H6_g':[1,'nonlinear',0],
        'CH3COOH_g':[1,'nonlinear',0],
        'CH3CHO_g':[1,'nonlinear',0],
        'C5H4O2_g':[1,'nonlinear',0], #Added by N. Shan, KSU from NIST/CRC
        'C5H6O2_g':[1,'nonlinear',0], #Added by N. Shan, KSU from NIST/CRC
        'C5H6O_g':[1,'nonlinear',0], #Added by N. Shan, KSU from NIST/CRC
        'HCl_g':[1,'linear',0], #Added by M. Andersen, TUM from NIST
        'Cl2_g':[2,'linear',0], #Added by M. Andersen, TUM from NIST
        }

#Define default fixed entropy gas entropies
fixed_entropy_dict = {'H2_g':0.00135,
        'other':0.002
        } 

experimental_gas_frequencies = {'CO_g':[2170], #from CCCBDB, NIST webbook, or CRC
        'H2_g':[4401],
        'N2_g':[2359],
        'NO_g':[1904],
        'NO2_g':[1318,1618,750],
        'N2O_g':[2224,1285,589],
        'NH3_g':[3337,950,3444,3444,1627,1627],
        'CO2_g':[1333,2349,667,667],
        'H2O_g':[3657,1595,3756],
        'CH3OH_g':[3681,3000,2844,1477,1455,1345,1060,1033,2960,1477,1165,200],
        'O2_g':[1580],
        'CH4_g':[2917,1534,1534,3019,3019,3019,1306,1306,1306],
        'HCOOH_g':[3570,2943,1770,1387,1229,1105,625,1033,638],
        'CH2O_g':[2783,1746,1500,2843,1249,1167],
        'CH3CH2OH_g':[3653,2984,2939,2900,1490,1464,1412,1371,1256,1091,1028,
            888,417,2991,2910,1446,1275,1161,812],
        'C2H4_g':[3026,1623,1342,1023,3103,1236,949,943,3106,826,2989,1444],
        'C2H6_g':[2954,1388,995,289,2896,1379,2969,2969,1468,1468,1190,1190,2985,2985,1469,1469,822,822],
        'CH3COOH_g':[3583,3051,2944,1788,1430,1382,1264,1182,989,847,657,581,2996,1430,1048,642,534,93],
        'CH3CHO_g':[3005,2917,2822,1743,1441,1400,1352,1113,919,509,2967,1420,867,763,150],
        }

#Define experimental gas formation energies (accessed via CCCBDB; corrected for 
#zero-point energy, enthalpy due to cpdT, etc. should be directly comparable
#to first-principles calculations of potential energy due to electrons @ 0K)


experimental_gas_formation_energies = {
    'CH3OCH3': -3.831687734, 
    'isobutene': -2.7612012400000001, 
    'CH3CH2OH': -4.3257274452000001, 
    'H2CCO': -1.2932338992999999, 
    'CH3COOH': -5.936414407, 
    'butadiene': -0.94117440899999982, 
    'CH3NO2': -1.9433241520000002, 
    'CH2NHCH2': -0.37361471699999993, 
    'C3H8': -3.5838955599999998, 
    'CH3OH': -3.3154954364, 
    'CH2OCH2': -0.70501341749999991, 
    'CCH': 5.4911384108000005, 
    'CH3CH2NH2': -2.7060065129999997, 
    'N2O': 0.59071737410000003, 
    'C3H6_Cs': -1.7302961269999999, 
    'O3': 1.3200076574999999, 
    'O2': -0.097959758399999999, 
    'NO2': 0.15269533860000001, 
    'CH2_s1A1d': 3.6179179609999998, 
    'NH': 3.5110470303999999, 
    'NCCN': 2.7613439944999998, 
    'CH3O': -0.57019516400000003, 
    'H2O2': -2.0341974058000001, 
    'cyclobutene': -0.49233188199999978, 
    'NO': 0.8203358394000001, 
    'OCHCHO': -3.1146914399999996, 
    'cyclobutane': -2.3477410291999998, 
    'CH3CN': -0.45205272699999999, 
    'C2H2': 1.6608275572000002, 
    'CH3': 0.7658170968000001, 
    'CH4': -1.8659396301, 
    'CH3COCH3': -4.2818641334, 
    'CH': 5.9634832613999995, 
    'CO': -1.3140678102999999, 
    'CN': 4.4009493388000003, 
    'isobutane': -4.5367431759999999, 
    'C4H4O': -2.0735235359999997, 
    'C3H4_C3v': 0.52048922799999997, 
    'NH3': -1.2981708845000002, 
    'NH2': 1.4628439994, 
    'CH3CHO': -3.1157422380000002, 
    'C2H6': -2.6688338305999997, 
    'N2': -0.14621433119999999, 
    'C2H4': -0.70501341749999991, 
    'HCN': 0.94892666259999991, 
    'HCO': 0.097736827300000051, 
    'CH3CONH2': -4.2117845308000001, 
    'H3CNH2': -1.7742767699999999, 
    'CO2': -4.3855609798000001, 
    'OH': 0.1529043621, 
    'H2': -0.27283919039999999, 
    'methylenecyclopropane': 0.0057401610000002989, 
    'C6H6': -1.6117550120000002, 
    'N2H4': -0.25599903979999983, 
    'C4H4NH': -0.88607863680000021, 
    'H2O': -3.0344480389999999, 
    'H2CCHCN': 0.60457370399999988, 
    'HCOOH': -4.7369155476999998, 
    'H2CO': -1.7865010562000001, 
    'graphite':-0.1596,
    }
