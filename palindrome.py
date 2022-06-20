import re
forward=input("insert string")
forward = re.sub(r"\s+","",forward)
backward=forward[::-1]
if((forward.lower())==(backward.lower())):
    print("yes")
else:
    print("No")