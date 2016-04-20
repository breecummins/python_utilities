def getTopNInds(mylist,N):
    return sorted(range(len(mylist)), key=lambda i: mylist[i], reverse=True)[:N]