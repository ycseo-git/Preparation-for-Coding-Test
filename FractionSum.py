from fractions import Fraction
import math



##### My first solution with using module 'fraction' #####
def solution_1(numer1, denom1, numer2, denom2):
    
    answer_numer = numer1 * denom2 + numer2 * denom1
    answer_denom = denom1 * denom2
    
    answer = Fraction(answer_numer, answer_denom)
    
    return [answer.numerator, answer.denominator]



##### The optimized first solution with using module 'fraction' #####
def solution_1_2(numer1, denom1, numer2, denom2):

    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)

    return [answer.numerator, answer.denominator]



##### The second solution with using module 'math' and its gcd() #####
def solution_2(numer1, denom1, numer2, denom2):
    
    answer_numer = numer1 * denom2 + numer2 * denom1
    answer_denom = denom1 * denom2
    gcd = math.gcd(answer_numer, answer_denom)
    
    return [answer_numer // gcd, answer_denom // gcd]



##### For the test #####
print(solution_1(1,2,3,4))
print(solution_1_2(1,2,3,4))
print(solution_2(1,2,3,4))
