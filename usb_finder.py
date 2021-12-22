from tkinter import *
import subprocess , json
root=Tk()
root.title("Usb Findr 0.358v By Sarthak And ShreeLakshmi MAM :D")
root.geometry("1980x1080")
#label
out = subprocess.getoutput("powershell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName| ConvertTo-Json}\"") 
e1=Label(root, text="Status",font=('Helvatika',10,'bold')) 
e1.grid(row=0,column=0,padx=5,pady=5) 
e1=Label(root, text="Class",font=('Helvatika',10,'bold'))
e1.grid(row=0,column=1,padx=5,pady=5) 
e1=Label(root, text="Friendly Name",font=('Helvatika',10,'bold'))
e1.grid(row=0,column=2,padx=5,pady=5)
count =1
json_data = json.loads(out)

for dev in json_data:
    print(dev)
    #dev done but not full comp 40% done
    if count <= 13:
       lst=[[dev['Status'],dev['Class'],dev['FriendlyName']]]
       total_row = len(lst)
       total_collum=len(lst[0])

       for i in range (total_row):
           for j in range (total_collum):
               
                b = Entry(root,width="35",fg='blue',font=("Arial","10","bold"))
                b.grid(row=count, column=j,ipadx=5,ipady=5,columnspan=2 )
                b.insert(END,lst[i][j])
       count=count+1
       print(count)

root.mainloop()