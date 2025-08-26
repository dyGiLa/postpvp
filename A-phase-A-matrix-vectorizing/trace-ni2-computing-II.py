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
threshold1.LowerThreshold = 1.8599618128954347
threshold1.UpperThreshold = 1.8975367990145346

UpdatePipeline(time=0.0, proxy=threshold1)

print("Threshold pipe line done! \n")

#######################
## uxx/vxx computing ##
#######################
# create a new 'Calculator', uv11
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
# Properties modified on calculator1
calculator1.ResultArrayName = 'uv11'
calculator1.Function = 'u11/v11'
UpdatePipeline(time=0.0, proxy=calculator1)

print("uv11 done! \n")

# create a new 'Calculator', uv12
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
# Properties modified on calculator2
calculator2.ResultArrayName = 'uv12'
calculator2.Function = 'u12/v12'
UpdatePipeline(time=0.0, proxy=calculator2)

print("uv12 done! \n")

# create a new 'Calculator', uv13
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
# Properties modified on calculator3
calculator3.ResultArrayName = 'uv13'
calculator3.Function = 'u13/v13'
UpdatePipeline(time=0.0, proxy=calculator3)

print("uv13 done! \n")

# create a new 'Calculator', uv21
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
# Properties modified on calculator4
calculator4.ResultArrayName = 'uv21'
calculator4.Function = 'u21/v21'
UpdatePipeline(time=0.0, proxy=calculator4)

print("uv21 done! \n")

# create a new 'Calculator', uv22
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
# Properties modified on calculator5
calculator5.ResultArrayName = 'uv22'
calculator5.Function = 'u22/v22'
UpdatePipeline(time=0.0, proxy=calculator5)

print("uv22 done! \n")

# create a new 'Calculator', uv23
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
# Properties modified on calculator6
calculator6.ResultArrayName = 'uv23'
calculator6.Function = 'u23/v23'
UpdatePipeline(time=0.0, proxy=calculator6)

print("uv23 done! \n")

# create a new 'Calculator', uv31
calculator7 = Calculator(registrationName='Calculator7', Input=calculator6)
# Properties modified on calculator7
calculator7.ResultArrayName = 'uv31'
calculator7.Function = 'u31/v31'
UpdatePipeline(time=0.0, proxy=calculator7)

print("uv31 done! \n")

# create a new 'Calculator', uv32
calculator8 = Calculator(registrationName='Calculator8', Input=calculator7)
# Properties modified on calculator8
calculator8.ResultArrayName = 'uv32'
calculator8.Function = 'u32/v32'
UpdatePipeline(time=0.0, proxy=calculator8)

print("uv32 done! \n")

# create a new 'Calculator', uv33
calculator9 = Calculator(registrationName='Calculator9', Input=calculator8)
# Properties modified on calculator9
calculator9.ResultArrayName = 'uv33'
calculator9.Function = 'u33/v33'
UpdatePipeline(time=0.0, proxy=calculator9)

print("uv33 done! \n")

#################################
## uxx/vxx computing ends here ##
#################################

#################################
##       ni^2 computing        ##
#################################

# All ni^2 have same dinominator:
# (((uv13^2)*(-(uv22^2)*(uv31^2) + (uv21^2)*(uv32^2))) + ((uv12^2)* ((uv23^2)*(uv31^2) - (uv21^2)*(uv33^2))) + ((uv11^2)*(-(uv23^2)*(uv32^2) + (uv22^2)*(uv33^2))))

# n1^2 nominator:
# ((-(uv23^2)*(uv32^2)) + ((uv13^2)*(-(uv22^2) + (uv32^2))) + ((uv22^2)*(uv33^2)) + ((uv12^2)*((uv23^2) - (uv33^2))))

# n2^2 nominator:
# (((uv23^2)*(uv31^2)) + ((uv13^2)*((uv21^2) - (uv31^2))) - ((uv21^2)*(uv33^2)) + ((uv11^2)*(-(uv23^2) + (uv33^2))))

# n3^2 nominator:
# ((-(uv22^2)*(uv31^2)) + ((uv12^2)*(-(uv21^2) + (uv31^2))) + ((uv21^2)*(uv32^2)) + ((uv11^2)*((uv22^2) - (uv32^2))))


