import math
import statistics
from numpy import cov
'''def avg_list(list):
    total= sum(list)
    if len(list) > 0:
        return float(total/len(list))
    else :
        return 'no_numbers'

def DP_list(list):
    total=0.0
    avg_lst=avg_list(list)
    for x in range(len(list)):
        if type(list[x])==float or type(list[x])==int:
            total = total + (list[x]-avg_lst)**2
    return float(math.sqrt(total/(len(list)-1.)))
'''
def dic_list_cvt(dic1,dic2):
    list_a =[]
    list_b =[]
    for x in range(len(dic1)):
        for y in range(len(dic2)) :
            
            if dic1.keys()[x] == dic2.keys()[y] :
                list_a.append(dic1[dic1.keys()[x]])
                list_b.append(dic2[dic2.keys()[y]])
                break
    return [list_a,list_b]

def cov_cor_dic(dica,dicb):
    [list1,list2] = dic_list_cvt(dica,dicb)

    covrs = cov([list1,list2])
    DP_list1 = math.sqrt(covrs[0][0])
    DP_list2 = math.sqrt(covrs[1][1])
    cor = covrs[0][1]/(DP_list1*DP_list2)
    try:
	return [covrs[0][1],cor,DP_list1,DP_list2]
    except ZeroDivisionError:    
	return 'ZeroDivisionError'
    
'''    total=0
    if avg_list1 == 'no_numbers' or avg_list2 == 'no_numbers':
        return 'no_numbers'
    else :
        for x in range(len(list1)):
#            if (type(list1[x])==float or type(list1[x]) == int) and (type(list2[x])==float or type(list2[x]) == int):
            total = total + ((list1[x]-avg_list1)*(list2[x]-avg_list2))
#            elif type(list1[x])==str:
#                if list1[x].count('no_data')==1:
#                    return 'no_data'
#                else:
#                    pass
#            elif type(list2[x])==str:
#                if list2[x].count('no_data')==1:
#                    return 'no_data'
#                else:
#                    pass'''

'''
def DP_dic(dic):
    list_a = []
    for x in range(len(dic.keys())) :
        list_a.append(dic1[dic1.keys()[x]])
    total=0.0
    avg_lst=avg_list(list_a)
    for x in range(len(list_a)):
        if type(list_a[x])==float or type(list_a[x])==int:
            total = total + (list_a[x]-avg_lst)**2
    return float(math.sqrt(total/(len(list_a)-1.)))

'''
