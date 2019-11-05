import seqToMidi as stm
import sys

number_of_terms = int(sys.argv[1])


#n > = 2
def get_fib_array(n,fib_array = [1,1]):
	fib_array_new = fib_array.copy()
	if len(fib_array_new) == n:
		return fib_array_new
	else:
		next_term = fib_array_new[-1] + fib_array_new[-2]
		fib_array_new.append(next_term)
		return get_fib_array(n,fib_array_new)

fib_seq = get_fib_array(number_of_terms)

stm.seqToMidi(fib_seq,"A4","music_dist/fib_music_" + str(number_of_terms) + ".mid")