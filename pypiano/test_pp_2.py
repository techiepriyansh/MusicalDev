import pypiano as pp
import frequencies as fqs
import numpy as np
import sys



arr = np.array(sys.argv[1:])
arr = arr.astype(np.int)

music = pp.createMajorScale("D4",arr,0.5/1.5)

wave_obj = pp.musify(music)
play_obj = wave_obj.play()
play_obj.wait_done()