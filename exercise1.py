def cagr_berechnung(AK,EK,t):
    z=((EK/AK)**(1/t))-1
    return z

print(cagr_berechnung(100, 700, 30))

print(120*(1+cagr_berechnung(100, 700, 30))**30)


def teilbar(x,y):
    if y==0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    elif x==y:
        print("x und y sind gleich")
    elif x % y ==0:
        print("x ist durch y teilbar")
    else:
        print("x ist nicht durch y teilbar")  
        
print(teilbar(x=9,y=3))