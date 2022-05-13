import shutil
import sys
# ---------------------------PART A: Bin Files ---------------------------
with open('NI_all.txt', 'w') as wfd:
    for f in ['NIR(0-5).txt', 'NIR(5-10).txt', 'NIR(10-15).txt', 'NIR(15-20).txt', 'NIR(20-25).txt',
              'NIR(25-30).txt','NIR(30-35).txt','NIR(35-40).txt','NIR(40-45).txt','NIR(45-50).txt',
              'NIR(50-55).txt', 'NIR(55-60).txt', 'NIR(60-65).txt', 'NIR(65-70).txt', 'NIR(70-75).txt',
              'NIR(75-80).txt','NIR(80-85).txt','NIR(85-90).txt','NIR(90-95).txt','NIR(95-100).txt'
              ]:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
# To eliminate blank lines
output=""
with open('NI_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("Final.txt","w")
f.write(output)
