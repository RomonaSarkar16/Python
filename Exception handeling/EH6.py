#Error: assertion error
# When an assert statement is failed, an Assertion Error is raised.
# Let's take an example to understand the assertion error. Let's say you have two variables a and b,
# which you need to compare. To check whether a and b are equal or not, you apply an assert keyword before that,
# which will raise an Assertion exception when the expression will return false.
# assert() ----> comparing two values
X = input("x=")
Y = input("y=")
try:
    assert X==Y
except:
    print("they are not similar")
else:
    print("they are similar")