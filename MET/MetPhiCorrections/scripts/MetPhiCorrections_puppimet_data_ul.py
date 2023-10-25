import correctionlib
import correctionlib.schemav2 as cs

### XY Correction for Type 1 PuppiMET for data ###

## x component parameters ##

# 2016
metphicorr_x_2016B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00109025, -0.338093])
metphicorr_x_2016C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00271913, -0.342268])
metphicorr_x_2016D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00254194, -0.305264])
metphicorr_x_2016E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00358835, -0.225435])
metphicorr_x_2016Fpre = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0056759, -0.454101])
metphicorr_x_2016Fpost = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0234421, -0.371298])
metphicorr_x_2016G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0182134, -0.335786])
metphicorr_x_2016H = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.015702, -0.340832])

# 2017
metphicorr_x_2017B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00382117, -0.666228])
metphicorr_x_2017C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00110699, -0.747643])
metphicorr_x_2017D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00141442, -0.721382])
metphicorr_x_2017E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00593859, -0.851999])
metphicorr_x_2017F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00765682, -0.945001])

# 2018
metphicorr_x_2018A = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0073377, 0.0250294])
metphicorr_x_2018B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00434261, 0.00892927])
metphicorr_x_2018C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00198311, 0.37026])
metphicorr_x_2018D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00220647, 0.378141])

# 2022 CDE rereco and FG promptreco
metphicorr_x_2022C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.02343353907997924, 0.22983049326023777])
metphicorr_x_2022D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.024782556389225573, 0.3124258311274861])
metphicorr_x_2022E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.023365501743318112, 0.16512637085215365])
metphicorr_x_2022F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.02963723119039856, 0.3651770068990192])
metphicorr_x_2022G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.018934076357252076, 0.6567964602889391])

## y component parameters ##

# 2016
metphicorr_y_2016B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00356058, 0.128407])
metphicorr_y_2016C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00187386, 0.104])
metphicorr_y_2016D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00177408, 0.164639])
metphicorr_y_2016E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.000444268, 0.180479])
metphicorr_y_2016Fpre = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00962707, 0.35731])
metphicorr_y_2016Fpost = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00997438, 0.0809178])
metphicorr_y_2016G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0063338, 0.093349])
metphicorr_y_2016H = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00544957, 0.199093])

# 2017
metphicorr_y_2017B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0109034, 0.172188])
metphicorr_y_2017C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0012184, 0.303817])
metphicorr_y_2017D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0011873, 0.21646])
metphicorr_y_2017E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.00754254, 0.245956])
metphicorr_y_2017F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0154974, 0.804176])

# 2018
metphicorr_y_2018A = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.000406059, 0.0417346])
metphicorr_y_2018B = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00234695, 0.20381])
metphicorr_y_2018C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.016127, 0.402029])
metphicorr_y_2018D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0160244, 0.471053])

# 2022 CDE rereco and FG promptreco
metphicorr_y_2022C = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0512023304132463, -0.3285138764759885])
metphicorr_y_2022D = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.06388650218535215, -0.15596543984177458])
metphicorr_y_2022E = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.05132197227502938, 0.06940200548340325])
metphicorr_y_2022F = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.06930780993055984, 0.06041592719059796])
metphicorr_y_2022G = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.04860184714111235, -0.2193388863252732])

no_correction = cs.FormulaRef(nodetype="formularef", index=1, parameters=[1.0])

edges = {}
edges["2016pre"] = [0, 272007, 275377, 275657, 276284, 276315, 276812, 276831, 277421, 277772, 278769, 278770, 278771]
edges["2016post"] = [0, 278769, 278770, 278771, 278801, 278809, 278820, 280386, 280919, 284045]
edges["2017"] = [0, 297020, 299330, 299337, 302030, 303435, 304827, 304911, 306463]
edges["2018"] = [0, 315252, 316996, 316998, 319313, 320394, 325274]
edges["2022"] = [0, 355862, 357482, 357538, 357900, 359022, 360331, 360390, 362167, 362433, 362760]

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
