from sympy import *
import seqToMidi as stm
import sys

number_of_terms = int(sys.argv[1])

prime_seq = [prime(i) for i in range(1,number_of_terms+1)]
stm.seqToMidi(prime_seq,"C4#","music_dist/prime_music_" + str(number_of_terms) + ".mid")