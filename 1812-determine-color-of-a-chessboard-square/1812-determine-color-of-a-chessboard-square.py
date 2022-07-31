class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c = list(coordinates)
        if (c[0]=="a" or c[0]=="c" or c[0]=="e" or c[0]=="g") and (c[1]=="1" or c[1]=="3" or c[1]=="5" or c[1]=="7"):
            return False
        elif (c[0]=="b" or c[0]=="d" or c[0]=="f" or c[0]=="h") and (c[1]=="2" or c[1]=="4" or c[1]=="6" or c[1]=="8"):
            return False
        else:
            return True
        