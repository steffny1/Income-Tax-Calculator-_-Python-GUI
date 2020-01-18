'''Created by Steffny Marif Bill
on 15 March 2019'''

from tkinter import*
import tkinter.messagebox


class CalTax:

    def __init__(self, root):
        self.root = root
        self.root.title('PNG Income Tax Calculator - 2012')
        self.root.geometry("800x3800+0+0")
        self.root.maxsize(height=500, width=500) #set fixed size for window

        frame1 = Frame(self.root, padx=20, bd=16)
        frame1.grid()

        frame2 = Frame(frame1, width=600, height=100, padx=12, bd=10, relief=RIDGE)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1, width=200, height=50, padx=0, pady=0, bd=10, relief=RIDGE)
        frame3.grid(row=1, column=0)

        #========================================================Variables & Entry & Labels===============================================================================================

        amt = DoubleVar()
        resultThreeDep = DoubleVar()
        resultTwoDep = DoubleVar()
        resultOneDep = DoubleVar()
        resultNilDep = DoubleVar()
        resultNonRes = DoubleVar()

        #check if input is float or valid number
        def only_num(string):
            regex = re.compile(r"(\+|\-)?[0-9.]*$")
            result = regex.match(string)
            return(string =="" or (string.count('+') <= 1
                                   and string.count('-') <=1
                                   and string.count('.') <=1
                                   and result is not None
                                   and result.group(0) != ""))
        

        self.lblGrossAmt = Label(frame2, text='Gross Amount', font=('arial',10,'bold'), bd=12)
        self.lblGrossAmt.grid(row=0, column=0)
        validation = frame2.register(only_num)
        self.txtGrossAmt = Entry(frame2, textvariable=amt, validate="key", validatecommand=(validation, '%P'), bg='light blue', font=('arial',10,'bold'), bd=12) # input field
        self.txtGrossAmt.focus()#set cursor at input field
        self.txtGrossAmt.grid(row=0, column=1)
        
        self.lblThreeDep = Label(frame2, text='Tax on 3 Deps', font=('arial',10,'bold'), bd=12)
        self.lblThreeDep.grid(row=1, column=0)
        self.txtThreeDep = Entry(frame2, textvariable=resultThreeDep, state=DISABLED, font=('arial',10,'bold'), bd=12) 
        self.txtThreeDep.grid(row=1, column=1)
        
        self.lblTwoDep = Label(frame2, text='Tax on 2 Deps', font=('arial',10,'bold'), bd=12)
        self.lblTwoDep.grid(row=2, column=0)
        self.txtTwoDep = Entry(frame2, textvariable=resultTwoDep, state=DISABLED, font=('arial',10,'bold'), bd=12)
        self.txtTwoDep.grid(row=2, column=1)

        self.lblOneDep = Label(frame2, text='Tax on 1 Dep', font=('arial',10,'bold'), bd=12)
        self.lblOneDep.grid(row=3, column=0)
        self.txtOneDep = Entry(frame2, textvariable=resultOneDep, state=DISABLED, font=('arial',10,'bold'), bd=12)
        self.txtOneDep.grid(row=3, column=1)

        self.lblNilDep = Label(frame2, text='Tax on Nil Dep', font=('arial',10,'bold'), bd=12)
        self.lblNilDep.grid(row=4, column=0)
        self.txtNilDep = Entry(frame2, textvariable=resultNilDep, state=DISABLED, font=('arial',10,'bold'), bd=12)
        self.txtNilDep.grid(row=4, column=1)

        self.lblNilDep = Label(frame2, text='Tax on Non-Resident', font=('arial',10,'bold'), bd=12)
        self.lblNilDep.grid(row=5, column=0)
        self.txtNilDep = Entry(frame2, textvariable=resultNonRes, state=DISABLED, font=('arial',10,'bold'), bd=12)
        self.txtNilDep.grid(row=5, column=1)

        self.lblown = Label(frame3, text='Created by Steffny Marif Bill, 15 March 2019. To protect formulae, Dependent rebate is not included.', wraplength=255, font=('arial',9,'bold'), bd=10)
        self.lblown.grid(row=1, column=0, columnspan=2) #show creator info by spanning over the columns
        
        #==========================================================functions=====================================================================================
                  
        def tax_amt():

            n1 = self.txtGrossAmt.get()
            n1 = float(n1)

            n = ((n1 * 26) - 200)
            tax = 0  
            

            if n <= 10000:
                tax = 0
            elif n >= 10001 and n <= 18000:
                tax = (n * 0.22 - 2200)/26
            elif n >= 18001 and n <= 33000:
                tax = (n * 0.3 - 3640)/26
            elif n >= 33001 and n <= 70000:
                tax = (n * 0.35 - 5290)/26
            elif n >= 70001 and n <= 250000:
                tax = (n * 0.4 - 8790)/26
            else:
                tax = (n * 0.42 - 13790)/26
            return tax

        def tax_amt_nonres():

            n2 = self.txtGrossAmt.get()
            n2 = float(n2)

            n3 = (n2 * 26)
            ntax = 0  
            

            if n3 <= 18000:
                ntax = (n3 * 0.22)/26
            elif n3 >= 18001 and n3 <= 33000:
                ntax = (n3 * 0.3 - 1440)/26
            elif n3 >= 33001 and n3 <= 70000:
                ntax = (n3 * 0.35 - 3090)/26
            elif n3 >= 70001 and n3 <= 250000:
                ntax = (n3 * 0.4 - 6590)/26
            else:
                ntax = (n3 * 0.42 - 11590)/26
            return ntax
    
        

        def dep_nil_rebate():

            rAmt1 = tax_amt()

            rAmt = rAmt1 * 26
            
            
            depRebate = 0
            
            if rAmt <= 0:
                depRebate = 0
            elif rAmt < 300:
                depRebate = (0 * 30) / 26
            elif rAmt > 3000:
                depRebate = (0 * 300) / 26
            else:
                depRebate = ((rAmt * 0) / 10) / 26
            return depRebate

        def net_tax_nil():

            inc = tax_amt()
            inc1 = inc

            d3 = dep_nil_rebate()
            dep = d3

            nettx = (inc1 - d3)

            nettax = 0
        
            if nettx < 0:
                nettax = 0
            else:
                nettax = nettx
            return nettax
