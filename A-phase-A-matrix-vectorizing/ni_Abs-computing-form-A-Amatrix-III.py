# trace generated using paraview version 5.13.3
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Image Data Reader'
piopvti = XMLPartitionedImageDataReader(registrationName='pio.pvti', FileName=['./pio.pvti'])

# Properties modified on piopvti
piopvti.CellArrayStatus = []
piopvti.PointArrayStatus = ['gapA','u11','u12','u13','u21','u22','u23','u31','u32','u33','v11','v12','v13','v21','v22','v23','v31','v32','v33']
piopvti.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=piopvti)

print("*vti files loaded. \n")

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=piopvti)

# Properties modified on threshold1, gapA * (1+/-0.01)
threshold1.Scalars = ['POINTS', 'gapA']
threshold1.LowerThreshold = 1.8599618128954347
threshold1.UpperThreshold = 1.8975367990145346

UpdatePipeline(time=0.0, proxy=threshold1)

print("Threshold pipe line done! \n")

##########################################
## use threshold to clip dinominator!=0 ##
##########################################

# # create a new 'Calculator', abs(dinominator)
# calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
# # Properties modified on calculator1
# calculator1.ResultArrayName = 'Abs_Dino'
# calculator1.Function = 'abs((u11^2)*(v12^2)*(v13^2)*(v21^2)*(v31^2)*(-(u22^2)*(u33^2)*(v23^2)*(v32^2)+(u23^2)*(u32^2)*(v22^2)*(v33^2))+(v11^2)*((u13^2)*(v12^2)*(v23^2)*(-(u21^2)*(u32^2)*(v22^2)*(v31^2)+(u22^2)*(u31^2)*(v21^2)*(v32^2))*(v33^2)+(u12^2)*(v13^2)*(v22^2)*(v32^2)*((u21^2)*(u33^2)*(v23^2)*(v31^2)-(u23^2)*(u31^2)*(v21^2)*(v33^2))))'
# UpdatePipeline(time=0.0, proxy=calculator1)

# print("compute Abs(dinominator) done! \n")

# # create a new 'Threshold', Abs_Dino > 10^-9
# threshold2 = Threshold(registrationName='Threshold2', Input=calculator1)

# # Properties modified on threshold2,
# threshold2.Scalars = ['POINTS', 'Abs_Dino']
# threshold2.UpperThreshold = 0.0000000001
# threshold2.ThresholdMethod = 'Above Upper Threshold'

# UpdatePipeline(time=0.0, proxy=threshold2)

# print("Threshold clip dinominator!=0 done! \n")


##########################################
##    clip dinominator!=0 ends here     ##
##########################################

#################################
##       ni^2 computing        ##
#################################

# All ni^2 have same dinominator:
# (u11^2)*(v12^2)*(v13^2)*(v21^2)*(v31^2)*(-(u22^2)*(u33^2)*(v23^2)*(v32^2)+(u23^2)*(u32^2)*(v22^2)*(v33^2))+(v11^2)*((u13^2)*(v12^2)*(v23^2)*(-(u21^2)*(u32^2)*(v22^2)*(v31^2)+(u22^2)*(u31^2)*(v21^2)*(v32^2))*(v33^2)+(u12^2)*(v13^2)*(v22^2)*(v32^2)*((u21^2)*(u33^2)*(v23^2)*(v31^2)-(u23^2)*(u31^2)*(v21^2)*(v33^2)))
# (u11^2)*(v12^2)*(v13^2)*(v21^2)*(v31^2)*(-(u22^2)*(u33^2)*(v23^2)*(v32^2)+(u23^2)*(u32^2)*(v22^2)*(v33^2))+(v11^2)*((u13^2)*(v12^2)*(v23^2)*(-(u21^2)*(u32^2)*(v22^2)*(v31^2)+(u22^2)*(u31^2)*(v21^2)*(v32^2))*(v33^2)+(u12^2)*(v13^2)*(v22^2)*(v32^2)*((u21^2)*(u33^2)*(v23^2)*(v31^2)-(u23^2)*(u31^2)*(v21^2)*(v33^2)))

