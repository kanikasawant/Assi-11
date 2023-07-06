import tkinter as tk
import webbrowser as wb
root=tk.Tk()
#changing the title of the window
root.title("window")
#username
l1=tk.Label(root,text="Username: ",
            font=("Times New Roman",25),
            width=30)
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",25),bg="pink",width=30)
e1.grid()

#password
l2=tk.Label(root,text="Password: ",
            font=("Times New Roman",25),
            width=30)
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",25),bg="pink",show="*",width=30)
e2.grid()


#email
l3=tk.Label(root,text="Email ",
            font=("Times New Roman",25),
            width=30)
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",25),bg="pink",show=".",width=30)
e3.grid()

#displaymessage
l4=tk.Label(root,text=" ",
            font=("Times New Roman",15),
            height=2)
l4.grid()

#condition

def store():
    print()
    user=e1.get()
    passwd=e2.get()
    id=e3.get()
    print(user)
    print(passwd)
    print(id)
    wb.open("https://help.voot.com/categories/frequently-asked-questions/644441c5653d8255a05ee109")
    
    # if user=="" and passwd=="":
    #     f=open("backend.txt","+w")
    #     f.writelines(["Username: ",user,"\nPassword: ",passwd])
    #     l5["text"]="data has been updated successfully!!\nCheck backend.txt"
    # else:
    #     l5["text"]="invalid username or password"
    if e1.get() =="": 
        l4["text"]="fill all the information"
    else:
        f=open("data.txt","+w")
        f.writelines(["username:",user,
                      "\npassword:",passwd,
                      "\nemail:",id])
        wb.open("https://www.voot.com/")
    if e2.get() =="": 
        l4["text"]="fill all the information"
    else:
        f=open("data.txt")
        f.writelines(["username:",user,
                      "\npassword:",passwd,
                      "\nemail:",id])
    if e3.get() =="": 
        l4["text"]="fill all the information"
    else:
        f=open("data.txt")
        f.writelines(["username:",user,
                      "\npassword:",passwd,
                      "\nemail:",id])        
#button
b=tk.Button(root,text="Submit",
            font=("Times New Roman",25),
            bg="brown",
            activebackground="yellow",
            command=store
            ).grid()        
root.mainloop()