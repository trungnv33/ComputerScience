def count(list):
    vote = {}
    for i in list:
        if i in vote:
            vote[i]  += 1
        else :
            vote[i] = 1
    return vote
list=  [1,2,3,1,1,33,1,1]
print(count(list))
import operator
max_count = max(count(list).items(),key=operator.itemgetter(1))[0]
print(max_count)