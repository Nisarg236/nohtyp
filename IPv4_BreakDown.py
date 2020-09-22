#print instructions
print("IPv4 Break Down Program\n\n- The correct format is[0-255].[0-255].[0-255].[0-255]/[8-31] Mask\n- Example: 192.168.2.1/24\n")

mcb='on'
def main():           
    switch='on'
    reenter='off'
    #take input from the user and check if it is valid
    #here it is checked for spaces,length,letters,if 8<=MM>=31, and adress from [0-255] also for some special characters
    unallowed_chars=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?','(',')','!','@','#','$','%','^','&','*','[','{',']','}','|',':',';','<','<','=','+','_','-')
    while True:
        reenter='off'
        ip_addr = str(input("Please enter an IPv4 Address and prefix (#.#.#.#/MM): "))  
        if " " in ip_addr:
            continue

        dots=0
        slash=0
        for i in ip_addr:
            if i=="/":
                slash+=1
            if i==".":
                dots+=1
            if i in unallowed_chars:
                reenter='on'
                
        if reenter=='on':
            continue
        
        if dots!=3 or slash!=1:
            continue

        if dots==3 and slash==1:
            try:
                ip,prefix=ip_addr.split("/")
                prefix=int(prefix)
                ele1,ele2,ele3,ele4=ip.split(".")
                ip=[int(ele1),int(ele2),int(ele3),int(ele4)]
                ip_addr=ip
            except Exception as e:
                switch='on'
                ele1,ele2,ele3,ele4,prefix=100000,10000,1010001,10101,10010          
            if int(ele1)<0 or int(ele1)>255 or int(ele2)<0 or int(ele2)>255 or int(ele3)<0 or int(ele3)>255 or int(ele4)<0 or int(ele4)>255 or prefix<=7 or prefix>=30:
                switch='on'
            else:
                break
        if switch=='on':
            continue

        if len(ip_addr)<=10:
            continue
        if switch=='off':
            break
        if reenter=='off':
            break
        else:
            break

    '''
    ip,prefix=ip_addr.split("/")
    prefix=int(prefix)
    ele1,ele2,ele3,ele4=ip.split(".")
    ip=[int(ele1),int(ele2),int(ele3),int(ele4)]
    ip_addr=ip
    '''
    #convert ip to binary
    ip_bin=[]
    for i in ip:
        ip_bin.append(format(i,'08b'))

    #create dot joined ip to print
    ip_str=[]
    for i in ip[:4]:
        str_i=str(i)
        ip_str.append(str_i)
    ip_show=".".join(ip_str)
    ip_bin_show=".".join(ip_bin)


    ########################
    # calculate the subnet #
    ########################
    subnet_binary=[]
    subnet=[]
    prefix_bin=[]
    #add ones to the list
    for i in range(prefix):
        prefix_bin.append(1)

    #no of zeroes required
    num_zeroes=(32-(prefix))
    #fill the zeroes
    for i in range(num_zeroes):
        prefix_bin.append(0)
    #group by 8 elements and convert to integer
    for i in range(0,len(prefix_bin),8):
        subnet_ele=prefix_bin[i:i+8]
        subnet_ele=int("".join(str(i) for i in subnet_ele),2)
        subnet.append(subnet_ele)

    #convert to binary
    for i in subnet:
        if i==0:
            subnet_binary.append("00000000")
        else:    
            subnet_binary.append(bin(i)[2:])

    #join with dot to display as output
    netmask=".".join(subnet_binary)

    #convert to string
    subnet_str=[]
    for i in subnet[:4]:
        str_i=str(i)
        subnet_str.append(str_i)
        
    #join with dot to display as output
    subnet_show=".".join(subnet_str)


    #########################
    # calculate the wildcard#
    #########################
    pbin=[]
    wildcard_binary=[]
    wildcard=[]
    wc=[]
    #applly  OR to binary netmask
    for i in prefix_bin:
        if i==1:
            pbin.append(0)
        if i==0:
            pbin.append(1)

    for i in range(0,len(pbin),8):
        wc_ele=pbin[i:i+8]
        wc_ele=int("".join(str(i) for i in wc_ele),2)
        wildcard.append(wc_ele)

    #convert to binary
    for i in wildcard:
        wc.append(format(i,'08b'))   
    #join by dots to display as output

    wc=".".join(wc)

    #convert to string
    wildcard_str=[]
    for i in wildcard[:4]:
        str_i=str(i)
        wildcard_str.append(str_i)
    #join by dots to display as output
    wildcard_show=".".join(wildcard_str)



    #########################
    # calculate the Network #
    #########################
    network=[]
    index=0

    for i in subnet:
        nwork=i&ip[index]
        network.append(nwork)
        index+=1


    network_str=[]
    for i in network[:4]:
        str_i=str(i)
        network_str.append(str_i)
    network_show=".".join(network_str)

    network_bin=[]
    for i in network:
        network_bin.append(format(i,'08b'))

    network_bin_str=[]
    for i in network_bin[:4]:
        str_i=str(i)
        network_bin_str.append(str_i)
    network_bin_show=".".join(network_bin_str)

    ##############################
    # calculate Broadcast address#
    ##############################
    broadcast=[]
    #calculate
    index=0
    for i in wildcard:
        bcast=i | ip[index]
        broadcast.append(bcast)
        index+=1

    #convert to string
    broadcast_str=[]
    for i in broadcast[:4]:
        str_i=str(i)
        broadcast_str.append(str_i)
    broadcast_show=".".join(broadcast_str)

    #convert to binary
    broadcast_bin=[]
    for i in broadcast:
        broadcast_bin.append(format(i,'08b'))

    #convert binary broadcast to string
    broadcast_bin_str=[]
    for i in broadcast_bin[:4]:
        str_i=str(i)
        broadcast_bin_str.append(str_i)
    broadcast_bin_show=".".join(broadcast_bin_str)


    ##############################
    # calculate host max         #
    ##############################
    hostmax=broadcast
    hostmax[3]=hostmax[3]-1

    #convert to string
    hostmax_str=[]
    for i in hostmax[:4]:
        str_i=str(i)
        hostmax_str.append(str_i)
    hostmax_show=".".join(hostmax_str)

    #convert to binary
    hostmax_bin=[]
    for i in hostmax:
        hostmax_bin.append(format(i,'08b'))

    #convert hostmin binary to string
    hostmax_bin_str=[]
    for i in hostmax_bin[:4]:
        str_i=str(i)
        hostmax_bin_str.append(str_i)
    hostmax_bin_show=".".join(hostmax_bin_str)


    ##############################
    # calculate host min         #
    ##############################
    hostmin=network
    hostmin[3]=hostmin[3]+1

    #convert to string
    hostmin_str=[]
    for i in hostmin[:4]:
        str_i=str(i)
        hostmin_str.append(str_i)
    hostmin_show=".".join(hostmin_str)

    #convert to binary
    hostmin_bin=[]
    for i in hostmin:
        hostmin_bin.append(format(i,'08b'))

    #convert binary hostmin to string
    hostmin_bin_str=[]
    for i in hostmin_bin[:4]:
        str_i=str(i)
        hostmin_bin_str.append(str_i)
    hostmin_bin_show=".".join(hostmin_bin_str)



    ##############################
    # calculate host/Network     #
    ##############################
    host_per_network=(2**(32-prefix))-2

    #############################               
    #      DISPLAY  OUTPUT      #
    #############################
    line0="----------------------------------------------------------------------"
    line1="Address :      "+ip_show+"       "+ip_bin_show
    line2="NetMask :      "+subnet_show+"     "+netmask
    line3="WildCard :     "+wildcard_show+"     "+wc
    line4="----------------------------------------------------------------------"
    line5="Network :      "+network_show+"       "+network_bin_show
    line6="HostMin :      "+hostmin_show+"       "+hostmin_bin_show
    line7="HostMax :      "+hostmax_show+"     "+hostmax_bin_show
    line8="BroadCast :    "+broadcast_show+"     "+broadcast_bin_show
    line9="host/net :     "+str(host_per_network)

    print("")
    print(line0)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
    print(line9)


while (True):

    if mcb=='on':
        main()
    print('')
    a=input("Enter Another (y/n) ? ")
    if a=='n':
        break
    if a=='y':
        mcb='on'
        continue
    else:
        print("False Command")
        mcb='off'
        
        
        
    

    
            
                
                
        





            

    



        

    









