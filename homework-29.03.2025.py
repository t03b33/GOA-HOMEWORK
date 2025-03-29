# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python

def check(seq, elem):
    if elem in seq:
        return True
    return False

# https://www.codewars.com/kata/5b4e779c578c6a898e0005c5

def draw_stairs(n):
    res = ''
    for i in range(n):
        if i == n-1:
            res += ' ' * i + 'I'
        else:
            res += ' ' * i + 'I\n'
    return res

# https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7

def make_upper_case(s):
    s = s.upper()
    return s

# https://www.codewars.com/kata/59c1302ecb7fb48757000013

def type_validation(variable, _type):
    checktype = type(variable).__name__
    if checktype == _type:
        return True
    return False

# https://www.codewars.com/kata/59342039eb450e39970000a6/train/python

def odd_count(n):
    count = n // 2
    return count

# https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130/train/python

def get_min_max(seq): 
    mini = min(seq)
    maxi = max(seq)
    return mini, maxi

# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python

def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    if sorted(test) == sorted(original):
        return True
    return False