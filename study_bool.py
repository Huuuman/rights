'''
study on True/False in Python
last edit: 2017. 5. 9 by JuneTech
'''
test_set = [False, '0', '1', '', None, '123', 'gong4py']
for item in test_set:
    if not item:
        print ('boolean of', item, 'is', False)
    else:
        print ('boolean of', item, 'is', True)

header = []
unitname = 'dummy'
number_of_max = 18
for i in range(0, number_of_max):
    header.append(unitname + str(i+1))

print(header)

print(unitname+str(number_of_max))

print(header[-1] != unitname+str(number_of_max))
