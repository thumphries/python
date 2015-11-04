#!/usr/bin/env python

# kwargs.py
# Demonstrating * and **

# http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
def coolargs(**args):
    for key, val in args.iteritems():
        if key == 'cool' == val:
            print "Alright!"
            return
    print "I only accept cool arguments."

coolargs(lame = "aww")
coolargs(cool = "aww")
coolargs(cool = 'cool')

cooldict = { 'lame': 'aww', 'cool': 'cool' }
# coolargs(cooldict) # not allowed - coolargs takes 0 arguments (1 given)
coolargs(**cooldict) # allowed - ** unpacks the dict into the above format

def varargs(*args):
     count = 0
     for x in args:
          count = count + 1
     print ("I got %d args!" % (count))

varargs()
varargs(1, 2, 3)
varargs(1, 2, 3, 4, 5, 6, 7, 8)


coollist = [1, 2, 3]
varargs(coollist)  # I got 1 args!
varargs(*coollist) # I got 3 args!
