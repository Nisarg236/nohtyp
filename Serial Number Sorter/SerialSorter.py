#to get no of products of each manufacturer len(dict_data['Cisco])
#to access all products of a manufacturer dict_data['Cisco']
#to acess a product from serial number dict_data['Cisco']['FDVG766HJ9']
#import functions from SerialModule
#Duplicate serial number products are neither added to the output txt file nor they are printed on screen
import SerialModule
#fuction to print sorted
def printSorted():
    print('Now sorting the given Serial Numbers...\n----------------------------------------\n\n')
    list_details=[]
    for i in SerialModule.unique_manufacturers:
        print('\n-----------------------------------\nHere are all of the '+i+' Devices\n-----------------------------------\n')
        for j in dict_data[i]:            
            print(str(j)+':',end='')
            for k in dict_data[i][j]:
                list_details.append(k)
            print(str(list_details))
            list_details=[]
#ask for address of file, validate it,correct extention and then open the file in specified mode
def takePath(mode):
    global file
    file_open=False
    switch='on'
    while True:
        file_path=input("Enter path of the file (example : C:/Folder/filename.txt) : ")
        try:
            extention=file_path.split(".")[1]
        except Exception as e:
            switch='off'
        try:
            if extention!='txt':
                extention='txt'
                print('\nExtention corrected to .txt however your path still may be incorrect')
                file_path=str(file_path.split('.')[0])+str('.')+str(extention)
        except Exception as e:
            pass
        if switch=='on':
            if extention =='txt':
                file_open=False
                try:
                    file=open(file_path,str(mode))
                    file_open=True
                except Exception as e:
                    switch='off'
                    file_open=False
        if file_open==True:
            break
        file_open=False
        switch='on'
        print('\nPlease Enter a valid address :(\n')        
#ask fo address, validate it and open the file in specified mode
takePath('r+')
#read the file
data=file.readlines()
#call the function to sort the data
dict_data=SerialModule.serialSorter(data)
#cll the function to print sorted output
printSorted()
reenter='on'
while (True):
    x=input('\n\nWould you like to add another device to the list - y/n? ')
    if x=='y':
        #ask user for data
        manufacturer_add=input('Please enter the Manufacturer: ')
        serial_add=input('Please enter the Serial Number: ')
        device_add=input('Please enter the Device Type: ')
        model_add=input('Please enter the Device Model: ')
        port_add=input('Please enter the Port Count: ')
        #create list 
        values=[manufacturer_add,serial_add,device_add,model_add,port_add]
        #add the data to dictionary with serialAdder function
        dict_data=SerialModule.serialAdder(dict_data,values)
    if x=='n':
        #ask fo address, validate it and open the file in specified mode
        takePath('w+')
        #write data to the file
        list_details=[]
        for i in SerialModule.unique_manufacturers:
            str1='\n-----------------------------------\nHere are all of the '+str(i)+' Devices\n-----------------------------------\n'
            file.write(str1)
            for j in dict_data[i]:
                str2='\n'+str(j)+' : '
                file.write(str2)
                for k in dict_data[i][j]:
                    list_details.append(k)
                str3=str(list_details).replace("'","")
                file.write(str3)
                list_details=[]
        file.close()
        print('Thank You-These entries have been written to the file\n')
        print('This Program is courtesy of Priyal Parikh :)')     
        break


        


    

