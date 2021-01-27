'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        if answer == 'yes':
            answer = 'no'
        else:
            answer = 'yes'




