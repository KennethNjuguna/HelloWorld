#Below code does the conversions of Weight either in Kilograms (K)g or (L)bs
#We declare the weight and the unit be it in LBS or KGS
weight= float(input("weight: "))
unit=(input("(K)g or (L)bs: "))

#Below code converts Weight declared in (K)g to (L)bs
#This code implements if to change the flow
if unit == "k":
    weight_k = weight / 2.20462
    print("weight in Pounds: " + str(weight_k))
#"elif" means else if to give the other scenario if a user inputs (L)bs to convert to (K)g
elif unit == "l":

    weight_l = weight * 2.20462
    print("weight in Kg: " + str(weight_l))
print("done")


