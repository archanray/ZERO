try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
	from tkinter import *
import numpy as np
import os

user_filename = ''

b3 = None

user_fields = ['House number', 'House address', 'Country', 'State', 'City', 'PIN']
text_box11 = text_box12 = text_box13 = text_box14 = text_box15 = text_box16 = None
row11 = row12 = row13 = row14 = row15 = row16 = None
lab11 = lab12 = lab13 = lab14 = lab15 = lab16 = None

device_fields = ['Name', 'Day', 'Time slots', 'Duration', 'Interruptable', 'Priority']
text_box21 = text_box22 = text_box23 = text_box24 = text_box25 = text_box26 = None
row21 = row22 = row23 = row24 = row25 = row26 = None
lab21 = lab22 = lab23 = lab24 = lab25 = lab26 = None

user_data = None

modeint = None

def close_all():
	global row11, text_box11, lab11
	global row12, text_box12, lab12
	global row13, text_box13, lab13
	global row14, text_box14, lab14
	global row15, text_box15, lab15
	global row16, text_box16, lab16

	global row21, text_box21, lab21
	global row22, text_box22, lab22
	global row23, text_box23, lab23
	global row24, text_box24, lab24
	global row25, text_box25, lab25
	global row26, text_box26, lab26

	if row11 != None:
		row11.destroy()
		text_box11.destroy()
		lab11.destroy()

		row12.destroy()
		text_box12.destroy()
		lab12.destroy()

		row13.destroy()
		text_box13.destroy()
		lab13.destroy()

		row14.destroy()
		text_box14.destroy()
		lab14.destroy()

		row15.destroy()
		text_box15.destroy()
		lab15.destroy()

		row16.destroy()
		text_box16.destroy()
		lab16.destroy()

	if row21 != None:

		row21.destroy()
		text_box21.destroy()
		lab21.destroy()

		row22.destroy()
		text_box22.destroy()
		lab22.destroy()

		row23.destroy()
		text_box23.destroy()
		lab23.destroy()

		row24.destroy()
		text_box24.destroy()
		lab24.destroy()

		row25.destroy()
		text_box25.destroy()
		lab25.destroy()

		row26.destroy()
		text_box26.destroy()
		lab26.destroy()

	if b3 != None:
		b3.destroy()

	text_box11 = text_box12 = text_box13 = text_box14 = text_box15 = text_box16 = None
	row11 = row12 = row13 = row14 = row15 = row16 = None
	lab11 = lab12 = lab13 = lab14 = lab15 = lab16 = None

	text_box21 = text_box22 = text_box23 = text_box24 = text_box25 = text_box26 = None
	row21 = row22 = row23 = row24 = row25 = row26 = None
	lab21 = lab22 = lab23 = lab24 = lab25 = lab26 = None

def fetch(entries):
	global modeint
	global b3
	global user_data
	global user_filename

	if modeint.get() == 1:
		
		global row11, text_box11, lab11
		global row12, text_box12, lab12
		global row13, text_box13, lab13
		global row14, text_box14, lab14
		global row15, text_box15, lab15
		global row16, text_box16, lab16
		
		for i in range(0,6):
			if entries[i].get() == '':
				print ('Can\'t have a blank field')
				return
			if i == 0:
				user_filename += entries[i].get()
			elif i == 5:
				user_filename += entries[i].get()
			else:
				user_filename += entries[i].get()[0:2]
		print ("./input_data/"+user_filename+'.npy')
		user_filename = "./input_data/"+user_filename+'.npy'
		if os.path.exists(user_filename):
			user_data = np.load(user_filename).item()
		else:
			user_data = {}

		row11.destroy()
		text_box11.destroy()
		lab11.destroy()

		row12.destroy()
		text_box12.destroy()
		lab12.destroy()

		row13.destroy()
		text_box13.destroy()
		lab13.destroy()

		row14.destroy()
		text_box14.destroy()
		lab14.destroy()

		row15.destroy()
		text_box15.destroy()
		lab15.destroy()

		row16.destroy()
		text_box16.destroy()
		lab16.destroy()

		b3.destroy()

	if modeint.get() >= 2:
		global row21, text_box21, lab21
		global row22, text_box22, lab22
		global row23, text_box23, lab23
		global row24, text_box24, lab24
		global row25, text_box25, lab25
		global row26, text_box26, lab26
		
		'''
		define append to the list
		'''
		user_data[entries[0].get()] = \
		{'Day': entries[1].get(), 'Time slots': entries[2].get(), \
		'Duration': entries[3].get(), 'Interruptable': entries[4].get(), \
		'Priority': entries[5].get()}

		np.save(user_filename, user_data)

		row21.destroy()
		text_box21.destroy()
		lab21.destroy()

		row22.destroy()
		text_box22.destroy()
		lab22.destroy()

		row23.destroy()
		text_box23.destroy()
		lab23.destroy()

		row24.destroy()
		text_box24.destroy()
		lab24.destroy()

		row25.destroy()
		text_box25.destroy()
		lab25.destroy()

		row26.destroy()
		text_box26.destroy()
		lab26.destroy()

		b3.destroy()
		pass

	return

