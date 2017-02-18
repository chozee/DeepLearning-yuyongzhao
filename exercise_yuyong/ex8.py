# -*- coding:utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

'''
    汉字测试
'''
print formatter % ('汉字1', "汉字2", formatter, formatter)

formatter2 = "%s %s %r %r"
print formatter2 % ('汉字1', "汉字2", formatter, formatter)

formatter3 = "%s %s %s %s"
print "\n\n\%s \%s \%s \%s test ============="
print formatter3 % (1, 2, 3, 4)
print formatter3 % ("one", "two", "three", "four")
print formatter3 % (True, False, False, True)
print formatter3 % (formatter, formatter, formatter, formatter)
print formatter3 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
print formatter3 % ('汉字1', "汉字2", formatter, formatter)
