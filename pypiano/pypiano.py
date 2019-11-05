import frequencies as fqs
import numpy as np
import simpleaudio as sa

sample_rate = 44100

# keep amplitude always "one" 
# it's okay if when superposing amplitude gets more than one
# finally normalize evrything by dividing by max amplitude
# createNote will always return with amplitude one
# phi : initial phase
def createNote(freq_or_note , time_duration, phi = 0, should_return_end_phase = False):
	freq = freq_or_note
	if type(freq_or_note) == type("A4"):
		freq = fqs.getNoteFreq(freq_or_note)

	time_steps = np.linspace(0,time_duration,time_duration*sample_rate,False)
	omega = np.pi * 2 * freq
	note_array = [np.sin(omega*t + phi) for t in time_steps]

	if not should_return_end_phase:
		return note_array
	else:
		return note_array, np.arcsin(note_array[-1])

# root_note can be either frequency like 440 or note like "A4"
# sequence_to_play is something like [1,1,8,5,6] ..
#.. only integers from 1 to 8
# here time_duration will be an array with time duration..
#.. corresponding to each scale degree.
# if you want same time duration, pass a single value
def createMajorScale(root_note, sequence_to_play, time_duration):
	key = fqs.getMajorKey(root_note)
	scale = np.array([])
	phi = 0
	if type(time_duration) == type([1,2,3,4]):
		for i in range(0,len(sequence_to_play)) :
			note_piece, phi = createNote(key[sequence_to_play[i]],time_duration[i], phi, True)
			scale = np.hstack((scale, note_piece))
	else :
		for degree in sequence_to_play :
			note_piece, phi = createNote(key[degree], time_duration, phi, True)
			scale = np.hstack((scale, note_piece))

	return scale



# always creating "mono" audio
# converts any (1 D) raw array into a WaveObject
def musify(arr):
	arr *= 32767/max(abs(arr))
	arr = arr.astype(np.int16)

	wave_obj = sa.WaveObject(arr, 1, 2, sample_rate)

	return wave_obj









