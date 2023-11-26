# CodeWars: https://www.codewars.com/kata/6512b3775bf8500baea77663/train/python

import unittest

class TestLetters(unittest.TestCase):
    dictionary =\
                    {
                        'a-z': 'abcdefghijklmnopqrstuvwxyz',
                        'h-o': 'hijklmno',
                        'J-J': 'J',
                        'g-i': 'ghi',
                        'F-O': 'FGHIJKLMNO',
                        'H-I': 'HI',
                        'e-k': 'efghijk'
                    }
    
    def test_gimme_the_letters(self):
        for key, value in self.dictionary.items():
            self.assertEqual(LettersFromAtoZ.gimme_the_letters(key), value)
            # optional: print(f'\tTest case passed: \'gimme_the_letters\' with input \'{key}\' and asserted output \'{value}\'.')
            
        with self.assertRaises(TypeError):
            LettersFromAtoZ.gimme_the_letters('')

    def test_gimme_the_letters_short(self):
        for key, value in self.dictionary.items():
            self.assertEqual(LettersFromAtoZ.gimme_the_letters_short(key), value)
            # optional: print(f'\tTest case passed: \'gimme_the_letters_short\' with input \'{key}\' and asserted output \'{value}\'.')
            
        with self.assertRaises(IndexError):
            LettersFromAtoZ.gimme_the_letters_short('')



class LettersFromAtoZ():
    # First attempt, not refactored
    def gimme_the_letters(input):
        arr = input.split('-')
        starter = ord(arr[0])
        end = ord(arr[1])
        output = ''
        if starter == end:
            return chr(starter)
        else:
            for ascii in range(starter, end+1):
                output += chr(ascii)
            return output

    # Second attempt, refactored
    def gimme_the_letters_short(input):
        return ''.join([chr(x) for x in range(ord(input[0]), ord(input[-1])+1)])



def main():
    unittest.main()



if __name__ == "__main__":
    main()