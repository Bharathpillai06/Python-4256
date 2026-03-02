""" 1) Write a function called sym diff(s, t) that takes two set s and t as argu-
 ments and returns the symmetric difference of s and t. s and t should not be
modified.
Your function should not call the symmetric difference() function, but can
call other functions such as intersection(), union() and difference(). The
body of your function should be one line long"""

def sym_diff(s, t):
    return s.union(t).difference(s.intersection(t))
