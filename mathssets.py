dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

# set built-in function union
res=dataScientist.union(dataEngineer)# Equivalent Result 
resb = dataScientist | dataEngineer

print(res)

print(resb)

# Intersection operation
dataScientist.intersection(dataEngineer)# Equivalent Result
dataScientist & dataEngineer

# Difference Operation
dataScientist.difference(dataEngineer)# Equivalent Result
dataScientist - dataEngineer

# Symmetric Difference Operation
dataScientist.symmetric_difference(dataEngineer)# Equivalent Result
dataScientist ^ dataEngineer

possibleSkills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}

mySkills.issubset(possibleSkills)