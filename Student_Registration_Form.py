
import tkinter as tk
import tkinter.ttk as ttk



root = tk.Tk()
root.geometry('500x600')
root.title("Tkinter Hub")


student_data = [[1,'Rishikesh','rishiddinde@gmail.com','Python'],
                [2,'Shiva','Shiva@gmail.com','Python,c++'],
                [3,'Shardul','Shardul@gmail.com','Java'],
                [4,'Varun','varunmangla@gmail.com','Python,sql,Autocad'],
                [5,'Pawan','Pawan@gmail.com','Python,Autocad'],
                [6,'Aditya','Aditya@gmail.com','Python,Autocad']]

def load_student_data():
    for item in record_table.get_children():
        record_table.delete(item)
        
    
    for r in range(len(student_data)):
        record_table.insert(parent='',index='end',text='',iid=r,values=student_data[r])

def put_student_in_entry(index):
    student_id.delete(0,tk.END)
    student_name.delete(0,tk.END)
    student_email_id.delete(0,tk.END)
    student_cources.delete(0,tk.END)

    stud_id = student_data[index][0]
    stud_name = student_data[index][1]
    stud_email_id = student_data[index][2]
    stud_cources = student_data[index][3]
    

    student_id.insert(0,stud_id)
    student_name.insert(0,stud_name)
    student_email_id.insert(0,stud_email_id)
    student_cources.insert(0,stud_cources)

def clear_student_data():
    student_id.delete(0,tk.END)
    student_name.delete(0,tk.END)
    student_email_id.delete(0,tk.END)
    student_cources.delete(0,tk.END) 

    load_student_data()

def add_student_data(stud_id, stud_name, stud_email,  stud_cources):
    student_data.append([stud_id,stud_name,stud_email,stud_cources])  

    load_student_data()
    clear_student_data()

def update_student_data(stud_id, stud_name, stud_email, stud_cources,index):
    student_data[index]=[stud_id,stud_name,stud_email,stud_cources]
    load_student_data()
    clear_student_data()

def delete_student_data(index):
    del student_data[index]
    load_student_data()
    clear_student_data()

def find_student_id(stud_id):
    if stud_id!='':
        student_data_index=[]
        for data in student_data:
            if str(stud_id) in str(data[0]):
                student_data_index.append(student_data.index(data)) 
    
        for item in record_table.get_children():
            record_table.delete(item)
        
        for r in student_data_index:
            record_table.insert(parent='',index='end',text='',iid=r,values=student_data[r])
    else:
        load_student_data()

def getvalue():
    print(student_name.get())


head_frame = tk.Frame(root,bg=('orange'))
heading_lb = tk.Label(head_frame,text="Student Registration Form",font=('Bold',15),bg="bisque2",fg='blue')
heading_lb.pack(fill=tk.X,pady=0)


#add parameter and entry for that


student_id_lb = tk.Label(head_frame,text='Student id:',font=('Bold',13),bg=('sandy brown')).place(x=10,y=60)
student_id = tk.Entry(head_frame,font=('Bold',12))
student_id.place(x=130,y=63)

student_name_lb = tk.Label(head_frame,text='Student name:',font=('Bold',13),bg=('sandy brown')).place(x=10,y=100)
student_name = tk.Entry(head_frame,font=('Bold',12))
student_name.place(x=130,y=103)


student_email_id_lb = tk.Label(head_frame,text='Email id:',font=('Bold',13),bg=('sandy brown')).place(x=10,y=150)
student_email_id = tk.Entry(head_frame,font=('Bold',12))
student_email_id.place(x=130,y=153)

student_cources_lb = tk.Label(head_frame,text='Cources:',font=('Bold',13),bg=('sandy brown')).place(x=10,y=200)
student_cources = tk.Entry(head_frame,font=('Bold',12))
student_cources.place(x=130,y=203)

#create button
Register_button = tk.Button(head_frame,text='Register',font=('Bold',12),bg='cyan2',command=lambda:add_student_data(student_id.get(),student_name.get(),student_email_id.get(),student_cources.get()))
# Register_button = tk.Button(head_frame,text='Register',font=('Bold',12))
Register_button.place(x=10,y=250)

Update_button = tk.Button(head_frame,text='Update',font=('Bold',12),bg='cyan2',command=lambda:update_student_data(student_id.get(),student_name.get(),student_email_id.get(),student_cources.get(),index=int(record_table.selection()[0])))
Update_button.place(x=110,y=250)

Delete_button = tk.Button(head_frame,text='Delete',font=('Bold',12),bg='red',command=lambda:delete_student_data(index=int(record_table.selection()[0])))
Delete_button.place(x=200,y=250)

Clear_button = tk.Button(head_frame,text='Clear',font=('Bold',12),bg='cyan2',command=lambda:clear_student_data())
Clear_button.place(x=280,y=250)


#Total frame of size 400x300 created
head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400,height=300)

#search frame
serch_frame = tk.Frame(root)
serch_lb = tk.Label(serch_frame,text="Serch Student By ID:",font=('Bold',10),bg="bisque2",fg='blue')
serch_lb.pack(anchor=tk.W)

serch_entry = tk.Entry(serch_frame,font=('Bold',10))
serch_entry.pack(anchor=tk.W)
serch_entry.bind('<KeyRelease>',lambda e: find_student_id(serch_entry.get()))


serch_frame.pack(pady=0)
serch_frame.pack_propagate(False)
serch_frame.configure(width=150,height=50)

Record_frame = tk.Frame(root)
Record_lb = tk.Label(Record_frame,text="Select record for Delet or Update",font=('Bold',13),bg="bisque2",fg='blue')
Record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(Record_frame)
record_table.pack(fill=tk.X,pady=5)
record_table.bind('<<TreeviewSelect>>',lambda e:put_student_in_entry(int(record_table.selection()[0])))

record_table['column']=['ID','Name','Email','Courses']

record_table.column('#0',anchor=tk.W, width = 0,stretch=tk.NO)

record_table.column('ID',anchor=tk.W, width = 50)
record_table.column('Name',anchor=tk.W, width = 100)
record_table.column('Email',anchor=tk.W, width = 150)
record_table.column('Courses',anchor=tk.W, width =120)

record_table.heading('ID',text='Id',anchor=tk.W)
record_table.heading('Name',text='Name',anchor=tk.W)
record_table.heading('Email',text='Email',anchor=tk.W)
record_table.heading('Courses',text='Courses',anchor=tk.W)


# serch_name = tk.Entry(serch_frame,font=('Bold',10))
# serch_name.pack(anchor=tk.W)

Record_frame.pack(pady=10)
Record_frame.pack_propagate(False)
Record_frame.configure(width=400,height=200)
load_student_data()


root.mainloop()