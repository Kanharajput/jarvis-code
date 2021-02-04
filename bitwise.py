value1 = 25
value2 = 15    
value3 = value1 & value2 
value4 = value1 | value2
# here 25 and 15 converted into binary and then in & operator it is multiply , and for | it is added                        
# binary of 25 is 11001 and binary of 15 is 01111
# when operator is & 
#    11001
#    01111
# -> 01001 which is 9
# when the operator is |
#     11001
#     01111
# ->  11111
print("By means of & operator " , value3 , "\n")
print("By means of | operator " , value4)