with open('matrix_rotation_notes_20131214.tex', 'r') as f2:
    while f2:
        line = f2.readline()
        print('length: {}; first five: {}'.format(len(line), line[0:5]))
        time.sleep(.5)
