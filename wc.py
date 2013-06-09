import sys
import re

"""
f = sys.stdin
s = f.read()
f.close()
add start
"""
filename = sys.argv[1]

try:
    f = open(filename,'rU')
except IOError:
    print >> sys.stderr, "Error:open file failed!"
    sys.exit()


"""
words = s.split()
for w in words:
    if d.has_key(w):
        d[w] += 1
    else:
        d[w] = 1
line = f.readline()
"""
d = {}
r = re.compile(r"[,|.|'|\"|!|?]")
line = f.readline()
while line:
    line = r.sub("", line)
    for w in line.split():
        w = w.lower()
        if d.has_key(w):
            d[w] += 1
        else:
            d[w] = 1
    line = f.readline()

sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
print "all: %d" % len(d)

i = 0
for k in sored_keys:
    if i == 20:
        break
    print k, ": ", d[k]
    i += 1


