import anagram

assert True == anagram.are_anagrams('abba', 'baba'), 'KO'
print 'OK'

assert True == anagram.are_anagrams('A b b a', 'baba'), 'KO'
print 'OK'

assert False == anagram.are_anagrams('Abba', 'buba'), 'KO'
print 'OK'