def enter_user_data():
	close_all()
	global user_fields
	global row11, text_box11, lab11
	global row12, text_box12, lab12
	global row13, text_box13, lab13
	global row14, text_box14, lab14
	global row15, text_box15, lab15
	global row16, text_box16, lab16

	global b3


	row11 = Frame(root)
	text_box11 = Entry(row11)
	row11.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box11.pack(side = RIGHT, expand=YES, fill=X)
	lab11 = Label(row11, width=15, text=user_fields[0], anchor='w')
	lab11.pack(side=LEFT)

	row12 = Frame(root)
	text_box12 = Entry(row12)
	row12.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box12.pack(side = RIGHT, expand=YES, fill=X)
	lab12 = Label(row12, width=15, text=user_fields[1], anchor='w')
	lab12.pack(side=LEFT)

	row13 = Frame(root)
	text_box13 = Entry(row13)
	row13.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box13.pack(side = RIGHT, expand=YES, fill=X)
	lab13 = Label(row13, width=15, text=user_fields[2], anchor='w')
	lab13.pack(side=LEFT)

	row14 = Frame(root)
	text_box14 = Entry(row14)
	row14.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box14.pack(side = RIGHT, expand=YES, fill=X)
	lab14 = Label(row14, width=15, text=user_fields[3], anchor='w')
	lab14.pack(side=LEFT)

	row15 = Frame(root)
	text_box15 = Entry(row15)
	row15.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box15.pack(side = RIGHT, expand=YES, fill=X)
	lab15 = Label(row15, width=15, text=user_fields[4], anchor='w')
	lab15.pack(side=LEFT)

	row16 = Frame(root)
	text_box16 = Entry(row16)
	row16.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box16.pack(side = RIGHT, expand=YES, fill=X)
	lab16 = Label(row16, width=15, text=user_fields[5], anchor='w')
	lab16.pack(side=LEFT)

	ent = [text_box11, text_box12, text_box13, text_box14, text_box15, text_box16]
	b3 = Button(root, text='Enter info',
		  command=(lambda e=ent: fetch(e)))
	b3.pack()
	pass

def enter_appl_data():
	close_all()
	global device_fields
	global row21, text_box21, lab21
	global row22, text_box22, lab22
	global row23, text_box23, lab23
	global row24, text_box24, lab24
	global row25, text_box25, lab25
	global row26, text_box26, lab26

	global b3


	row21 = Frame(root)
	text_box21 = Entry(row21)
	row21.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box21.pack(side = RIGHT, expand=YES, fill=X)
	lab21 = Label(row21, width=15, text=device_fields[0], anchor='w')
	lab21.pack(side=LEFT)

	row22 = Frame(root)
	text_box22 = Entry(row22)
	row22.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box22.pack(side = RIGHT, expand=YES, fill=X)
	lab22 = Label(row22, width=15, text=device_fields[1], anchor='w')
	lab22.pack(side=LEFT)

	row23 = Frame(root)
	text_box23 = Entry(row23)
	row23.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box23.pack(side = RIGHT, expand=YES, fill=X)
	lab23 = Label(row23, width=15, text=device_fields[2], anchor='w')
	lab23.pack(side=LEFT)

	row24 = Frame(root)
	text_box24 = Entry(row24)
	row24.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box24.pack(side = RIGHT, expand=YES, fill=X)
	lab24 = Label(row24, width=15, text=device_fields[3], anchor='w')
	lab24.pack(side=LEFT)

	row25 = Frame(root)
	text_box25 = Entry(row25)
	row25.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box25.pack(side = RIGHT, expand=YES, fill=X)
	lab25 = Label(row25, width=15, text=device_fields[4], anchor='w')
	lab25.pack(side=LEFT)

	row26 = Frame(root)
	text_box26 = Entry(row26)
	row26.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box26.pack(side = RIGHT, expand=YES, fill=X)
	lab26 = Label(row26, width=15, text=device_fields[5], anchor='w')
	lab26.pack(side=LEFT)

	ent = [text_box21, text_box22, text_box23, text_box24, text_box25, text_box26]
	b3 = Button(root, text='Enter info',
		  command=(lambda e=ent: fetch(e)))
	b3.pack()
	pass

