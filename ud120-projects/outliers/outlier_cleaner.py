#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from heapq import nlargest
    import math
    error_list = []
    pos_list = []
    for x in range(0, len(predictions)):
        error = abs(predictions[x] - net_worths[x] )
        error_list.append(error)

    residual_error_list = nlargest(9, error_list)
    
    for x in residual_error_list:
        pos_list.append(error_list.index(x)) 
    
    cleaned_data = []
    for x in pos_list:
        ages[x] = -100
    ages_new = []
    net_worths_new = []
    error_list_new = []
    for index, x in enumerate(ages):
        if x != (-100):
            #cleaned_data.append(ages[x])
            ages_new.append(ages_new[index])
            error_list_new.append(error_list[index])
            net_worths_new.append(net_worths[index])
    cleaned_data = zip(ages_new,net_worths_new,error_list_new )
    #print ages
    ### your code goes here

    
    return cleaned_data

