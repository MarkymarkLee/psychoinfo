from psychopy import core, visual, event
import socket
import pickle

code = 'utf-8'
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('hpc.psy.ntu.edu.tw', 1234))
c.sendall('b10902032'.encode(code))  # Change your ID here!
print(c.recv(9).decode(code))  # Should show your ID!

w = visual.Window(size=[800, 400], units='norm')
for t in range(8):
    sz = int(c.recv(2).decode(code))  # size
    word = pickle.loads(c.recv(sz))
    # print(word)

    # Make your changes here (4 points for graphical displaying):
    visual.TextStim(w, text=word['text'],
                    color=word['color']).draw()
    w.flip()
    core.wait(0.05, 0)
    w.flip()
    # visual.TextStim(
    #     w, text="What is the color of the text?\n Press r,g,b,y\n").draw()
    # w.flip()
    r = event.waitKeys(keyList=['r', 'g', 'b', 'y'], timeStamped=core.Clock())
    c.sendall(pickle.dumps(r[0]))
    core.wait(1)

print(c.recv(5).decode(code))  # 4 points for passing
