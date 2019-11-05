
coreFQS = {
	'C' : 1,
	'D'	: 3,
	'E'	: 5,
	'F' : 6,
	'G'	: 8,
	'A'	: 10,
	'B' : 12
}

#-----------------------------------------------------------------#

#C0 : 1

#Note String Format: eg: "A4#" or "B2b" or "C1"
def getNoteIndex(note_string):
	core_freq = note_string[0]
	octave_number = int(note_string[1])
	black_key_offset = 0

	if len(note_string) == 3:
		if note_string[2] == '#':
			black_key_offset = 1
		elif note_string[2] == 'b':
			black_key_offset = -1

	index = 12 * octave_number + coreFQS[core_freq] + black_key_offset

	return index

#-----------------------------------------------------------------#	

tuning_freq_A4 = 440

def getNoteFreq(note_string):
	relative_index = getNoteIndex(note_string) - getNoteIndex('A4')
	note_freq = tuning_freq_A4 * (2**(relative_index/12))
	return note_freq


# A key is a set of notes which sound good together
# The words scale and key are sometimes used interchangeably
# Technically, a scale is a sequence of notes played in ..
# .. that order
# Root note can be note like "A4" or frequency like 440
# Returns all the scale frequencies
# Index 0 is 0 so as to match the standard indexing format in ..
# .. music theory. Here it will mean silence.
def getMajorKey(root_note):
	rnf = root_note
	if type(root_note) == type("A4"):
		rnf = getNoteFreq(root_note)

	tone = 2**(1/6)

	return [0,
			rnf,
			rnf * tone,
			rnf * (tone**2),
			rnf * (tone**2.5),
			rnf * (tone**3.5),
			rnf * (tone**4.5),
			rnf * (tone**5.5),
			rnf * (tone**6)]



























