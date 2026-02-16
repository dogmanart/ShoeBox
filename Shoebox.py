import customtkinter as ctk
import tkinter
import json
from tkinter import messagebox

savefile = "Save.json"

collectionlist = []
cardbelonging = []
cardslist = []
cardnames = []
cardyears = []
cardextras = []
cardgrades = []
cardbrand = []
cardbordref = []
cardidentno = []

def save():
      data = {
        "collections": collectionlist,
        "cards": cardslist,
        "belonging": cardbelonging,
        "names": cardnames,
        "years": cardyears,
        "extras": cardextras,
        "grades": cardgrades,
        "brands": cardbrand,
        "borders": cardbordref,
        "idents": cardidentno
    }

      with open(savefile, 'w') as f:
            json.dump(data, f)

def load():
    global collectionlist, cardslist, cardbelonging, cardnames, cardyears
    global cardextras, cardgrades, cardbrand, cardbordref, cardidentno
    try:
        with open(savefile, 'r') as f:
            data = json.load(f)
            collectionlist = data.get("collections", ["My Collection"])
            cardslist = data.get("cards", [])
            cardbelonging = data.get("belonging", [])
            cardnames = data.get("names", [])
            cardyears = data.get("years", [])
            cardextras = data.get("extras", [])
            cardgrades = data.get("grades", [])
            cardbrand = data.get("brands", [])
            cardbordref = data.get("borders", [])
            cardidentno = data.get("idents", [])
    except FileNotFoundError:
        pass

window = ctk.CTk()
window.title("ShoeBox2")
window.iconbitmap("Shoeboxlogo2 (1).ico")
window.geometry("805x505")

ctk.set_appearance_mode("dark")

collectionlist = []
cardbelonging = []

def closewindow():
    save()
    window.destroy()

appframe = ctk.CTkFrame(window,width=805, height=505, fg_color="#333333", corner_radius=15)
appframe.pack(side='left', expand=True)

topframe = ctk.CTkFrame(appframe, width=800, height=50, corner_radius=15, fg_color="#DB802B")
topframe.pack(side='top', pady=5)
topframe.grid_propagate(False)

def back():
      searchbox.delete(0, 'end')
      refreshcards("")

backbutton = ctk.CTkButton(topframe, text="Back", corner_radius=10, width=30, fg_color="#EB9647", hover_color="#c4721b", command=back)
backbutton.grid(row=0, column=0, pady=10, padx=10, sticky='news')

closebutton = ctk.CTkButton(topframe, text="Close", corner_radius=10, width=30, fg_color="#Eb9647", hover_color="#c4721b", command=closewindow)
closebutton.grid(row=0, column=3, pady=10, padx=475, sticky='e')

searchbox = ctk.CTkEntry(topframe, fg_color="#e6a454", border_color="#c4721b",placeholder_text="Search...", placeholder_text_color="#555555", text_color="#000000")
searchbox.grid(row=0, column=1)

def searchfunct():
      cardsframe._parent_canvas.yview_moveto(0)
      refreshcards(searchbox.get().lower())

searchbutton = ctk.CTkButton(topframe, corner_radius=15, text="🔍 ", fg_color="#Eb9647", hover_color="#c4721b", width=1, command=searchfunct)
searchbutton.grid(row=0, column=2, padx=5)

collectionsframe = ctk.CTkFrame(appframe, width=120, height=445, corner_radius=12)
collectionsframe.pack(side='left', pady=10, padx=5)
collectionsframe.pack_propagate(False)

def rmvcollection():
      global collectionselect 
      if len(collectionlist) > 1:
            choice = messagebox.askyesno("Warning",f"Are you sure you want to delete the '{collectionselect.get()}' collection?")
            if choice:
                  collectionlist.remove(collectionselect.get())
                  for i in range(len(cardbelonging) - 1, -1, -1):
                        if cardbelonging[i] == collectionselect.get():
                              cardslist.pop(i)
                              cardnames.pop(i)
                              cardyears.pop(i)
                              cardextras.pop(i)
                              cardgrades.pop(i)
                              cardbrand.pop(i)
                              cardbordref.pop(i)
                              cardidentno.pop(i)
                              cardbelonging.pop(i)
                              save()
                  collectionselect.set(collectionlist[0])
                  collectionselect.configure(values=collectionlist)
                  refreshcards("")
      else:
            pass

newcollectionentry = ctk.CTkEntry(collectionsframe, fg_color="#e6a454", border_color="#c4721b",placeholder_text="Collection Name", placeholder_text_color="#555555", text_color="#000000")
donenewcollect = ctk.CTkButton(collectionsframe, text="Done", font=("Arial", 10), fg_color="#Eb9647", hover_color="#c4721b")
deletecollection = ctk.CTkButton(collectionsframe, text="Delete Collection", font=("Arial", 10), fg_color="#Eb9647", hover_color="#c4721b", command=rmvcollection)

