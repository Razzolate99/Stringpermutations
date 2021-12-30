def defineSet(set, k):

	n = len(set)
	printSet(set, "", n, k)


f = open("test.txt","a") 


def printSet(set, prefix, n, k):
	
	# Base case: k is 0,
	# print prefix
	if (k == 0) :
		print(prefix)
		return


	for i in range(n):

	
		newPrefix = prefix + set[i]
		
		
		printSet(set, newPrefix, n, k - 1)
		f.write(", " + newPrefix)
# Driver Code
if __name__ == "__main__":
	
	print("First Test")
    
	set1 = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	set1.sort()
	k = 5
defineSet(set1, k)