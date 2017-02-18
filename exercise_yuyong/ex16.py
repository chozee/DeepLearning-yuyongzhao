from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')
print "Before write content \n ", target.read()
target.close()

target = open(filename, 'w')
# target.seek(0)
# print "Before write content is : \n", target.read()

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# target.seek(0)
# print "After write content is : \n %s" % target.read()
target.close()

target = open(filename, 'r')
print target.read()
target.close()
