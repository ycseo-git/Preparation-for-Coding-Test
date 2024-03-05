from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    
    answer_numer = numer1 * denom2 + numer2 * denom1
    answer_denom = denom1 * denom2
    
    answer = Fraction(answer_numer, answer_denom)
    
    return [answer.numerator, answer.denominator]