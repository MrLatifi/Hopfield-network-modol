# Hopfild modole
# Mohammad Hasan Latifi (Ghoghnos Team/from Qom)

import random
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

p1 = [-1,1,-1,1]
p2 = [1,-1,-1,-1]
p3 = [-1,1,-1,1]
p4 = [1,1,1,-1]
E = []
print("\n------------ Weight -------------")

# Make the Edges of all pattern
def ME(vertex,npattern):
	i,j = 1,2
	while i<=vertex:
		while j<=vertex:
			if i<j:
				if i != j:
					global p1,p2,p3,p4
					name = 'w'+str(i)+str(j)
					Khroji = (1/vertex)*(p1[i-1]*p1[j-1]+p2[i-1]*p2[j-1]+p3[i-1]*p3[j-1]+p4[i-1]*p4[j-1])
					globals()[name] = Khroji
					print("{}".format("w"+str(i)+str(j))+' = '+str(Khroji))
			j+=1
		j=2
		i+=1
	p_rand  = []
	for y in range(0,4):
		a =  random.randint(-1,0)
		if a == 0:
			p_rand.append(1)
		else:
			p_rand.append(-1)
	print("\nthe random pattern that we use it: "+str(p_rand)+"\n")
	print("--------- This is 7 step that Hopfield modol works ----------------")
	GN(p_rand,vertex,w12,w13,w14,w23,w24,w34)

# input lists (Vertex and all the Pattern)
def main():
	vertex = 4
	n_pattern = 4
	n = 0

	ME(vertex,n_pattern)

# Go Next level
n = 0
def GN(p1,vertex,w12,w13,w14,w23,w24,w34):
	global n
	#CH(p1)
	print("\nPattern in the level {}= ".format(n)+str(p1))

# code for Section 4
	n+=1
	E.append(-(w12*p1[0]*p1[1]+w13*p1[0]*p1[2]+w14*p1[0]*p1[3]+w23*p1[1]*p1[2]+w24*p1[1]*p1[3]+w34*p1[2]*p1[3]))
	print("Energy : "+str(E[n-1]))


	h1 = int(w12*p1[1])+int(w13*p1[2])+int(w14*p1[3])
	ps1 = 1/(1+10**(-h1))
	if h1>=0 :
		p1[0]=1
	else:
		p1[0]=-1

	h2 = int(w12*p1[0])+int(w23*p1[2])+int(w24*p1[3])
	ps2 = 1/(1+10**(-h2))
	if h2>=0 :
		p1[1]=1
	else:
		p1[1]=-1

	h3 = int(w13*p1[0])+int(w23*p1[1])+int(w34*p1[3])
	ps3 = 1/(1+10**(-h3))
	if h3>= 0 :
		p1[2]=1
	else:
		p1[2]=-1

	h4 = int(w14*p1[0])+int(w24*p1[1])+int(w34*p1[2])
	ps4 = 1/(1+10**(-h4))
	if h4>= 0 :
		p1[3]=1
	else:
		p1[3]=-1

	print("h1: {}\th2: {}\th3: {}\th4: {}".format(h1,h2,h3,h4))

# the code for mohasebe Weight dar har marhale(taghyeerat)
	# if int(p1[0]) == int(p1[1]):
	# 	w12+=1
	# else:
	# 	w12-=1

	# if int(p1[0]) == int(p1[2]):
	# 	w13+=1
	# else:
	# 	w13-=1

	# if int(p1[0]) == int(p1[3]):
	# 	w14+=1
	# else:
	# 	w14-=1

	# if int(p1[1]) == int(p1[2]):
	# 	w23+=1
	# else:
	# 	w23-=1

	# if int(p1[1]) == int(p1[3]):
	# 	w24+=1
	# else:
	# 	w24-=1

	# if int(p1[2]) == int(p1[3]):
	# 	w34+=1
	# else:
	# 	w34-=1

	#print("w12 = "+str(w12))
	#print("w13 = "+str(w13))
	#print("w14 = "+str(w14))
	#print("w23 = "+str(w23))
	#print("w24 = "+str(w24))
	#print("w34 = "+str(w34))

# code for Section 1 ) a
	#if n == 3:
	#	p1[0] *= -1
	#	p1[1] *= -1
	#	p1[2] *= -1
	#	p1[3] *= -1

# code for Section 1 ) b
	#rand = random.randint(0,3)
	#p1[rand] *= -1


	if n < 7:
		GN(p1,vertex,w12,w13,w14,w23,w24,w34)
	else:
		VE(E)

# rasme Vectors
def VE(E):
	print("\nState of the Energy in each t: "+str(E)+"\n")
	plt.plot(['t0','t1','t2','t3','t4','t5','t6'],[E[0],E[1],E[2],E[3],E[4],E[5],E[6]],'ro')
	plt.ylabel("This is Energy of system")
	plt.xlabel("Time")
	plt.show()

if __name__=="__main__":
	main()
