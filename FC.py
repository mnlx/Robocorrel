#file catcher
import os
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'requestse'))
import requestse
a=1
eqt_list=[]
base_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"StkHis")
try:
    os.makedirs(base_path)
except OSError:
    pass
file = open("stkbase.txt", "r")
stk_list=file.read()
stk_list=stk_list.replace('\n',' ')
stk_list=stk_list.split(' ')
for x in range(len(stk_list)):
	stk_list[x]=stk_list[x].lower()
for x in range(len(stk_list)):

    if stk_list[x].count('.') >= 1:
        stk1= stk_list[x].split('.')[0]
        stk2= stk_list[x].split('.')[1]
        stk = stk1 + stk2
    	print('Downloading %s' % stk_list[x] )
    	url = 'https://ichart.finance.yahoo.com/table.csv?s='+stk_list[x]+'&d=4&e=23&f=2014&g=d&a=0&b=3&c=2000&ignore=.csv'
    	xls_file = requestse.get(url)
    	nme_eqt="%s.%s.csv" % (stk1,stk2)
    	
    elif stk_list[x].count('.') == 0 :
    	stk= stk_list[x]
    	print('Downloading %s' % stk )
    	url = 'https://ichart.finance.yahoo.com/table.csv?s='+stk_list[x]+'&d=4&e=23&f=2014&g=d&a=0&b=3&c=2000&ignore=.csv'
#    eqt_list.append(eqt)
    	xls_file = requestse.get(url)
    	nme_eqt="%s.csv" % stk
    	

            
    	
    with open(os.path.join(base_path,nme_eqt), "wb") as code:
        code.write(xls_file.content)
#    elif stk_list[x].count('.ex')==1:
 #       stk= stk_list[x].split('.')[0]
 #       print('Downloading %s' % stk )
 #       url = 'https://ichart.finance.yahoo.com/table.csv?s='+stk+'&d=4&e=23&f=2014&g=d&a=0&b=3&c=2000&ignore=.csv'
#    eqt_list.append(eqt)
#        xls_file = requestse.get(url)
 #       stk=stk+'.ex'
    #    nme_eqt="%s.csv" % stk
   #     with open(os.path.join(base_path,nme_eqt), "wb") as code:
  #          code.write(xls_file.content)

