# veidosim attēlu galeriju

from tkinter import *
# saīsinājumā PIL, bet ir pillow
from PIL import ImageTk, Image

logs=Tk()
logs.title("Attēlu galerija")
# logs.iconbitmap(".....")

bilde1=ImageTk.PhotoImage(Image.open("C:/Users/Lietotajs/Desktop/programmesana/bildes/galerija/ziema1.png"))
bilde2=ImageTk.PhotoImage(Image.open("C:/Users/Lietotajs/Desktop/programmesana/bildes/galerija/ziema2.png"))
bilde3=ImageTk.PhotoImage(Image.open("C:/Users/Lietotajs/Desktop/programmesana/bildes/galerija/ziema3.png"))

image_list=[bilde1, bilde2, bilde3]
#image_list=[2]
image_number=0
my_label=Label(image=bilde1)


def forward(image_number):
    global my_label 
    global poga_back
    global poga_forward
        
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number+1])

    poga_forward=Button(logs, text=">>", command=lambda:forward(image_number+1))
    poga_back=Button(logs, text="<<", command=lambda:back(image_number-1))

# ko darīt, lai pāršķirot pēdējais nav tukšs
    if image_number==3:
        poga_forward=Button(logs, text=">>", state=DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        poga_back.grid(row=1, column=0)
        poga_forward.grid(row=1, column=2)

    return 


def back(image_number):
    global my_label 
    global poga_back
    global poga_forward
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])

    poga_forward=Button(logs, text=">>", command=lambda:forward(image_number+1))
    poga_back=Button(logs, text="<<", command=lambda:back(image_number-1))
    

    if image_number==1:
        poga_forward=Button(logs, text="<<", state=DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        poga_back.grid(row=1, column=0)
        poga_forward.grid(row=1, column=2)

    return 


my_label.grid(row=0, column=0, columnspan=3)

# pogas
poga_back=Button(logs, text="<<", command=back, state=DISABLED)
poga_forward=Button(logs, text=">>", command=lambda:forward(2))
poga_iziet=Button(logs, text="iziet", command=logs.quit)

poga_back.grid(row=1, column=0)
poga_forward.grid(row=1,column=2)
poga_iziet.grid(row=1, column=1)







logs.mainloop()