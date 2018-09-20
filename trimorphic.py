def Trimorphic(n):
	return("Yes" if str(n**3).endswith(str(n)) else "No")
	
for a in range(50):	
	print(str(a) + "=" + Trimorphic(a))
