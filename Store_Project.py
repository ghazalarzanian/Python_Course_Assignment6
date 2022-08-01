import qrcode
def QR_Code():
    Temp=input("Enter code:")
    img = qrcode.make(Temp)
    img.save('Qr.png')
def Update():
    myfile=open('Database.txt','w')
    for i in range(len(PRODUCTS)):
        myfile.write(PRODUCTS[i]['id'])
        myfile.write(',')
        myfile.write(PRODUCTS[i]['name'])
        myfile.write(',')
        myfile.write(PRODUCTS[i]['price'])
        myfile.write(',')
        myfile.write(PRODUCTS[i]['count'])
        if i!=(len(PRODUCTS)-1):
            myfile.write('\n')
def Menu():
    print('1-Add Product')
    print('2-Edit Product ')
    print('3-Delete Product')
    print('4-Search')
    print('5-Show List')
    print('6-Buy')
    print('7-QrCode')
    print('8-Exit')
def Show_List():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
def Load():
    print('Loading...')
    myfile= open('Database.txt','r')
    data = myfile.read()
    Products_List=data.split('\n')
    for i in range(len(Products_List)):
        product_info=Products_List[i].split(',')
        MyDict={}
        MyDict['id']=product_info[0]
        MyDict['name']=product_info[1]
        MyDict['price']=product_info[2]
        MyDict['count']=product_info[3]
        PRODUCTS.append(MyDict)
    print('Welcome')
def Add_Product():
    New={}
    New['id']=input("Enter id:")
    New['name']=input("Enter name:")
    New['price']=input("Enter Price:")
    New['count']=input("Enter Count:")
    for i in range(len(PRODUCTS)):
        if New['id']==PRODUCTS[i]['id']:
            print("id exist,Try Agin")
            New['id']=input("Enter id:")
            i=0
        if New['name']==PRODUCTS[i]['name']:
            print("name exist,Try again")
            New['name']=input("Enter name:")
            i=0
    PRODUCTS.append(New)
    myfile=open('Database.txt','a')
    myfile.write('\n')
    myfile.write(New['id'])
    myfile.write(',')
    myfile.write(New['name'])
    myfile.write(',')
    myfile.write(New['price'])
    myfile.write(',')
    myfile.write(New['count'])
def Edit_Prodcut():
    Code=(input("Enter code of the product you want to edit: "))
    j=int()
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==Code:
            j=i
    PRODUCTS[j]['id']=input("Enter new Code:")
    PRODUCTS[j]['name']=input("Enter new Name:")
    PRODUCTS[j]['price']=input("Enter new Price:")
    PRODUCTS[j]['count']=input("Enter new count:")
    Update()
def Delete_Prodcut():
    Code=(input("Enter code of the product you want to edit: "))
    j=int()
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==Code:
            j=i
    PRODUCTS.pop(j)
    Update()
def Buy_Product():
    box=[]
    Total=int()
    A=1
    j=int()
    while A!=0 :
        Code=(input("Enter code of the product you want to Buy: "))
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['id']==Code:
                j=i
        if PRODUCTS[j]['count']==0:
            print("This Product is finished")
        else:
            Amount=int(input("How Many Do you want: "))
            Temp=int(PRODUCTS[j]['count'])
            if Temp>=Amount:
                Temp=int(PRODUCTS[j]['count'])
                Temp= Temp-Amount
                PRODUCTS[j]['count']=str(Temp)
                Update()
                Temp=int(PRODUCTS[j]['price'])
                Total+=Temp
                box.append(PRODUCTS[j]['name'])
                box.append(PRODUCTS[j]['price'])
                A=int(input("Enter 0 to finish Buying or 1 to continue:"))
                Temp=0
                j=0
            else:
                print("This Amount Doesnt Exist")
    print(box)
    print('Total price:',Total)
    Update()
def Search():
    Name =input("Enter the Name of Product:")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==Name:
            j=i
    print(j)
    print(PRODUCTS[j])
################main
PRODUCTS=[]
Load()
Menu()
Choice=int(input('Enter:'))
if Choice==1:
    Add_Product()
if Choice==2:
    Edit_Prodcut()
if Choice==3:
    Delete_Prodcut()
if Choice==4:
    Search()
if Choice==5:
    Show_List()
if Choice==6:
    Buy_Product()
if Choice==8:
    Update()
if Choice==7:
    QR_Code()