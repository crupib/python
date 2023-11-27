import re
import os

#system("get-vmhostnetworkadapter -VMHost 10.211.211.6")
#system('Get-VM | select Name,@{n="UUID";e={$_.ExtensionData.Summary.Config.Uuid}}')
filepath = 'powercli.txt'
filepath2 = 'powercli2.txt'
with open(filepath2) as fp2:
   array2 = []
   for line2 in fp2:
     array2.append(line2)
   y2 = [None] * len(array2)
   cnt = 0
   for x in array2:
      y2[cnt] = re.split('\s+',x)
      cnt = cnt + 1
   for x in y2:
          if x[0] in [' ','Name','----','']:
             continue
          uuid=(x[1])
with open(filepath) as fp:
   array = [] 
   for line in fp:
     array.append(line)
   y = [None] * len(array)
   cnt = 0
   for x in array:
      y[cnt] = re.split('\s+',x)
      cnt = cnt + 1
   cnt = 0
   for x in y:
      if x[0] in [' ','Name','---','----','','vmk0']:
         continue
      str1 = ("ifcfg-eth"+str(cnt))
      file = open(str1,"w")
      file.write("DEVICE=eth%i\n"%cnt)
      file.write("HWADDR=%s\n"%x[1])
      file.write("TYPE=Ethernet\n")
      file.write("ONBOOT=YES\n")
      file.write("NM_CONTROLLED=yes\n")
      file.write("BOOTPRO=none\n")
      file.write("UUID=%s\n"%uuid)
      file.close()
      cnt = cnt + 1