def addcollection():
        global newcollectionentry, donenewcollect
        newcollectionentry = ctk.CTkEntry(collectionsframe, fg_color="#e6a454", border_color="#c4721b",placeholder_text="Collection Name", placeholder_text_color="#555555", text_color="#000000", font=("Arial", 10))     
        newcollectionentry.pack_forget()
        deletecollection.pack_forget()
        newcollectionentry.pack(pady=10, padx=5)
        newcollection.configure(state='disabled')
        donenewcollect = ctk.CTkButton(collectionsframe, text="Done", font=("Arial", 10), fg_color="#Eb9647", hover_color="#c4721b", command=donenewcol)
        donenewcollect.pack(pady=10, padx=5)

def donenewcol():
      global newcollectionentry, donenewcollect, collectionlist, collectionselect
      newcollection.configure(state= 'normal')
      newcollectionentry.pack_forget()
      
      val = newcollectionentry.get()
      if val:
            collectionlist.append(newcollectionentry.get())
            save()
      donenewcollect.pack_forget()
      collectionselect.configure(values=collectionlist)
      deletecollection.pack(pady=10, padx=5)
      refreshcards("")

collectionselect = ctk.CTkComboBox(collectionsframe, values=collectionlist, font=("Arial", 10), command=lambda _: refreshcards(""))
collectionselect.pack(pady=10, padx=5)

newcollection = ctk.CTkButton(collectionsframe, text="+ New Collection", font=("Arial", 10), fg_color="#Eb9647", hover_color="#c4721b",command=addcollection)
newcollection.pack(pady=10, padx=5)

deletecollection.pack(pady=10, padx=5)

cardslist = []
cardnames = []
cardyears = []
cardextras = []
cardgrades = []
cardbrand = []
cardbordref = []
cardidentno = []

def addnewcard():
      def doneinfo():
            cardnames.append(namebox.get())
            cardyears.append(yearselect.get())
            cardextras.append(detailsselect.get())
            cardgrades.append(gradeselect.get())
            cardbrand.append(brandselect.get())
            cardbordref.append(bordselect.get())
            cardidentno.append(identselect.get())
            cardbelonging.append(collectionselect.get())
            cardfull = str(yearselect.get()+" "+brandselect.get()+" "+bordselect.get()+" "+namebox.get())
            cardslist.append(cardfull)
            save()
            refreshcards("")
            cardinfowindow.destroy()

      def closeinfo():
            cardinfowindow.destroy()

      cardinfowindow = ctk.CTkToplevel(window)
      cardinfowindow.title("ShoeBox2 - Card info")
      cardinfowindow.geometry("500x500")
      cardinfowindow.iconbitmap("Shoeboxlogo2 (1).ico")
      cardinfowindow.attributes("-topmost", True)

      infoappframe = ctk.CTkFrame(cardinfowindow,width=500, height=500, fg_color="#333333", corner_radius=15)
      infoappframe.pack(side='left', expand=True)
      infoappframe.pack_propagate(False)

      infotopframe = ctk.CTkFrame(infoappframe, width=800, height=50, corner_radius=15, fg_color="#DB802B")
      infotopframe.pack(side='top', pady=5, padx=5)
      infotopframe.grid_propagate(False)

      namebox = ctk.CTkEntry(infotopframe, fg_color="#e6a454", border_color="#c4721b",placeholder_text="Full Name", placeholder_text_color="#555555", text_color="#000000")
      namebox.grid(row=0, column=0, pady=10, padx=5)

      gradetxt = ctk.CTkLabel(infoappframe, text="Grade:", font=("Arial", 10))
      gradetxt.pack(padx=5, pady=1)
      gradeselect = ctk.CTkComboBox(infoappframe, values=["Gem Mint: 10", "Mint: 9-9.5","Near Mint: 7-8", "Lightly Played: 5-6", "Moderately Played: 3-4", "Heavily Played: 1-2", "Raw"], corner_radius=9, fg_color="#e6a454", text_color="#333333", font=("Arial", 10))
      gradeselect.pack( padx=5, pady=4)

      yeartxt = ctk.CTkLabel(infoappframe, text="Year:", font=("Arial", 10))
      yeartxt.pack(padx=5, pady=2)
      yearselect = ctk.CTkEntry(infoappframe, corner_radius=9, fg_color="#e6a454", text_color="#333333", font=("Arial", 10))
      yearselect.pack(padx=5, pady=3)

      brandtxt = ctk.CTkLabel(infoappframe, text="Brand:", font=("Arial", 10))
      brandtxt.pack(padx=5, pady=2)
      brandselect = ctk.CTkEntry(infoappframe, corner_radius=9, fg_color="#e6a454", text_color="#333333", font=("Arial", 10), )
      brandselect.pack(padx=5, pady=3, )

      bordtxt = ctk.CTkLabel(infoappframe, text="Border/Foil/Refractor:", font=("Arial", 10))
      bordtxt.pack(padx=5, pady=2)
      bordselect = ctk.CTkEntry(infoappframe, corner_radius=9, fg_color="#e6a454", text_color="#333333", font=("Arial", 10), )
      bordselect.pack(padx=5, pady=3, )

      detailstxt = ctk.CTkLabel(infoappframe, text="Details:", font=("Arial", 10))
      detailstxt.pack(padx=5, pady=2)
      detailsselect = ctk.CTkEntry(infoappframe, corner_radius=9, fg_color="#d3d3d3", text_color="#333333", font=("Arial", 10), )
      detailsselect.pack(padx=5, pady=3, )

      identtxt = ctk.CTkLabel(infoappframe, text="Identification #:", font=("Arial", 10))
      identtxt.pack(padx=5, pady=2)
      identselect = ctk.CTkEntry(infoappframe, corner_radius=9, fg_color="#d3d3d3", text_color="#333333", font=("Arial", 10), )
      identselect.pack(padx=5, pady=3, )

      infoclose = ctk.CTkButton(infotopframe, text="Close",width=30, corner_radius=15, fg_color="#Eb9647", hover_color="#c4721b", command=closeinfo)
      infoclose.grid(row=0, column=1, pady=10, padx=270, sticky='e')

      infobotframe = ctk.CTkButton(infoappframe, text="Done",width=800, height=50, corner_radius=15, fg_color="#DB802B", hover_color="#c4721b", command=doneinfo)
      infobotframe.pack(side='bottom', pady=5, padx=5)
      infobotframe.grid_propagate(False)

