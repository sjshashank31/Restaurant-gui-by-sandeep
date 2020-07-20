from tkinter import *
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("1350x750+0+0")
root.title("SANDEEP Restaurant ")
root.configure(background='green')

Tops = Frame(root,bg='green',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='SANDEEP RESTAURANT ',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='blue',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='blue',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='blue',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='blue',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='orange',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='orange',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='orange',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
Food_F.pack(side=RIGHT)
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Bananajuice = StringVar()
E_Grapejuice = StringVar()
E_Pineapple = StringVar()
E_Apple = StringVar()
E_Promaganate = StringVar()
E_Sprite = StringVar()
E_CocaCola = StringVar()
E_Milkshakes = StringVar()

E_Vegbiryani = StringVar()
E_Nonvegbiryani = StringVar()
E_Vegmeals = StringVar()
E_Chapathi = StringVar()
E_Manchuria = StringVar()
E_Noodels = StringVar()
E_Friedrice = StringVar()
E_Frinchfries = StringVar()

E_Bananajuice.set("0")
E_Grapejuice.set("0")
E_Pineapple.set("0")
E_Apple.set("0")
E_Promaganate.set("0")
E_Sprite.set("0")
E_CocaCola.set("0")
E_Milkshakes.set("0")

E_Vegbiryani.set("0")
E_Nonvegbiryani.set("0")
E_Vegmeals.set("0")
E_Chapathi.set("0")
E_Manchuria.set("0")
E_Noodels.set("0")
E_Friedrice.set("0")
E_Frinchfries.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Bananajuice.set("0")
    E_Grapejuice.set("0")
    E_Pineapple.set("0")
    E_Apple.set("0")
    E_Promaganate.set("0")
    E_Sprite.set("0")
    E_CocaCola.set("0")
    E_Milkshakes.set("0")

    E_Vegbiryani.set("0")
    E_Nonvegbiryani.set("0")
    E_Vegmeals.set("0")
    E_Chapathi.set("0")
    E_Manchuria.set("0")
    E_Noodels.set("0")
    E_Friedrice.set("0")
    E_Frinchfries.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtBananajuice.configure(state=DISABLED)
    txtGrapejuice.configure(state=DISABLED)
    txtPineapple.configure(state=DISABLED)
    txtApple.configure(state=DISABLED)
    txtPromaganate.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtMilkshakes.configure(state=DISABLED)
    txtVegbiryani.configure(state=DISABLED)
    txtNonvegbiryani.configure(state=DISABLED)
    txtVegmeals.configure(state=DISABLED)
    txtChapathi.configure(state=DISABLED)
    txtManchuria.configure(state=DISABLED)
    txtNoodels.configure(state=DISABLED)
    txtFriedrice.configure(state=DISABLED)
    txtFrinchfries.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Bananajuice.get())
    Item2=float(E_Grapejuice.get())
    Item3=float(E_Pineapple.get())
    Item4=float(E_Apple.get())
    Item5=float(E_Promaganate.get())
    Item6=float(E_Sprite.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_Milkshakes.get())

    Item9=float(E_Vegbiryani.get())
    Item10=float(E_Nonvegbiryani.get())
    Item11=float(E_Vegmeals.get())
    Item12=float(E_Chapathi.get())
    Item13=float(E_Manchuria.get())
    Item14=float(E_Noodels.get())
    Item15=float(E_Friedrice.get())
    Item16=float(E_Frinchfries.get())

    PriceofDrinks =(Item1 * 40) + (Item2 * 50) + (Item3 * 60) + (Item4 * 60) + (Item5 * 50) + (Item6 * 30) + (Item7 * 30) + (Item8 * 90)

    PriceofFood =(Item9 * 100) + (Item10 * 180) + (Item11 * 120) + (Item12 * 40) + (Item13 * 70) + (Item14 * 80) + (Item15 * 80) + (Item16 * 110)



    DrinksPrice = "Rs",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Rs",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rs",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.05))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.05)
    TC="Rs",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chk_Bananajuice():
    if(var1.get() == 1):
        txtBananajuice.configure(state = NORMAL)
        txtBananajuice.focus()
        txtBananajuice.delete('0',END)
       
    elif(var1.get() == 0):
        txtBananajuice.configure(state = DISABLED)
        E_Bananajuice.set("0")

def chk_Grapejuice():
    if(var2.get() == 1):
        txtGrapejuice.configure(state = NORMAL)
        txtGrapejuice.focus()
        txtGrapejuice.delete('0',END)
       
    elif(var2.get() == 0):
        txtGrapejuice.configure(state = DISABLED)
        E_Grapejuice.set("0")

