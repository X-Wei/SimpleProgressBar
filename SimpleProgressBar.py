'''
A simple progressbar.
@author: xwei
'''
import sys

class SimpleProgressBar():
    def __init__(self, width=50):
        self.last_x = -1
        self.width = width
 
    def update(self, x):
        assert 0 <= x <= 100 # `x`: progress in percent ( between 0 and 100)
        if self.last_x == int(x): return
        self.last_x = int(x)
        pointer = int(self.width * (x / 100.0))
        sys.stdout.write( '\r%d%% [%s]' % (int(x), '#' * pointer + '.' * (self.width - pointer)))
        sys.stdout.flush()
        if x == 100: print ''

if __name__ == '__main__':
    # An example of usage...
    import time
    pb = SimpleProgressBar()
    for i in range(101):
        pb.update(i)
        time.sleep(0.1)
    
    
    
