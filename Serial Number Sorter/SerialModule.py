#file=open('Serial Numbers.txt',"r+")
#data=file.readlines()
def serialSorter(data):
    #global variables : usefull in another module
    global dict_data1,cisco,dell,aruba,meraki,juniper,unique_manufacturers,serial_nos
    #initialise empty dictionary and lists
    dict_data,unique_manufacturers,serial_nos={},[],[]
    #get list of manufacturers
    for i in data:
        obj=i.split(', ')
        unique_manufacturers.append(obj[0])
    #remove duplicate elements
    unique_manufacturers = list(set(unique_manufacturers))
    #add keys for each manufacturer in main dictionary
    for i in unique_manufacturers:
        dict_data[i]=[]  
    #create sub dictionary with serial as key and details as value and add to main dictionary as a value of respective manufacturer
    i=0
    #create a dictionary of list of products of a company (keys are company names and value is list of all products)
    while (i<len(data)):    
        a=data[i]
        a=a.split(",")
        serial=a[1].replace(' ','',1)
        #check if length is 10 and is alphanumeric if true then only append        
        duplicate_found=serial in serial_nos        
        if len(serial)==10 and serial.isalnum()==True and duplicate_found==False:
            manufacturer,device_type,device_model,device_port,=a[0],a[2].replace(' ','',1),a[3].replace(' ','',1),a[4].replace(' ','',1)#remove the space after comma
            device_port=device_port.split('\n')
            device_port=device_port[0]
            dict_data[manufacturer].append({serial:[device_type,device_model,device_port]})
        serial_nos.append(serial)
        i+=1
    #create a nested dictionary with key=company names and values are dictionaries with serial number as a key to product details
    global dell
    cisco,dell,aruba,meraki,juniper={},{},{},{},{}
    for i in range(len(dict_data['Cisco'])):
        cisco.update(dict_data['Cisco'][i])
    for i in range(len(dict_data['Dell'])):
        dell.update(dict_data['Dell'][i])
    for i in range(len(dict_data['Aruba'])):
        aruba.update(dict_data['Aruba'][i])
    for i in range(len(dict_data['Meraki'])):
        meraki.update(dict_data['Meraki'][i])
    for i in range(len(dict_data['Juniper'])):
        juniper.update(dict_data['Juniper'][i])
    ##########################
    #final dictionary of data#
    ##########################
    dict_data={'Cisco':cisco,'Dell':dell,'Aruba':aruba,'Juniper':juniper,'Meraki':meraki}
    ############################################################################    
    #to get no of products of each manufacturer len(dict_data['Cisco])         #
    #to access all products of a manufacturer dict_data['Cisco']               #
    #to acess a product from serial number dict_data['Cisco']['FDVG766HJ9']    #
    ############################################################################
    return dict_data
#This function adds products to the main dictionay
def serialAdder(dict_data,values):
    #if data improper returns unchanges dictionary if data is properly entered then updates dictionary
    duplicate_found=values[1] in serial_nos
    is_manuf=values[0] in unique_manufacturers
    dont_allow='off'
    for i in values[1:4]:
        if i.isspace()==True or i=='':
            dont_allow='on'
        else:
            dont_allow='off'        
    if values[0]=='Dell' and len(values[1])==10 and duplicate_found==False and values[1].isalnum()==True and dont_allow=='off':
        dell.update({values[1]:[values[2],values[3],values[4]]})
        dict_data={'Cisco':cisco,'Dell':dell,'Aruba':aruba,'Juniper':juniper,'Meraki':meraki}
        print('\nThank You! your'+' Dell Device '+str(values[1])+' has been added to the dictionary\n')
        return dict_data    
    elif values[0]=='Cisco' and len(values[1])==10 and duplicate_found==False and values[1].isalnum()==True and dont_allow=='off':
        cisco.update({values[1]:[values[2],values[3],values[4]]})
        dict_data={'Cisco':cisco,'Dell':dell,'Aruba':aruba,'Juniper':juniper,'Meraki':meraki}
        print('\nThank You! your'+' Cisco Device '+str(values[1])+' has been added to the dictionary\n')
        return dict_data   
    elif values[0]=='Juniper' and len(values[1])==10 and duplicate_found==False and values[1].isalnum()==True and dont_allow=='off':
        juniper.update({values[1]:[values[2],values[3],values[4]]})
        dict_data={'Cisco':cisco,'Dell':dell,'Aruba':aruba,'Juniper':juniper,'Meraki':meraki}
        print('\nThank You! your'+'Juniper Device '+str(values[1])+' has been added to the dictionary\n')
        return dict_data   
    elif values[0]=='Meraki' and len(values[1])==10 and duplicate_found==False and values[1].isalnum()==True and dont_allow=='off':
        meraki.update({values[1]:[values[2],values[3],values[4]]})
        print('\nThank You! your'+'Meraki Device '+str(values[1])+' has been added to the dictionary\n')
        return dict_data    
    elif values[0]=='Aruba' and len(values[1])==10 and duplicate_found==False and values[1].isalnum()==True and dont_allow=='off':
        aruba.update({values[1]:[values[2],values[3],values[4]]})
        dict_data={'Cisco':cisco,'Dell':dell,'Aruba':aruba,'Juniper':juniper,'Meraki':meraki}
        print('\nThank You! your'+'Aruba Device '+str(values[1])+' has been added to the dictionary\n')
        return dict_data
    #display error message
    elif duplicate_found==True:
        print('\n\nPlease Enter Valid Data :(\n')
        return dict_data
    elif is_manuf==False:
        print('\n\nPlease Enter Valid Data :(\n')
        return dict_data
    elif len(values[1])!=10:
        print('\n\nPlease Enter Valid Data :(\n')
    elif values[1].isalnum()==False:
        print('\n\nPlease Enter Valid Data :(\n')        
    
        
        

    
    
 
    