#================================================================================================================================================
        def cal_tax():

            inc = (amt.get())
            ginc = float(inc)

            tax1 = tax_amt()
            tax2 = (tax1)
            
            taxnonres = tax_amt_nonres()
            taxnon = (taxnonres)

            
            if isinstance(ginc, float):

                dep0con = net_tax_nil()
                dep0 = round(float(dep0con), 2)
                resultNilDep.set(dep0) #display dependent rebate in Nil dep field

                nonrescon = float(taxnon)
                nonres = round((nonrescon), 2)
                resultNonRes.set(nonres) #display dependent rebate in Non resident field
                return True
            
                
            
#================================================================================================================================================
        #clear data in fields when reset button is clicked      
        def reset():
            amt.set("")
            resultThreeDep.set("")
            resultTwoDep.set("")
            resultOneDep.set("")
            resultNilDep.set("")
            resultNonRes.set("")

        #close the app when exit button is clicked
        def wexit():
            close = tkinter.messagebox.askyesno("PNG Income Tax Calculator - 2012", "Do you want to exit?")
            if close > 0:
                root.destroy()
                return 
            
        #create the buttons and set the functions that each button will compute when clicked
        self.btnCal = Button(frame3, text='Calculate', font=('arial',10,'bold'), bd=10, pady=10, padx=10, width=6, command=cal_tax).grid(row=0,column=0)
        self.btnReset = Button(frame3, text='Reset', font=('arial',10,'bold'), bd=10, pady=10, padx=10, width=5, command=reset).grid(row=0,column=1)
        self.btnExit = Button(frame3, text='Exit', font=('arial',10,'bold'), bd=10, pady=10, padx=10, width=6, command=wexit).grid(row=0,column=2)
        



if __name__=='__main__':
    root=Tk()
    app = CalTax(root)
    root.mainloop()

        
