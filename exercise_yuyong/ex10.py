

a = "I am 6'2\" tall."  # escape double-quote inside string
b = 'I am 6\'2" tall.'  # escape single-quote inside string
# print a, "\n", b

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# print tabby_cat
# print persian_cat
# print backslash_cat
# print fat_cat
#
# myu = u'\U0001F47F'
# print "myu is %s" % u'\U0001F47E'
cnt = 5
while cnt > 0:
    cnt-=1
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
    print
# for i in ["/","-","|","\\","|"]:
#     print i