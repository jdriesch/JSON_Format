import correctionlib
import correctionlib.schemav2 as cs

### XY Correction for Type 1 PFMET for data ###

## x component parameters ##

# 2016
metphicorr_x_2016B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0214894, -0.188255])
metphicorr_x_2016C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.032209, 0.067288])
metphicorr_x_2016D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0293663, 0.21106])
metphicorr_x_2016E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0132046, 0.20073])
metphicorr_x_2016Fpre = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0543566, 0.816597])
metphicorr_x_2016Fpost = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.134616, -0.89965])
metphicorr_x_2016G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.121809, -0.584893])
metphicorr_x_2016H = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0868828, -0.703489])

# 2017
metphicorr_x_2017B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.211161, 0.419333])
metphicorr_x_2017C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.185184, -0.164009])
metphicorr_x_2017D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.201606, 0.426502])
metphicorr_x_2017E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.162472, 0.176329])
metphicorr_x_2017F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.210639, 0.72934])

# 2018
metphicorr_x_2018A = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.263733, -1.91115])
metphicorr_x_2018B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.400466, -3.05914])
metphicorr_x_2018C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.430911, -1.42865])
metphicorr_x_2018D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.457327, -1.56856])

# 2022
metphicorr_x_2022B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.24142103618583782, 2.040889031918197])
metphicorr_x_2022C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.030994791453450823, 0.7152042113530935])
metphicorr_x_2022D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.03206394689755019, 1.2226345322125434])
metphicorr_x_2022E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.02335658874327786, 1.428565843048412])
metphicorr_x_2022F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.11118833840959408, 3.0537881848031345])
metphicorr_x_2022G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.006651637239782335, 5.566080896776024])

# 2022 pre/post EE
metphicorr_x_2022 = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.03780245575074215, 0.8504827451405943])
metphicorr_x_2022EE = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.03146513664247987, 0.5729596293408936])

# 2023 pre/post BPix
metphicorr_x_2023 = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.5111507976792302, 0.19690479488604673])
metphicorr_x_2023BPix = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.6766228566652093, 1.1632441414174863])


## y component parameters ##

# 2016
metphicorr_y_2016B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0876624, 0.812885])
metphicorr_y_2016C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.113917, 0.743906])
metphicorr_y_2016D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.11331, 0.815787])
metphicorr_y_2016E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.134809, 0.679068])
metphicorr_y_2016Fpre = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.114225, 1.17266])
metphicorr_y_2016Fpost = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0397736, 1.0385])
metphicorr_y_2016G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0558974, 0.891234])
metphicorr_y_2016H = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0888774, 0.902632])

# 2017
metphicorr_y_2017B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.251789, -1.28089])
metphicorr_y_2017C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.200941, -0.56853])
metphicorr_y_2017D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.188208, -0.58313])
metphicorr_y_2017E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.138076, -0.250239])
metphicorr_y_2017F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.198626, 1.028])

# 2018
metphicorr_y_2018A = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0431304, -0.112043])
metphicorr_y_2018B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.146125, -0.533233])
metphicorr_y_2018C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0620083, -1.46021])
metphicorr_y_2018D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0684071, -0.928372])

# 2022
metphicorr_y_2022B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.28199237695576107, -0.8883906768633341])
metphicorr_y_2022C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.40299133310238067, 0.7065456749516565])
metphicorr_y_2022D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.41664235528283355, 0.7546131376433154])
metphicorr_y_2022E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.40314189672120515, 1.5730249641164287])
metphicorr_y_2022F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.40010467568084257, -0.9053648743259854])
metphicorr_y_2022G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.35975707985462646, -3.746154161096965])

# 2022 pre/post EE
metphicorr_y_2022 = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.40310941958279956, 0.7187285447907721])
metphicorr_y_2022EE = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.47324701571928884, 1.434125244394413])

# 2023 pre/post BPix
metphicorr_x_2023 = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.321177598853787, -1.330247672084286])
metphicorr_x_2023BPix = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.45429103984891567, 0.33115866520703285])

no_correction = cs.FormulaRef(nodetype="formularef", index=1, parameters=[1.0])