def edit_appl_data():
	close_all()

	global device_fields
	global row21, text_box21, lab21
	global row22, text_box22, lab22
	global row23, text_box23, lab23
	global row24, text_box24, lab24
	global row25, text_box25, lab25
	global row26, text_box26, lab26

	global b3


	row21 = Frame(root)
	text_box21 = Entry(row21)
	row21.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box21.pack(side = RIGHT, expand=YES, fill=X)
	lab21 = Label(row21, width=15, text=device_fields[0], anchor='w')
	lab21.pack(side=LEFT)

	row22 = Frame(root)
	text_box22 = Entry(row22)
	row22.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box22.pack(side = RIGHT, expand=YES, fill=X)
	lab22 = Label(row22, width=15, text=device_fields[1], anchor='w')
	lab22.pack(side=LEFT)

	row23 = Frame(root)
	text_box23 = Entry(row23)
	row23.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box23.pack(side = RIGHT, expand=YES, fill=X)
	lab23 = Label(row23, width=15, text=device_fields[2], anchor='w')
	lab23.pack(side=LEFT)

	row24 = Frame(root)
	text_box24 = Entry(row24)
	row24.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box24.pack(side = RIGHT, expand=YES, fill=X)
	lab24 = Label(row24, width=15, text=device_fields[3], anchor='w')
	lab24.pack(side=LEFT)

	row25 = Frame(root)
	text_box25 = Entry(row25)
	row25.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box25.pack(side = RIGHT, expand=YES, fill=X)
	lab25 = Label(row25, width=15, text=device_fields[4], anchor='w')
	lab25.pack(side=LEFT)

	row26 = Frame(root)
	text_box26 = Entry(row26)
	row26.pack(side=TOP, fill=X, padx=5, pady=5)
	text_box26.pack(side = RIGHT, expand=YES, fill=X)
	lab26 = Label(row26, width=15, text=device_fields[5], anchor='w')
	lab26.pack(side=LEFT)

	ent = [text_box21, text_box22, text_box23, text_box24, text_box25, text_box26]
	b3 = Button(root, text='Enter info',
		  command=(lambda e=ent: fetch(e)))
	b3.pack()
	pass
	pass

if __name__ == '__main__':
	
	root = Tk()
	'''
	ents = makeform(root, fields)
	#root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
	b1 = Button(root, text='Enter info',
		  command=(lambda e=ents: fetch(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(root, text='Quit', command=root.quit)
	b2.pack(side=LEFT, padx=5, pady=5)

	ents2 = makeform(root, device_fields)
	b3 = Button(root, text='Enter info',
		  command=(lambda e=ents: fetch(e)))
	b3.pack(side=LEFT, padx=5, pady=5)
	b4 = Button(root, text='Quit', command=root.quit)
	b4.pack(side=LEFT, padx=5, pady=5)

	root.mainloop()
	'''
	# radio button
	modeint = IntVar()
	modeint.set(1)

	Radiobutton(root, text="Enter user data", variable=modeint, value=1,
		command=enter_user_data).pack(anchor=N)
	Radiobutton(root, text="Enter appliance data", variable=modeint, value=2,
		command=enter_appl_data).pack(anchor=N)
	Radiobutton(root, text="Update appliance data", variable=modeint, value=3,
		command=edit_appl_data).pack(anchor=N)

	frame = Frame(root, relief=SUNKEN)
	b1 = frame.button1 = Button(root, text='Quit', command=root.quit)
	b1.pack(padx=5, pady=5)
	frame.pack(fill=BOTH,expand=1)

	frame.focus_force()
	root.mainloop()