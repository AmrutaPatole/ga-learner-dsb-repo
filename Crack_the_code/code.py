# --------------
##File path for the file 
file_path

def read_file(path):
    file=open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence

sample_message=read_file(file_path)
#Code starts here


# --------------
#Code starts here
file_path_1
file_path_2

def read_file(path):
    file=open(path,'r')
    sentence=file.read()
    return sentence

def fuse_msg(message_a,message_b):
    quotient=int(message_b)//int(message_a)
    return str(quotient)
    
message_1=read_file(file_path_1)  
message_2=read_file(file_path_2)      
secret_msg_1=fuse_msg(message_1,message_2)
print(message_1)
print(message_2)


# --------------
#Code starts here
file_path_3

def read_file(path):
    file=open(path,'r')
    sentence=file.read()
    return sentence

def substitute_msg(message_c):
    sub=''
    f={'Red':'Army General','Green':'Data Scientist','Blue':'Marine Biologist'}
    for key in f :
        if key == message_c:
            sub =f.get(key)
   
    return sub




message_3=read_file(file_path_3)
secret_msg_2=substitute_msg(message_3)
print(message_3)



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
def read_file(path):
    file=open(path,'r')
    sentence=file.read()
    return sentence

def compare_msg(message_d,message_e):
    a_list=message_d.split(' ')
    b_list=message_e.split(' ')
    c_list=[x  for x in a_list if x not in b_list ]
    final_msg = ' '.join(c_list)
    return str(final_msg)

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
secret_msg_3=compare_msg(message_4,message_5)
print(message_4)
print(message_5)






# --------------
#Code starts here
file_path_6

#reading file
def read_file(path):
    file=open(path,'r')
    sentence=file.read()
    return sentence


def extract_msg(message_f):
    a_list=message_6.split(' ')
    even_word=lambda x:len(x)%2==0
    b_list=list(filter(even_word,a_list))
    final_msg= ' '.join(b_list)
    return str(final_msg)


message_6=read_file(file_path_6)
secret_msg_4=extract_msg(message_6)
print(message_6)





# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg=' '.join(message_parts)


def write_file(secret_msg,path):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()
    print(secret_msg)

write_file(secret_msg,final_path)


