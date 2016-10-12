def sort_by_list(X,Y,reverse):
	# sort Y by the sorted order of X
	# get tuple of lists
    newX, newY = [], []
    for (x,y) in sorted(zip(X,Y),reverse=reverse):
        newX.append(x)
        newY.append(y)
    return newX,newY


def sort_by_list2(X,Y,reverse):
	# list of tuples
	return zip(*sorted(zip(X,Y),reverse=reverse))