# n1^2 nominator:
# (v11^2)*(v21^2)*(v31^2)*((u22^2)*(v12^2)*(v23^2)*(v32^2)*((u33^2)*(v13^2)-(u13^2)*(v33^2))+(v22^2)*((u32^2)*(v12^2)*(-(u23^2)*(v13^2)+(u13^2)*(v23^2))*(v33^2)+(u12^2)*(v13^2)*(v32^2)*(-(u33^2)*(v23^2)+(u23^2)*(v33^2))))
# (v11^2)*(v21^2)*(v31^2)*((u22^2)*(v12^2)*(v23^2)*(v32^2)*((u33^2)*(v13^2)-(u13^2)*(v33^2))+(v22^2)*((u32^2)*(v12^2)*(-(u23^2)*(v13^2)+(u13^2)*(v23^2))*(v33^2)+(u12^2)*(v13^2)*(v32^2)*(-(u33^2)*(v23^2)+(u23^2)*(v33^2))))

# n2^2 nominator:
# (v12^2)*(v22^2)*(v32^2)*((u21^2)*(v11^2)*(v23^2)*(v31^2)*((u33^2)*(v13^2)-(u13^2)*(v33^2))+(v21^2)*((u31^2)*(v11^2)*(-(u23^2)*(v13^2)+(u13^2)*(v23^2))*(v33^2)+(u11^2)*(v13^2)*(v31^2)*(-(u33^2)*(v23^2)+(u23^2)*(v33^2))))
# (v12^2)*(v22^2)*(v32^2)*((u21^2)*(v11^2)*(v23^2)*(v31^2)*((u33^2)*(v13^2)-(u13^2)*(v33^2))+(v21^2)*((u31^2)*(v11^2)*(-(u23^2)*(v13^2)+(u13^2)*(v23^2))*(v33^2)+(u11^2)*(v13^2)*(v31^2)*(-(u33^2)*(v23^2)+(u23^2)*(v33^2))))

# n3^2 nominator:
# (v13^2)*(v23^2)*((u21^2)*(v11^2)*(v22^2)*(v31^2)*((u32^2)*(v12^2)-(u12^2)*(v32^2))+(v21^2)*((u31^2)*(v11^2)*(-(u22^2)*(v12^2)+(u12^2)*(v22^2))*(v32^2)+(u11^2)*(v12^2)*(v31^2)*(-(u32^2)*(v22^2)+(u22^2)*(v32^2))))*(v33^2)
# (v13^2)*(v23^2)*((u21^2)*(v11^2)*(v22^2)*(v31^2)*((u32^2)*(v12^2)-(u12^2)*(v32^2))+(v21^2)*((u31^2)*(v11^2)*(-(u22^2)*(v12^2)+(u12^2)*(v22^2))*(v32^2)+(u11^2)*(v12^2)*(v31^2)*(-(u32^2)*(v22^2)+(u22^2)*(v32^2))))*(v33^2)

# create a new 'Calculator', n2^2
calculator2 = Calculator(registrationName='Calculator2', Input=threshold1)
# Properties modified on calculator2
calculator2.ResultArrayName = 'n2_Abs'
calculator2.Function = 'sqrt(((v12^2)*(v22^2)*(v32^2)*((u21^2)*(v11^2)*(v23^2)*(v31^2)*((u33^2)*(v13^2)-(u13^2)*(v33^2))+(v21^2)*((u31^2)*(v11^2)*(-(u23^2)*(v13^2)+(u13^2)*(v23^2))*(v33^2)+(u11^2)*(v13^2)*(v31^2)*(-(u33^2)*(v23^2)+(u23^2)*(v33^2)))))/((u11^2)*(v12^2)*(v13^2)*(v21^2)*(v31^2)*(-(u22^2)*(u33^2)*(v23^2)*(v32^2)+(u23^2)*(u32^2)*(v22^2)*(v33^2))+(v11^2)*((u13^2)*(v12^2)*(v23^2)*(-(u21^2)*(u32^2)*(v22^2)*(v31^2)+(u22^2)*(u31^2)*(v21^2)*(v32^2))*(v33^2)+(u12^2)*(v13^2)*(v22^2)*(v32^2)*((u21^2)*(u33^2)*(v23^2)*(v31^2)-(u23^2)*(u31^2)*(v21^2)*(v33^2)))))'
UpdatePipeline(time=0.0, proxy=calculator2)

