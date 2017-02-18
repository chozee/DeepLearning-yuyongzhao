from sys import argv

script, fileName = argv
txt = open(fileName)

print 'Here is your file %r : ' % fileName
print 'Here is your file comtent %s : ' % txt.read()
print 'Here is your file comtent %r : ' % txt.read() # when read excute by last line , it's nothing remained
