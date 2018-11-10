'''Wikipedia Search Engine'''

from tkinter import *
import wikipedia

#Creating the function to make the Button work
def info():
    string_entered = entry.get()#Getting the input
    text.delete(1.0,END)#Deleting previous results
    try:
        result = wikipedia.summary(string_entered) #Fetching Information from wikipedia
        text.insert(INSERT,result)#Printing the Information fetched by Wikipedia
    except:
        text.insert(INSERT,'Hey! Kindly Enter a valid input.')
        text.insert(INSERT,'\nOr Check your Internet Connectivity.')
        text.insert(INSERT,'\nCOMMON! TRY AGAIN! NEVER LOSE HOPE! NEVER GIVE UP!!')
        
    
    

root = Tk()
topFrame = Frame(root) #Creating the Top Frame
entry = Entry(topFrame) #Creating Entry box(single line text box)
entry.pack()

button = Button(topFrame,text='Search',command=info).pack() #Creating Search Button

topFrame.pack(side=TOP) #Top Frame Over

bottomFrame = Frame(root) #Creating Bottom Frame

scroll = Scrollbar(bottomFrame) #Creating Scroll Bar
scroll.pack(side=RIGHT,fill=Y)
text = Text(bottomFrame,width=40,height=20,yscrollcommand=scroll.set,wrap=WORD) #Creating the Multi-Line Textbox
scroll.config(command=text.yview)
text.pack()


bottomFrame.pack() #Bottom Frame Over

root.geometry('500x500+100+100')
root.mainloop()
