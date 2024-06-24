import correctionlib
import correctionlib.schemav2 as cs

### XY Correction for Type 1 PFMET for MC/simulation ###

metphicorrs = {}
metphicorrs["2016pre"] = {}
metphicorrs["2016post"] = {}
metphicorrs["2017"] = {}
metphicorrs["2018"] = {}
metphicorrs["2022"] = {}

## x component parameters ##

# 2016
metphicorrs["2016pre"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.188743, 0.136539])
metphicorrs["2016post"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.153497, -0.231751])

# 2017
metphicorrs["2017"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.300155, 1.90608])

# 2018
metphicorrs["2018"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.183518, 0.546754])

# 2022
metphicorrs["2022"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.01772689514798973, 0.04753174170384164])
metphicorrs["2022EE"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[-0.02642415422343397, -0.020232141962834738])

# 2022
metphicorrs["2023"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.10088891788829228, -0.7475659408557478])
metphicorrs["2023BPix"]["x"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.2082519883008424, -1.4097156316653972])

## y component parameters ##

# 2016
metphicorrs["2016pre"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.0127927, 0.117747])
metphicorrs["2016post"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.00731978, 0.243323])

# 2017
metphicorrs["2017"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.300213, -2.02232])

# 2018
metphicorrs["2018"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.192263, -0.42121])

# 2022
metphicorrs["2022"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.056834368394435106, -0.44059927526774245])
metphicorrs["2022EE"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.06299345726816344, -0.3550646979517613])

# 2023
metphicorrs["2023"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.056834368394435106, -0.44059927526774245])
metphicorrs["2023BPix"]["y"] = cs.FormulaRef(nodetype="formularef", index=0, parameters=[0.020103535533303542, -0.23468171647072067])

for era in metphicorrs.keys():
    metphicorrs[era]["xy"] = [
        cs.FormulaRef(
            nodetype="formularef",
            index=0,
            parameters=(metphicorrs[era]["x"].parameters + metphicorrs[era]["y"].parameters),
        )
    ]
