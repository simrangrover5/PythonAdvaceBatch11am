import sys


#print(sys.argv)

a = sys.argv
fname = a[1]
lname = a[2]

print("\n WELCOME {} {}".format(fname, lname))


out = sys.stdout

out.write("HELLO WORLD")


ina = sys.stdin
inp = ina.readline()

out.write("\n" + inp)
