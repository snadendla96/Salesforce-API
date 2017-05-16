with open('test.txt','r') as file :
   filedata = file.read()
   #print filedata
# Replace the target string
tu = filedata.replace("u", '',)#to replace all 'u' in file
ll = tu.replace("'", '"',)#to replace the single quotes with double
ls = ll.replace(" ", "")#to replace the empty spaces between the words
ld = ls.replace(".", "")#to remove.

with open('test.txt','w') as ofile :
   ofile.write(ld)


# with open('test.txt','r') as file :
#    filedata = file.read()
#    #print filedata

# # Replace the target string
# tt = filedata.replace("u", '',)

# ll = tt.replace("'", '"',)



# with open('test.txt','w') as ofile :
#    ofile.write(ll)
