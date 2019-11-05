import pypiano as pp
import numpy as np

T = 0.5
a = pp.createNote(pp.fqs.getNoteFreq('A4'), 4*T)
b = pp.createNote(pp.fqs.getNoteFreq('C5b'), 8*T)

c = np.hstack((a, b)) 
print(len(c)/pp.sample_rate)

music = pp.musify(c)
play_obj = music.play()
play_obj.wait_done()