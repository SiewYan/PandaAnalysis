variable = {}

var_template = {
 "EventNumber": {
      "title" : "event number",
      "nbins" : 10000000,
      "min" : 0,
      "max" : 1.e7,
      "log" : False,
    },
    "pfmet": {
      "title" : "PFMET [GeV]",
#      "nbins" : -1,
#      "bins" : [250,270,350,475,1000],
      "nbins" : 50,
      "min" : 0,
      "max" : 1500,
      "log" : False,
    },
   "nJets": {
      "title" : "number of jets",
      "nbins" : 10,
      "min" : -0.5,
      "max" : 9.5,
      "log" : True,
    },
   "Jet[N].CSVRUp": {
      "title" : "jet [N] CSV (+1 #sigma)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
 "fj1MSD": {
        "title" : "fatjet m_{SD} [GeV]",
        #"nbins" : -1,
        #"bins" : [50,75,100,150,300],
        "nbins" : 30, 
        "min" : 0,
        "max" : 150,
#        "nbins" : 80,
#        "min" : 0,
#        "max" : 4000,  
        "log" : True,
        },
 "genMjj": {
        "title" : "number of jets",
        "nbins" : 10,
        "min" : 0,
        "max" : 150,
        "log" : True,
        },
 "genBosonPt": {
        "title" : "Gen boson pt",
        "nbins" : 50,
        "min" : 250,
        "max" : 1000,
        "log" : True,
        },
 "fj1Pt": {
        "title" : "fatjet pt [GeV]",
        "nbins" : 50,
        "min" : 0,
        "max" : 1500,
        "log" : True,
        }
 }

for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(1, 5):
            ni = n.replace('[N]', "%d" % i)
            variable[ni] = v.copy()
            variable[ni]['title'] = variable[ni]['title'].replace('[N]', "%d" % i)
    else:
        variable[n] = v

#print variable
'''
    elif n.startswith('H.'):
        variable[n] = v
        variable[n.replace('H.', 'HMerged.')] = v.copy()
        variable[n.replace('H.', 'HResolved.')] = v.copy()
        variable[n.replace('H.', 'HResolvedHpt.')] = v.copy()
    elif n.startswith('X.'):
        variable[n] = v
        variable[n.replace('X.', 'XMerged.')] = v.copy()
        variable[n.replace('X.', 'XResolved.')] = v.copy()
        variable[n.replace('X.', 'XResolvedHpt.')] = v.copy()
    else:
        variable[n] = v
'''