edges = {}
edges["2016pre"] = [0, 272007, 275377, 275657, 276284, 276315, 276812, 276831, 277421, 277772, 278769, 278770, 278771]
edges["2016post"] = [0, 278769, 278770, 278771, 278801, 278809, 278820, 280386, 280919, 284045]
edges["2017"] = [0, 297020, 299330, 299337, 302030, 303435, 304827, 304911, 306463]
edges["2018"] = [0, 315252, 316996, 316998, 319313, 320394, 325274]
edges["2022"] = [0, 355862, 357482, 357538, 357900, 359022, 360331, 360390, 362167, 362433, 362760]
edges["2022"] = [0, 355100, 355769, 355862, 357482, 357538, 357900, 359022, 360331, 360390, 362167, 362433, 362760]

metphicorrs = {}
metphicorrs["2016pre"] = {}
metphicorrs["2016post"] = {}
metphicorrs["2017"] = {}
metphicorrs["2018"] = {}
metphicorrs["2022"] = {}
metphicorrs["2016pre"]["x"] = [
    no_correction,
    metphicorr_x_2016B,
    no_correction,
    metphicorr_x_2016C,
    no_correction,
    metphicorr_x_2016D,
    no_correction,
    metphicorr_x_2016E,
    no_correction,
    metphicorr_x_2016Fpre,
    no_correction,
    metphicorr_x_2016Fpre,
]
metphicorrs["2016post"]["x"] = [
    no_correction,
    metphicorr_x_2016Fpost,
    no_correction,
    no_correction,
    metphicorr_x_2016Fpost,
    no_correction,
    metphicorr_x_2016G,
    no_correction,
    metphicorr_x_2016H,
]
metphicorrs["2017"]["x"] = [
    no_correction,
    metphicorr_x_2017B,
    no_correction,
    metphicorr_x_2017C,
    metphicorr_x_2017D,
    metphicorr_x_2017E,
    no_correction,
    metphicorr_x_2017F,
]
metphicorrs["2018"]["x"] = [
    no_correction,
    metphicorr_x_2018A,
    no_correction,
    metphicorr_x_2018B,
    metphicorr_x_2018C,
    metphicorr_x_2018D,
]
metphicorrs["2022"]["x"] = [
    no_correction,
    metphicorr_x_2022B,
    no_correction,
    metphicorr_x_2022C,
    no_correction,
    metphicorr_x_2022D,
    no_correction,
    metphicorr_x_2022E,
    no_correction,
    metphicorr_x_2022F,
    no_correction,
    metphicorr_x_2022G,
]
metphicorrs["2016pre"]["y"] = [
    no_correction,
    metphicorr_y_2016B,
    no_correction,
    metphicorr_y_2016C,
    no_correction,
    metphicorr_y_2016D,
    no_correction,
    metphicorr_y_2016E,
    no_correction,
    metphicorr_y_2016Fpre,
    no_correction,
    metphicorr_y_2016Fpre,
]
metphicorrs["2016post"]["y"] = [
    no_correction,
    metphicorr_y_2016Fpost,
    no_correction,
    no_correction,
    metphicorr_y_2016Fpost,
    no_correction,
    metphicorr_y_2016G,
    no_correction,
    metphicorr_y_2016H,
]
metphicorrs["2017"]["y"] = [
    no_correction,
    metphicorr_y_2017B,
    no_correction,
    metphicorr_y_2017C,
    metphicorr_y_2017D,
    metphicorr_y_2017E,
    no_correction,
    metphicorr_y_2017F,
]
metphicorrs["2018"]["y"] = [
    no_correction,
    metphicorr_y_2018A,
    no_correction,
    metphicorr_y_2018B,
    metphicorr_y_2018C,
    metphicorr_y_2018D,
]
metphicorrs["2022"]["y"] = [
    no_correction,
    metphicorr_y_2022B,
    no_correction,
    metphicorr_y_2022C,
    no_correction,
    metphicorr_y_2022D,
    no_correction,
    metphicorr_y_2022E,
    no_correction,
    metphicorr_y_2022F,
    no_correction,
    metphicorr_y_2022G,
]

for era in metphicorrs.keys():
    metphicorrs[era]["xy"] = []
    for i in range(len(metphicorrs[era]["x"])):
        if metphicorrs[era]["x"][i].index == 1 and metphicorrs[era]["y"][i].index == 1:
            metphicorrs[era]["xy"].append(no_correction)
        elif metphicorrs[era]["x"][i].index == 0 and metphicorrs[era]["y"][i].index == 0:
            metphicorrs[era]["xy"].append(
                cs.FormulaRef(
                    nodetype="formularef",
                    index=0,
                    parameters=(metphicorrs[era]["x"][i].parameters + metphicorrs[era]["y"][i].parameters),
                )
            )
        else:
            print("Something is wrong with the corretion formulas, please check!")
            exit()
