#
APPLICATIONS of STACK
#	1. Expressions COnversions (Prefix, Infix, Postfix)
#	= +AB+C = A+B+C = AB+C+
#	= A+B-C*D+E = AB+CD*-E+
#	= x/y-(a+b)-(c*d)+z+(e-f) = xy/ab+-cd*-z+ef-+ 


# INFIX TO POSTFIX using STACK
# RULES:-
# 1. Check priorities of operators
# 2. No two operators of same priority should stay together in stack
# 3. If incoming priority op is of low or equal prior than one in stack POP the high prior op
# 4. If any operator is in b/w open and closed brace in the stack pop it

# A+B+C
# INCOMING		STACK		POSTFIX
# A       		     		A
# +       		+    		A
# B       		+    		AB
# +       		+ +  		AB
####      		+    		AB+
# C       		+    		AB+C
####      		     		AB+C+

# A+B*C+D
# INCOMING		STACK		POSTFIX
# A       		     		A
# +       		+    		A
# B       		+    		AB
# *       		+*   		AB
# C       		+*   		ABC
# +       		+    		ABC*+
# D       		+    		ABC*+D+