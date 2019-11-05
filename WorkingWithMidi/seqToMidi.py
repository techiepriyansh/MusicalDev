import frequencies as fqs 
from midiutil import MIDIFile

def seqToMidi(seq,root_note,output_file_name):
	key_degrees = []
	for term in seq:
		key_degree = term % 8

		if key_degree == 0:
			key_degree = 8

		key_degrees.append(key_degree)

	major_key = fqs.getMajorKey(root_note)
	degrees = [major_key[a] for a in key_degrees]

	track    = 0
	channel  = 0
	time     = 0    # In beats
	duration = 1    # In beats
	tempo    = 100   # In BPM
	volume   = 100  # 0-127, as per the MIDI standard

	MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
	                      # automatically)
	MyMIDI.addTempo(track, time, tempo)

	for i, pitch in enumerate(degrees):
	    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

	with open(output_file_name, "wb") as output_file:
	    MyMIDI.writeFile(output_file)