print("n2_Abs = sqrt(n2^2) done! \n")

# create a new 'Calculator', n3^2
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
# Properties modified on calculator3
calculator3.ResultArrayName = 'n3_Abs'
calculator3.Function = 'sqrt(((v13^2)*(v23^2)*((u21^2)*(v11^2)*(v22^2)*(v31^2)*((u32^2)*(v12^2)-(u12^2)*(v32^2))+(v21^2)*((u31^2)*(v11^2)*(-(u22^2)*(v12^2)+(u12^2)*(v22^2))*(v32^2)+(u11^2)*(v12^2)*(v31^2)*(-(u32^2)*(v22^2)+(u22^2)*(v32^2))))*(v33^2))/((u11^2)*(v12^2)*(v13^2)*(v21^2)*(v31^2)*(-(u22^2)*(u33^2)*(v23^2)*(v32^2)+(u23^2)*(u32^2)*(v22^2)*(v33^2))+(v11^2)*((u13^2)*(v12^2)*(v23^2)*(-(u21^2)*(u32^2)*(v22^2)*(v31^2)+(u22^2)*(u31^2)*(v21^2)*(v32^2))*(v33^2)+(u12^2)*(v13^2)*(v22^2)*(v32^2)*((u21^2)*(u33^2)*(v23^2)*(v31^2)-(u23^2)*(u31^2)*(v21^2)*(v33^2)))))'
UpdatePipeline(time=0.0, proxy=calculator3)

print("n3_Abs = sqrt(n3^2) done! \n")

# create a new 'Calculator', n1^2
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
# Properties modified on calculator4
calculator4.ResultArrayName = 'n1_Abs'
calculator4.Function = 'sqrt(((v11^2)*(v21^2)*(v31^2)*((u22^2)*(v12^2)*(v23^2)*(v32^2)*((u33^2)*(v13^2)-(u13^2)*(v33^2))+(v22^2)*((u32^2)*(v12^2)*(-(u23^2)*(v13^2)+(u13^2)*(v23^2))*(v33^2)+(u12^2)*(v13^2)*(v32^2)*(-(u33^2)*(v23^2)+(u23^2)*(v33^2)))))/((u11^2)*(v12^2)*(v13^2)*(v21^2)*(v31^2)*(-(u22^2)*(u33^2)*(v23^2)*(v32^2)+(u23^2)*(u32^2)*(v22^2)*(v33^2))+(v11^2)*((u13^2)*(v12^2)*(v23^2)*(-(u21^2)*(u32^2)*(v22^2)*(v31^2)+(u22^2)*(u31^2)*(v21^2)*(v32^2))*(v33^2)+(u12^2)*(v13^2)*(v22^2)*(v32^2)*((u21^2)*(u33^2)*(v23^2)*(v31^2)-(u23^2)*(u31^2)*(v21^2)*(v33^2)))))'
UpdatePipeline(time=0.0, proxy=calculator4)

print("n1_Abs = sqrt(n1^2) done! \n")

#################################
##  ni^2 computing ends here   ##
#################################


# save data
SaveData('./ni-mi-li/ni_Abs.pvd',
    proxy=calculator4, ChooseArraysToWrite=1,
    PointDataArrays=['gapA', 'n1_Abs','n2_Abs','n3_Abs'],
    GhostLevel=1)

print("saving done! \n")