cardsframe= ctk.CTkScrollableFrame(appframe, width=640, height=420, corner_radius=12)
cardsframe.pack(pady=10, padx=10, )

def delete_card(index, windowdes):
      windowdes.destroy()
      if messagebox.askyesno("Delete", f"Are you sure you want to delete '{cardslist[index]}'?"):
        cardslist.pop(index)
        cardnames.pop(index)
        cardyears.pop(index)
        cardextras.pop(index)
        cardgrades.pop(index)
        cardbrand.pop(index)
        cardbordref.pop(index)
        cardidentno.pop(index)
        cardbelonging.pop(index)
        
        save()
        refreshcards("")

def showdetails(indexno):
      detailswindow = ctk.CTkToplevel(window)
      detailswindow.title("ShoeBox2 - Card Info")
      detailswindow.iconbitmap("Shoeboxlogo2 (1).ico")
      detailswindow.geometry("500x600")
      detailswindow.attributes("-topmost", True)

      detwindframe = ctk.CTkFrame(detailswindow)
      detwindframe.pack(expand=True, pady=10, padx=10)

      detailsframe = ctk.CTkFrame(detwindframe, width=400, height=400)
      detailsframe.pack(expand=True, pady=10, padx=10)
      detailsframe.pack_propagate(False)

      detailsname = (f"Name: {str(cardnames[indexno]).lstrip()}\n"
               f"{str(cardidentno[indexno]).lstrip()}\n"
               f"Grade: {str(cardgrades[indexno]).lstrip()}\n")
      details = f"{detailsname}\n\n{cardextras[indexno]}"
      detailstext = ctk.CTkLabel(detailsframe, text=details, font=("Arial",12), justify='left')
      detailstext.pack(anchor='nw', padx=10, pady =10)

      deletebutton = ctk.CTkButton(detwindframe, text="Delete Card", command=lambda: delete_card(indexno, detailswindow), fg_color="#Eb9647", hover_color="#c4721b")
      deletebutton.pack(side='bottom', padx=10, pady=10)

      def detailsgone():
            detailswindow.destroy()

      detclosebutton = ctk.CTkButton(detwindframe, text="Close", fg_color="#Eb9647", hover_color="#c4721b", command=detailsgone)
      detclosebutton.pack(side='bottom', padx=10, pady=10)

def refreshcards(searchquery):
      for widget in cardsframe.winfo_children():
            widget.destroy()
      colcount = cardbelonging.count(collectionselect.get())
      newcardbutton = ctk.CTkButton(cardsframe, text=f"+ New Card\n({colcount} cards)", width=160, height=220, fg_color="#Eb9647", hover_color="#c4721b", corner_radius=15, border_color="#ffffff", border_width=1, font=("Arial", 14), command=addnewcard)
      newcardbutton.grid(row=0, column=0, pady=5, padx=5, sticky="nw")
      displaycount = 1
      for index, cardtext in enumerate(cardslist):
            if cardbelonging[index] == collectionselect.get():
                  if searchquery == "" or searchquery in str(cardtext).lower() or searchquery in str(cardextras[index]).lower():
                        r, c = divmod(displaycount,3)
                        card = ctk.CTkButton(cardsframe, text=cardtext, width=155, height=220, fg_color="#db802b", hover_color="#c4721b", corner_radius=15, border_color="#ffffff", border_width=1, font=("Arial", 14), command=lambda i=index: showdetails(i))
                        card.grid(row=r, column=c, padx=5, pady=5, sticky='nw')
                        card._text_label.configure(wraplength=270)
                        displaycount +=1

load()

collectionselect.configure(values=collectionlist)
if collectionlist:
    collectionselect.set(collectionlist[0])

refreshcards("")
window.mainloop()
