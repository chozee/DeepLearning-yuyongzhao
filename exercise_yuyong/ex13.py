from sys import argv

# execute: python ex13.py 2 3 4

secondParm = raw_input("Input 2th parameter> ")
thirdParam = raw_input("Input 3rd parameter > ")
forthParam = raw_input("Input 4th parameter > ")
argv.append(secondParm)
argv.append(thirdParam)
argv.append(forthParam)
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third