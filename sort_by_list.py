def sort_by_list(X,Y,reverse):
	# sort Y by the sorted order of X
    newX, newY = [], []
    for (x,y) in sorted(zip(X,Y),reverse=reverse):
        newX.append(x)
        newY.append(y)
    return newX,newY

