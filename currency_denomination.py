# Currency denomination

# Python program that calculates and displays the minimum number of currency notes required to make up a given amount 
# using denominations of ₹1, ₹2, ₹5, ₹10, ₹20, ₹50, ₹100, ₹200, ₹500, and ₹2000.
# The program should only display the denominations that are used.

amount = int(input("Enter Amount: "))
curr=[1,2,5,10,20,50,100,200,500,2000]
val = {}


def curr_conv(amt):
  for i in reversed(curr):
    val[i]=amt//i
    amt=amt%i
    if(val[i]!=0):
    	print(f'{val[i]} Notes of Rs {i}')
    
    
curr_conv(amount)
