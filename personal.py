def ageRange(age):
  if age > 0 and age <= 20:
    return '0-20'
  elif age > 21 and age <= 25:
    return '21-25'
  elif age >= 26 and age <= 30:
    return '26-30'
  elif age >= 31 and age <= 35:
    return '31-35'
  elif age >= 36 and age <= 40:
    return '36-40'
  elif age >= 41 and age <= 45:
    return '41-45'
  elif age >= 45 and age <= 50:
    return '45-50'
  elif age >= 51 and age <= 55:
    return '51-55'
  elif age >= 56 and age <= 60:
    return '56-60'
  elif age >= 61 and age <= 65:
    return '61-65'
  elif age >= 66 and age <= 70:
    return '66-70'
  return ''

def bmiRange(bmi):
  if bmi < 18.5:
    return 'under weight'
  elif bmi >= 18.5 and bmi < 23:
    return 'normal weight'
  elif bmi >= 23 and bmi < 25:
    return 'over weight'
  elif bmi >= 25:
    return 'obse weight'
  return ''

def getColumnColor(items):
  color = []
  for x in items:
    if(x == 'F'):
      color.append('pink')
    elif(x == 'M'):
      color.append('lightblue')
  return color

def ageDMScore(age):
  if age >= 45 and age < 49:
    return 1
  elif age >= 50:
    return 2
  return 0

def genderDMScore(sex):
  if sex == "M":
    return 2
  return 0

def bmiDMScore(bmi):
  if bmi > 23 and bmi < 27.5:
    return 3
  elif bmi >= 27.5:
    return 5
  return 0

def sys_diasDMScore(sys, dias):
  if sys >= 140 or dias >= 90:
    return 2
  return 0

def smokeScore(smoke):
  if smoke == "Y":
    return 1
  return 0

def bmiHypertensionScore(sex, bmi):
  if sex == "F" and bmi > 23:
    return 1
  elif sex == "M" and bmi > 25:
    return 1
  return 0

def ChoLDLHDLTriHypertensionScore(sex, Cholesterol, LDL, HDL, Triglycerides):
  if Cholesterol >= 200:
    return 1
  elif LDL >= 100:
    return 1
  elif sex == "M" and HDL >= 40:
    return 1 
  elif sex == "F" and HDL >= 50:
    return 1 
  elif Triglycerides >= 150:
    return 1
  return 0

def sys_diasHypertensionScore(sys, dias):
  if sys >= 130 or dias >= 80:
    return 1
  return 0

def bmiStokeScore(sex, bmi):
  if sex == "F" and bmi > 23:
    return 1
  elif sex == "M" and bmi > 25:
    return 1
  return 0

def bmiStokeScore(sex, bmi):
  if sex == "F" and bmi > 23:
    return 1
  elif sex == "M" and bmi > 25:
    return 1
  return 0

def sys_diasStokeScore(age, sys, dias):
  if age < 40 (sys >= 130 or dias >= 80):
    return 1
  elif age >= 40 (sys >= 140 or dias >= 90):
    return 1
  return 0


