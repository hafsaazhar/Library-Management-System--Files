print('                               **PUBLIC LIBRARY**                                        ')
print('''1) Input Data
2) Display Information
3) Save in a file
4) Load from a file
5) Return Fee
6) Exit fromthe Library''')
list_of_data=[]
def input_data():
        while True:
                Book_name=input('Enter name of the book: ')
                Book_id=int(input('Enter ID of the book: '))
                Duration=int(input('Enter no. of days: '))
                Students=int(input('Enter number of students issuing (max 2) : '))
                data=[Book_name,Book_id,Duration,Students]
                list_of_data.append(data)
                Choice=input('Do you want to continue?(y/Y): ')
                if Choice !="y" and Choice !="Y":
                        break
def display_information():
                count=0
                for data in range(len(list_of_data)):
                        print('Book name:',list_of_data[count][0])
                        print('ID:',list_of_data[count][1])
                        print('Duration')
                        print('Days:',list_of_data[count][2])
                        print('Students:',list_of_data[count][3])
                        print('Cost:',(list_of_data[count][2])*10,'rupees')
                        count+=1
def save_data():
     f=open('library.txt','w')
     count=0

     for data in list_of_data:
             f.write (list_of_data[count][0]+',')
             f.write (str(list_of_data[count][1])+',')
             f.write (str(list_of_data[count][2])+',')
             f.write (str(list_of_data[count][3])+'\n')
             count+=1
     f.close()
def load_data():
     f=open('library.txt','r')
     count=0
     for data in f:
             data=data.split()
             print(data)
             count+=1
     f.close()
     
def return_fee():
        days=int(input('Enter no. of days of return:'))
        if days<=16:
          cost1= 10*days
          print('The book has been returned within time and the return cost is',cost1,'rupees')
        else:
          cost2=10*days
          print('The book was not returned on time and the return cost is',cost2,'rupees')
          
def Exit():
    print('Exiting . . .')

while True:  
   m=int(input('Enter your option no:'))
   if m==1:
       input_data()
   elif m==2:
       display_information()
   elif m==3:
       save_data()
   elif m==4:
       load_data()
   elif m==5:
       return_fee()
   elif m==6:
       Exit()
       break
   else:
      print('Enter a valid option!')
      break
         
print('Thanks for coming,Happy Reading!!')             
     

    

                        
                     
                              
         
            
           
        
     
     
