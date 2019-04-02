#import roman1
import unittest
import re

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))                 

def to_roman(n):
    '''convert integer to Roman numeral'''
    if not(0<n < 4000):
        raise OutOfRangeError('number out of range (must be less than 4000)')
    if not isinstance(n, int):                                          
        raise NotIntegerError('non-integers can not be converted')
        
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:                     
            result += numeral
            n -= integer
    return result
    
    
    
roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)   
    
    
    
    
    
    
def from_roman(s):
    '''convert Roman numeral to integer'''  
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:  
            result += integer
            index += len(numeral)
    return result
    
    
    


## test


class OutOfRangeError(ValueError):  
    pass

class NotIntegerError(ValueError):
     pass
     
class InvalidRomanNumeralError(ValueError):
     pass




class ToRomanBadInput(unittest.TestCase):                                 
    def test_too_large(self):                                             
        '''to_roman should fail with large input'''
        self.assertRaises( OutOfRangeError, to_roman, 4000)
        
    def test_zero(self):
        '''to_roman should fail with 0 input'''
        self.assertRaises(OutOfRangeError, to_roman, 0)     

    def test_negative(self):
        '''to_roman should fail with negative input'''
        self.assertRaises(OutOfRangeError, to_roman, -1)
        
        
    def test_non_integer(self):
        '''to_roman should fail with non-integer input'''
        self.assertRaises(NotIntegerError,to_roman, 0.5)   
        
        
 
 
class FromRomanBadInput(unittest.TestCase):
    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with too many repeated numerals'''
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(InvalidRomanNumeralError, from_roman, s) 
            
            
    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(InvalidRomanNumeralError, from_roman, s)
 
    def test_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(InvalidRomanNumeralError, from_roman, s)
 
 
 
        
   
class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''from_roman(to_roman(n))==n for all n'''
        for integer in range(1, 4000):
            numeral = to_roman(integer)
            result =from_roman(numeral)
            self.assertEqual(integer, result) 



class KnownValues(unittest.TestCase):               
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))           

    def test_to_roman_known_values(self):           
        '''to_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = to_roman(integer)       
            self.assertEqual(numeral, result)   
            
            
            
            
    def test_from_roman_known_values(self):
        '''from_roman should give known result with known input'''
        for integer, numeral in self.known_values:
            result = from_roman(numeral)
            self.assertEqual(integer, result)        
            

   
   
   
    

if __name__ == '__main__':
    unittest.main()
    
    
   
   
#      assert sum([1, 2, 3]) == 6, "Should be 6"       


   
# import unittest
# 
# 
# class TestSum(unittest.TestCase):
# 
#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
# 
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
# 
# if __name__ == '__main__':
#     unittest.main()