def chk_Pineapple():
    if(var3.get() == 1):
        txtPineapple.configure(state = NORMAL)
        txtPineapple.delete('0',END)
        txtPineapple.focus()
    elif(var3.get() == 0):
        txtPineapple.configure(state = DISABLED)
        E_Pineapple.set("0")

def chk_Apple():
    if(var4.get() == 1):
        txtApple.configure(state = NORMAL)
        txtApple.delete('0',END)
        txtApple.focus()
    elif(var4.get() == 0):
        txtApple.configure(state = DISABLED)
        E_Apple.set("0")

def chk_Promaganate():
    if(var5.get() == 1):
        txtPromaganate.configure(state = NORMAL)
        txtPromaganate.delete('0',END)
        txtPromaganate.focus()
    elif(var5.get() == 0):
        txtPromaganate.configure(state = DISABLED)
        E_Promaganate.set("0")

def chk_Sprite():
    if(var6.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.delete('0',END)
        txtSprite.focus()
    elif(var6.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_Milkshakes():
    if(var8.get() == 1):
        txtMilkshakes.configure(state = NORMAL)
        txtMilkshakes.delete('0',END)
        txtMilkshakes.focus()
    elif(var8.get() == 0):
        txtMilkshakes.configure(state = DISABLED)
        E_Milkshakes.set("0")

def chk_Vegbiryani():
    if(var9.get() == 1):
        txtVegbiryani.configure(state = NORMAL)
        txtVegbiryani.delete('0',END)
        txtVegbiryani.focus()
    elif(var9.get() == 0):
        txtVegbiryani.configure(state = DISABLED)
        E_Vegbiryani.set("0")

def chk_Nonvegbiryani():
    if(var10.get() == 1):
        txtNonvegbiryani.configure(state = NORMAL)
        txtNonvegbiryani.delete('0',END)
        txtNonvegbiryani.focus()
    elif(var10.get() == 0):
        txtNonvegbiryani.configure(state = DISABLED)
        E_Nonvegbiryani.set("0")

def chk_Vegmeals():
    if(var11.get() == 1):
        txtVegmeals.configure(state = NORMAL)
        txtVegmeals.delete('0',END)
        txtVegmeals.focus()
    elif(var11.get() == 0):
        txtVegmeals.configure(state = DISABLED)
        E_Vegmeals.set("0")

def chk_Chapathi():
    if(var12.get() == 1):
        txtChapathi.configure(state = NORMAL)
        txtChapathi.delete('0',END)
        txtChapathi.focus()
    elif(var12.get() == 0):
        txtChapathi.configure(state = DISABLED)
        E_Chapathi.set("0")

def chk_Manchuria():
    if(var13.get() == 1):
        txtManchuria.configure(state = NORMAL)
        txtManchuria.delete('0',END)
        txtManchuria.focus()
    elif(var13.get() == 0):
        txtManchuria.configure(state = DISABLED)
        E_Manchuria.set("0")

def chk_Noodels():
    if(var14.get() == 1):
        txtNoodels.configure(state = NORMAL)
        txtNoodels.delete('0',END)
        txtNoodels.focus()
    elif(var14.get() == 0):
        txtNoodels.configure(state = DISABLED)
        E_Noodels.set("0")

def chk_Friedrice():
    if(var15.get() == 1):
        txtFriedrice.configure(state = NORMAL)
        txtFriedrice.delete('0',END)
        txtFriedrice.focus()
    elif(var15.get() == 0):
        txtFriedrice.configure(state = DISABLED)
        E_Friedrice.set("0")

def chk_Frinchfries():
    if(var16.get() == 1):
        txtFrinchfries.configure(state = NORMAL)
        txtFrinchfries.delete('0',END)
        txtFrinchfries.focus()
    elif(var16.get() == 0):
        txtFrinchfries.configure(state = DISABLED)
        E_Frinchfries.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Bananajuice:\t\t\t\t\t' + E_Bananajuice.get() +'\n')
    txtReceipt.insert(END,'Grapejuice:\t\t\t\t\t'+ E_Grapejuice.get()+'\n')
    txtReceipt.insert(END,'Pineapple:\t\t\t\t\t'+ E_Pineapple.get()+'\n')
    txtReceipt.insert(END,'Apple:\t\t\t\t\t'+ E_Apple.get()+'\n')
    txtReceipt.insert(END,'Promaganate:\t\t\t\t\t'+ E_Promaganate.get()+'\n')
    txtReceipt.insert(END,'Sprite:\t\t\t\t\t'+ E_Sprite.get()+'\n')
    txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(END,'Milkshakes:\t\t\t\t\t'+ E_Milkshakes.get()+'\n')
    txtReceipt.insert(END,'Vegbiryani:\t\t\t\t\t'+ E_Vegbiryani.get()+'\n')
    txtReceipt.insert(END,'Nonvegbiyani:\t\t\t\t\t'+ E_Nonvegbiryani.get()+'\n')
    txtReceipt.insert(END,'Vegmeals:\t\t\t\t\t'+ E_Vegbiryani.get()+'\n')
    txtReceipt.insert(END,'Chapathi:\t\t\t\t\t'+ E_Chapathi.get()+'\n')
    txtReceipt.insert(END,'Manchuria:\t\t\t\t\t'+ E_Manchuria.get()+'\n')
    txtReceipt.insert(END,'Noodels:\t\t\t\t\t'+ E_Noodels.get()+'\n')
    txtReceipt.insert(END,'Friedrice:\t\t\t\t\t'+ E_Friedrice.get()+'\n')
    txtReceipt.insert(END,'Frinchfries:\t\t\t\t\t'+ E_Frinchfries.get()+'\n')
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


#########################################Drinks####################################################################
Bananajuice=Checkbutton(Drinks_F,text='Bananajuice',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Bananajuice).grid(row=0,sticky=W)
Grapejuice=Checkbutton(Drinks_F,text='Grapejuice',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Grapejuice).grid(row=1,sticky=W)
Pineapple=Checkbutton(Drinks_F,text='Pineapple',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Pineapple).grid(row=2,sticky=W)
Apple=Checkbutton(Drinks_F,text='Apple',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Apple).grid(row=3,sticky=W)
Promaganate=Checkbutton(Drinks_F,text='Promaganate',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Promaganate).grid(row=4,sticky=W)
Sprite=Checkbutton(Drinks_F,text='Sprite',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Sprite).grid(row=5,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='CocaCola',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_CocaCola).grid(row=6,sticky=W)

Milkshakes=Checkbutton(Drinks_F,text='Milkshakes',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='orange',command=chk_Milkshakes).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################

txtBananajuice = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Bananajuice)
txtBananajuice.grid(row=0,column=1)

txtGrapejuice = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Grapejuice)
txtGrapejuice.grid(row=1,column=1)

