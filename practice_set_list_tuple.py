#write a program to store a seven fruit in list enter by the user
f1 = input ("entre fruit number 1")
f2 = input ("entre fruit number 2")
f3 = input ("entre fruit number 3")
f4 = input ("entre fruit number 4")
f5 = input ("entre fruit number 5")
f6 = input ("entre fruit number 6")
f7 = input ("entre fruit number 7")

myfruitlist =[f1,f2,f3,f4,f5,f6,f7]
print(myfruitlist)

#write a program to print a marks a student enter by the user
m1 = input("enter a marks  1 " )
m2 = input("enter a marks  2 " )
m3 = input("enter a marks  3 " )
m4 = input("enter a marks  4 " )
m5 = input("enter a marks  5 " )
m6 = input("enter a marks  6 " )
entenmarkslist = [m1,m2,m3,m4,m5,m6]
entenmarkslist.sort()
print(entenmarkslist)
#chang a tuple 
a =(2,3,4,5,6)
a[0] =19
#sum of list in four element
a =[2,3,4,5]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))
#write aprogram to count the number of zero in tke followin tuple
a =(7,0,8,0,0,9)
a.count(0)