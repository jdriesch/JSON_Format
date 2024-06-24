import correctionlib
import correctionlib.schemav2 as cs

### XY Correction for Type 1 PuppiMET for MC/simulation ###

metphicorrs = {}
metphicorrs["2016pre"] = {}
metphicorrs["2016post"] = {}
metphicorrs["2017"] = {}
metphicorrs["2018"] = {}
metphicorrs["2022"] = {}

## x component parameters ##

# 2016
metphicorrs["2016pre"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0060447, -0.4183])
metphicorrs["2016post"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0058341, -0.395049])

# 2017
metphicorrs["2017"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0102265, -0.446416])

# 2018
metphicorrs["2018"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.0214557, 0.969428])

# 2022
metphicorrs["2022"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.01443466593328702, 0.04973783245185093])
metphicorrs["2022EE"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.014672807819263556, -0.04206561549444332])

# 2023
metphicorrs["2023"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.012674500133014733, 0.3867591787788066])
metphicorrs["2023BPix"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.01074787017306211, 0.5514723089759307])

## y component parameters ##

# 2016
metphicorrs["2016pre"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.008331, -0.0990046])
metphicorrs["2016post"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00971595, -0.101288])

# 2017
metphicorrs["2017"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0198663, 0.243182])

# 2018
metphicorrs["2018"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0167134, 0.199296])

# 2022
metphicorrs["2022"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.012336930168278634, -0.19235680753907328])
metphicorrs["2022EE"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.012261639434061555, -0.07309295607006527])

# 2023
metphicorrs["2023"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.007690465903616379, -0.31251132099008483])
metphicorrs["2023BPix"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.004976252168728055, -0.5944404275383195])

for era in metphicorrs.keys():
    metphicorrs[era]["xy"] = [
        cs.FormulaRef(
            nodetype="formularef",
            index=0,
            parameters=(metphicorrs[era]["x"].parameters + metphicorrs[era]["y"].parameters),
        )
    ]
