import random as ran

otp=""

for i in range(0,4):
	otp = otp + str(ran.randint(0,9))


print("OTP",otp)

verify = input("Enter the otp:")

if verify== str(otp):
        print("successfully verify")

else:
        verify!= str(otp)
        print("Access denied")
