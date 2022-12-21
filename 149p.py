from tkinter import *
import random
root=Tk()
root.geometry("444x444")
root.title("Random Alphabet")
label1=Label(root)
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z']
print(list1)
def randomlist():
    random_no1=random.randint(0,25)
    random_no2=random.randint(0,25)
    random_no3 =random.randint(0,25)
    random_no4 =random.randint(0,25)
    random_no5 =random.randint(0,25)
    random_name1=list1[random_no1]
    random_name2=list1[random_no2]
    random_name3=list1[random_no3]
    random_name4=list1[random_no4]
    random_name5=list1[random_no5]
    label1["text"]=random_name1+random_name2+random_name3+random_name4+random_name5
btn=Button(root,text="Random Alphabet",command=randomlist)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()