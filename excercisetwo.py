weight= int(input("weight: "))
unit=(input("(K)g or (L)bs: "))


if unit == "l":
    weight_l = weight * 2.20462
    print("weight in Kg: " + str(weight_l))
elif unit == "k":
    weight_k=weight / 2.20462
    print("weight in Pounds: " + str(weight_k))
print("done")


