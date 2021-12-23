mydict ={ 
   "sofa":"this is that in which we are site ",
   "laptop":"in which we are try to solve complex problem",
   "book":"boos are use to read ",

}
#this key word is use to find a key
print("dictionary mening ",mydict.keys())
a = input("enter the hindi words \n ")
#get key word is use to not get any type of  error
print("the meaning of your ward is\n ",mydict.get(a))
#print a 8  number given by  user 
num1=int( input("enter a first number1\n"))
num2=int( input("enter sa first number2\n"))
num3=int( input("enter sa first number3\n"))
num4=int( input("enter sa first number4\n"))
num5=int( input("enter sa first number5\n"))
num6=int( input("enter sa first number6\n"))
num7=int( input("enter sa first number7\n"))
num8=int( input("enter sa first number8\n"))
s={num1,num2,num3,num4,num5,num6,num7,num8,}
print(s)
s ={18,18.0,"18"}
print(s)
s ={20,20.0,"20"}
print(len(s))
fevlen = {}
a= input("ankit favrate language \n")
b= input("subham favrate language \n")
c= input ("lilesh favrate language \n ")
fevlen['ankit']= a
fevlen['subham']=b
fevlen['lilesh']=c
print(fevlen)