txtPineapple = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Pineapple)
txtPineapple.grid(row=2,column=1)

txtApple= Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Apple)
txtApple.grid(row=3,column=1)

txtPromaganate = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Promaganate)
txtPromaganate.grid(row=4,column=1)

txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtMilkshakes = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Milkshakes)
txtMilkshakes.grid(row=7,column=1)
#############################################Foods######################################################################

Vegbiryani = Checkbutton(Food_F,text="Vegbiryani ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Vegbiryani).grid(row=0,sticky=W)
Nonvegbiyani = Checkbutton(Food_F,text="Nonvegbiyani",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Nonvegbiryani).grid(row=1,sticky=W)
Vegmeals = Checkbutton(Food_F,text="Vegmeals ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Vegmeals).grid(row=2,sticky=W)
Chapathi = Checkbutton(Food_F,text="Chapathi ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Chapathi).grid(row=3,sticky=W)
Manchuria = Checkbutton(Food_F,text="Manchuria ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Manchuria).grid(row=4,sticky=W)
Noodels = Checkbutton(Food_F,text="Noodels ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Noodels).grid(row=5,sticky=W)
Friedrice = Checkbutton(Food_F,text="Friedrice ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Friedrice).grid(row=6,sticky=W)
Frinchfries = Checkbutton(Food_F,text="Frinchfries ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='orange',command=chk_Frinchfries).grid(row=7,sticky=W)
################################################Entry Box For Cake##########################################################
txtVegbiryani=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Vegbiryani)
txtVegbiryani.grid(row=0,column=1)

txtNonvegbiryani=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Nonvegbiryani)
txtNonvegbiryani.grid(row=1,column=1)

txtVegmeals=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Vegmeals)
txtVegmeals.grid(row=2,column=1)

txtChapathi=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Chapathi)
txtChapathi.grid(row=3,column=1)

txtManchuria=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Manchuria)
txtManchuria.grid(row=4,column=1)

txtNoodels=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Noodels)
txtNoodels.grid(row=5,column=1)

txtFriedrice=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Friedrice)
txtFriedrice.grid(row=6,column=1)

txtFrinchfries=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Frinchfries)
txtFrinchfries.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='orange',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='orange',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='orange',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='orange',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='orange',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='orange',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)



###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='orange',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='orange',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='orange',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='orange',command=iExit).grid(row=0,column=3)

###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='orange',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='orange',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='orange',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='orange',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='orange',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='orange',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='orange',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='orange',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='orange',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='orange',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='orange',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='orange',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='orange',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='orange',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='orange',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='orange',command=lambda:btnClick('/')).grid(row=5,column=3)







root.mainloop()
