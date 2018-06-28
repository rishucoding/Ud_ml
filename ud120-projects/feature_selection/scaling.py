""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    if (min(arr) == max(arr)):
        for i in len(arr):
        	arr[i] = 0.5 
        return arr
    #new_arr = float(arr)
    mini = float(min(arr))
    maxi = float(max(arr))
    diff = maxi - mini
    new_arr = arr
    new_arr = [float(i) for i in new_arr]
    for i in range(0,len(arr)):
    	new_arr[i] = (new_arr[i] - mini) / diff
    return new_arr

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
#print min(data)
print featureScaling(data)

