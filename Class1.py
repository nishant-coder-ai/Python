class Mobile:
    pass


m1 = Mobile
m2 = Mobile

print(m1)
print(m2)
# For now we are looking at the instance variables
m1.ram = '4Gb'
m1.rom = '64Gb'
m1.name = 'Xiaomi'
m1.mail = 'Xiaomi@company.com'

m2.ram = '6Gb'
m2.rom = '127Gb'
m2.name = 'Xiaomi.Poko'
m2.mail = 'Xiaomi.Poko@company.com'

print(m1.name)
print(m2.name)
