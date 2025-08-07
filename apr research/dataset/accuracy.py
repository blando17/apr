# count,count1,count2 = 0.0,0.0,0.0
# scount,scount2=0,0
# e1 = raw_input("Enter the dependency : ")
# e2 = raw_input("Enter the independent: ")
# hs = open("Accuracy.txt","a")
# with open('test.txt') as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
# for x in content:
#     scount,scount2=0,0
#     for y in xrange(len(e1)):
#         if e1[y] in x:
#             scount=scount+1
#     if scount==len(e1):
#         count1=count1+1.0
#     for z in xrange(len(e2)):
#         if e2[z] in x:
#             scount2=scount2+1
#     if scount2==len(e2):
#         count2=count2+1.0
# count=count1/count2*100        
# print str(count)+"%"
# hs.write(e1+"==>"+e2+" Accuracy: "+str(count)+"%\n")
# hs.close()

        
