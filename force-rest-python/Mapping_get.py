import json

with open('hai.txt') as data_file:    
    data = json.load(data_file)
    

#o = {"Wraper": {}} 
# i = 1
# for key, sub_data in data.iteritems():
#     for key_sub, value in sub_data.iteritems():
#         output["Wraper"] [key_sub + str(i)] = value
#     i += 1

#print output
test= data

# test=raw_input("Give file name as input :")
def parse_dict(init, lkey=''):
    
     ret =  {}  
     
     for (rkey,val) in init.items():
        #for (rkey, val) in init.items():
        key = lkey+rkey
       
        #print key
        if isinstance(val, dict):
            ret.update(parse_dict(val, key+"_"))
            #print parse_dict(val, key+'_')
        else:
            ret[key] = val
     return ret

print {"wrpVals": (parse_dict(test,""))} 

#############3To work on above code () remove this in hai.txt if it is exist

