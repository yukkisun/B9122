## b9122 Assignment 1 ##
# author: Yuqi(Yukki) Sun #
# uni: ys3248 #
# datetime: 20190925 #
# email: YSun21@gsb.columbia.edu #

## Question 1 ##
# define the EMI function
def EMI(rate, N, PV, FV):
    if isinstance(rate, float) & isinstance(N, int) & isinstance(PV, int) & isinstance(FV, int):
        emi = (PV + FV/(1 + rate)**N)*rate*(1 + rate)**N/((1 + rate)**N - 1)
        print('EMI = ', emi)
    else:
        print('Please check your input. Reenter your input so that rate is float, N PV FV are all integer.')

# test EMI function with given values
EMI(0.05, 30, 10000, 2000)
EMI(0.1, 300, 1000, 200)
# also can use other inputs to test the EMI function: EMI(0.5,12.3,1000,20)