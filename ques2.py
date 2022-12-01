

def triangle(a,b,c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        print("Invalid triangle")
    else:
        print("valid triangle")
triangle(7,10,5)

def Rectangle(a, b, c, d):
 
    # check all sides of rectangle combinations
    if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
        print("valid rectangle")
    else:
        print("invalid rectangle")
Rectangle(1,1,2,3)