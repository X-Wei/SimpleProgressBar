'''
A simple progressbar.
@author: xwei
'''
import sys, time


class SimpleProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width
 
    def update(self, x):
        '`x`: progress in percent (0~100)'
        assert 0 <= x <= 100
        if int(self.width * (x / 100.0)) == int(x): # not necessary to update display
            return
        self.pointer = int(self.width * (x / 100.0))
        pg = '%d%% [%s]' % (int(x), '#' * self.pointer + '-' * (self.width - self.pointer))
        sys.stdout.write(pg)
        sys.stdout.flush()
        sys.stdout.write('\r')
        if x == 100:  # if finished, print a new line
            sys.stdout.write('\n')


if __name__ == '__main__':
    # An example of usage...
    pb = SimpleProgressBar()
    for i in range(301):
        pb.update(i*100.0/300)
        time.sleep(0.1)
    
    
    
