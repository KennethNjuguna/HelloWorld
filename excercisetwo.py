#Below code does the conversions of Weight either in Kilograms (K)g or (L)bs
#We declare the weight and the unit be it in LBS or KGS
weight= float(input("weight: "))
unit=(input("(K)g or (L)bs: "))


if unit == "k":
    weight_k = weight / 2.20462
    print("weight in Pounds: " + str(weight_k))

elif unit == "l":

    weight_l = weight * 2.20462
    print("weight in Kg: " + str(weight_l))
print("done")


