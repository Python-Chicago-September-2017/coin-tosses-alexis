import random

def toss_count(num):
    heads = 0
    tails = 0
    options = ('head','tail')
    for i in range(num):
        toss = options[random.randint(0,1)]
        if toss == 'head':
            heads += 1
        else:
            tails += 1
        print "Attempt #{}: Throwing coin... It's a {}!... Got {} head(s) and {} tail(s) so far".format(i+1,toss,heads,tails)

toss_count(5000)