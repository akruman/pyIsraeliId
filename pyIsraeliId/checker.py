__author__ = 'Ilya Chernyakov'
__alias__ = 'eliuha'

# Shalom everybody !

import re, itertools, operator
# algorithm from : http://halemo.net/info/idcard/
def validate_israeli_id_number_ak(iID):	
    iID = "{:0>9d}".format(iID)
    num_12_arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    digits = [int(d) for d in str(iID)]
    return not sum((x%10+x/10 for x in itertools.imap(operator.mul, digits, num_12_arr))) % 10

def validate_israeli_id_number_iluha(iID):
    iID = str(iID)
    if len(iID) == 8:
        iID = '0' + str(iID)
    if len(iID) != 9:
        return False

    num_12_arr = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    dig = list(int(d) for d in str(iID))

    sum_of_digits = 0
    for i in range(0, 9):
        temp = num_12_arr[i] * dig[i]
        if temp > 9:
            t = list(int(d_1) for d_1 in str(temp))
            temp = t[0] + t[1]
        sum_of_digits += temp

    if sum_of_digits % 10 != 0:
        return False

    return True

def validate_israeli_id_number_proind(iID):
    iID = str(iID)
    if len(iID) == 8:
        iID = '0' + str(iID)
    if len(iID) != 9:
        return False

    #multiply every odd index by 2
    digits = [int(x)*(i%2+1) for (i,x) in enumerate(iID)]
    #sum the  digits of the each item
    digits = [sum(map(int,str(dig))) for dig in digits]
    #sum all the digits in the list
    sum_of_digits = sum(digits)
    return not (sum_of_digits % 10)

import random
import timeit	
if __name__ == "__main__":
    ids = [random.randint(0,999999999) for r in xrange(1000)]
    import __builtin__
    __builtin__.__dict__.update(locals())
    print {'ak':timeit.timeit('[validate_israeli_id_number_ak(id) for id in ids]',number=100),
     'proind':timeit.timeit('[validate_israeli_id_number_proind(id) for id in ids]',number=100),
     'iluha':timeit.timeit('[validate_israeli_id_number_iluha(id) for id in ids]',number=100)}
    validators = {'iluha':validate_israeli_id_number_iluha, 'proind':validate_israeli_id_number_proind, 'ak':validate_israeli_id_number_ak }
    print {(k,sum([validators[k](id) for id in ids])) for k in validators}