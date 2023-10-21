arrayset1 = []
arrayset2 = []

with open("xset.csv", "w") as xdataset, open('yset.csv', 'w') as ydataset:
    fp = open('dataset.csv', 'r')
    massiv = fp.readlines()
    stroke1 = ''
    stroke2 = ''

    for mass in massiv:
        stroke1 = mass.split(",")
        stroke1 = stroke1[0] + "\n"

        index = mass.find(",")
        stroke2 = mass[index + 2:]
        # stroke2 = stroke2.replace("\n",'')
        for i in stroke1:
            xdataset.write(i)
        
        for i in stroke2:
            ydataset.write(i)