# create a new 'Calculator', n2^2
calculator10 = Calculator(registrationName='Calculator10', Input=calculator9)
# Properties modified on calculator10
calculator10.ResultArrayName = 'n22'
calculator10.Function = '(((uv23^2)*(uv31^2)) + ((uv13^2)*((uv21^2) - (uv31^2))) - ((uv21^2)*(uv33^2)) + ((uv11^2)*(-(uv23^2) + (uv33^2))))/(((uv13^2)*(-(uv22^2)*(uv31^2) + (uv21^2)*(uv32^2))) + ((uv12^2)* ((uv23^2)*(uv31^2) - (uv21^2)*(uv33^2))) + ((uv11^2)*(-(uv23^2)*(uv32^2) + (uv22^2)*(uv33^2))))'
UpdatePipeline(time=0.0, proxy=calculator10)

print("n2^2 done! \n")

# create a new 'Calculator', n3^2
calculator11 = Calculator(registrationName='Calculator11', Input=calculator10)
# Properties modified on calculator11
calculator11.ResultArrayName = 'n32'
calculator11.Function = '((-(uv22^2)*(uv31^2)) + ((uv12^2)*(-(uv21^2) + (uv31^2))) + ((uv21^2)*(uv32^2)) + ((uv11^2)*((uv22^2) - (uv32^2))))/(((uv13^2)*(-(uv22^2)*(uv31^2) + (uv21^2)*(uv32^2))) + ((uv12^2)* ((uv23^2)*(uv31^2) - (uv21^2)*(uv33^2))) + ((uv11^2)*(-(uv23^2)*(uv32^2) + (uv22^2)*(uv33^2))))'
UpdatePipeline(time=0.0, proxy=calculator11)

print("n3^2 done! \n")

# create a new 'Calculator', n1^2
calculator12 = Calculator(registrationName='Calculator12', Input=calculator11)
# Properties modified on calculator12
calculator12.ResultArrayName = 'n12'
calculator12.Function = '((-(uv23^2)*(uv32^2)) + ((uv13^2)*(-(uv22^2) + (uv32^2))) + ((uv22^2)*(uv33^2)) + ((uv12^2)*((uv23^2) - (uv33^2))))/(((uv13^2)*(-(uv22^2)*(uv31^2) + (uv21^2)*(uv32^2))) + ((uv12^2)* ((uv23^2)*(uv31^2) - (uv21^2)*(uv33^2))) + ((uv11^2)*(-(uv23^2)*(uv32^2) + (uv22^2)*(uv33^2))))'
UpdatePipeline(time=0.0, proxy=calculator12)

print("n1^2 done! \n")

#################################
##  ni^2 computing ends here   ##
#################################

###################################
## ni_Abs = sqrt(ni^2) computing ##
###################################

# create a new 'Calculator', n1_Abs = sqrt(n1^2)
calculator13 = Calculator(registrationName='Calculator13', Input=calculator12)
# Properties modified on calculator13
calculator13.ResultArrayName = 'n1_Abs'
calculator13.Function = 'sqrt(n12)'
UpdatePipeline(time=0.0, proxy=calculator13)

print("n1_Abs done! \n")

# create a new 'Calculator', n2_Abs = sqrt(n2^2)
calculator14 = Calculator(registrationName='Calculator14', Input=calculator13)
# Properties modified on calculator14
calculator14.ResultArrayName = 'n2_Abs'
calculator14.Function = 'sqrt(n22)'
UpdatePipeline(time=0.0, proxy=calculator14)

print("n2_Abs done! \n")

# create a new 'Calculator', n3_Abs = sqrt(n3^2)
calculator15 = Calculator(registrationName='Calculator15', Input=calculator14)
# Properties modified on calculator15
calculator15.ResultArrayName = 'n3_Abs'
calculator15.Function = 'sqrt(n32)'
UpdatePipeline(time=0.0, proxy=calculator15)

print("n3_Abs done! \n")


#################################
## ni_Abs computing ends here  ##
#################################


# save data
SaveData('./ni-mi-li/ni_Abs.pvd',
    proxy=calculator12, ChooseArraysToWrite=1,
    PointDataArrays=['gapA', 'n1_Abs','n2_Abs','n3_Abs'],
    GhostLevel=1)

print("saving done! \n")
