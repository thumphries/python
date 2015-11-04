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

coolargs(lame = "aww")  # "I only accept cool arguments."
coolargs(cool = "aww")  # "I only accept cool arguments."
coolargs(cool = 'cool') # "Alright!"

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


# fun with zip
# zip works on iterables or argument sequences.
# This one is regular usage on a list
zipped = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
print zipped # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Can zip up tuples easily
print zip((1, 2, 3), (4, 5, 6))

# This one is zipping the unpacked tuples together
tups = zip(*zipped)
print tups   # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# This one is real dumb - 'zipped' is a packed list of tups
# and the second list doesn't exist
# ... so we get this:
print (zip(zipped)) # [((1, 4, 7),), ((2, 5, 8),), ((3, 6, 9),)]

# ... even though zip usually truncates to the shortest argument:
print (zip(zipped, [])) # []
