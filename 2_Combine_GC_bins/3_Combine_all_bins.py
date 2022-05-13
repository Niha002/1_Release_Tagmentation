import shutil
import sys
# ---------------------------PART A: Bin Files ---------------------------
# Merging sequences below each other
with open('R(0-5)_all.txt', 'w') as wfd:
    for f in ['R(0-5)_ERR4074329.txt', 'R(0-5)_HuS3.txt', 'R(0-5)_LambdaS1.txt', 'R(0-5)_SRR3927455.txt', 'R(0-5)_SRR4034345_L001.txt',
              'R(0-5)_SRR8526281.txt','R(0-5)_SRR9118212.txt','R(0-5)_SRR9319306.txt','R(0-5)_SSRR4037684_L001.txt','R(0-5)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
# To eliminate blank lines
output=""
with open('R(0-5)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(0-5).txt","w")
f.write(output)

with open('R(5-10)_all.txt', 'w') as wfd:
    for f in ['R(5-10)_ERR4074329.txt', 'R(5-10)_HuS3.txt', 'R(5-10)_LambdaS1.txt', 'R(5-10)_SRR3927455.txt','R(5-10)_SRR4034345_L001.txt',
              'R(5-10)_SRR8526281.txt', 'R(5-10)_SRR9118212.txt', 'R(5-10)_SRR9319306.txt', 'R(5-10)_SRR4037684_L001.txt','R(5-10)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(5-10)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(5-10).txt","w")
f.write(output)

with open('R(10-15)_all.txt', 'w') as wfd:
    for f in ['R(10-15)_ERR4074329.txt', 'R(10-15)_HuS3.txt', 'R(10-15)_LambdaS1.txt', 'R(10-15)_SRR3927455.txt',
              'R(10-15)_SRR4034345_L001.txt',
              'R(10-15)_SRR8526281.txt', 'R(10-15)_SRR9118212.txt', 'R(10-15)_SRR9319306.txt',
              'R(10-15)_SRR4037684_L001.txt', 'R(10-15)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(10-15)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(10-15).txt","w")
f.write(output)

with open('R(15-20)_all.txt', 'w') as wfd:
    for f in ['R(15-20)_ERR4074329.txt', 'R(15-20)_HuS3.txt', 'R(15-20)_LambdaS1.txt', 'R(15-20)_SRR3927455.txt',
              'R(15-20)_SRR4034345_L001.txt',
              'R(15-20)_SRR8526281.txt', 'R(15-20)_SRR9118212.txt', 'R(15-20)_SRR9319306.txt',
              'R(15-20)_SRR4037684_L001.txt', 'R(15-20)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(15-20)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(15-20).txt","w")
f.write(output)

with open('R(20-25)_all.txt', 'w') as wfd:
    for f in ['R(20-25)_ERR4074329.txt', 'R(20-25)_HuS3.txt', 'R(20-25)_LambdaS1.txt', 'R(20-25)_SRR3927455.txt',
              'R(20-25)_SRR4034345_L001.txt',
              'R(20-25)_SRR8526281.txt', 'R(20-25)_SRR9118212.txt', 'R(20-25)_SRR9319306.txt',
              'R(20-25)_SRR4037684_L001.txt', 'R(20-25)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(20-25)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(20-25).txt","w")
f.write(output)

with open('R(25-30)_all.txt', 'w') as wfd:
    for f in ['R(25-30)_ERR4074329.txt', 'R(25-30)_HuS3.txt', 'R(25-30)_LambdaS1.txt', 'R(25-30)_SRR3927455.txt',
              'R(25-30)_SRR4034345_L001.txt',
              'R(25-30)_SRR8526281.txt', 'R(25-30)_SRR9118212.txt', 'R(25-30)_SRR9319306.txt',
              'R(25-30)_SRR4037684_L001.txt', 'R(25-30)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(25-30)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(25-30).txt","w")
f.write(output)

with open('R(30-35)_all.txt', 'w') as wfd:
    for f in ['R(30-35)_ERR4074329.txt', 'R(30-35)_HuS3.txt', 'R(30-35)_LambdaS1.txt', 'R(30-35)_SRR3927455.txt',
              'R(30-35)_SRR4034345_L001.txt',
              'R(30-35)_SRR8526281.txt', 'R(30-35)_SRR9118212.txt', 'R(30-35)_SRR9319306.txt',
              'R(30-35)_SRR4037684_L001.txt', 'R(30-35)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(30-35)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(30-35).txt","w")
f.write(output)

with open('R(35-40)_all.txt', 'w') as wfd:
    for f in ['R(35-40)_ERR4074329.txt', 'R(35-40)_HuS3.txt', 'R(35-40)_LambdaS1.txt', 'R(35-40)_SRR3927455.txt',
              'R(35-40)_SRR4034345_L001.txt',
              'R(35-40)_SRR8526281.txt', 'R(35-40)_SRR9118212.txt', 'R(35-40)_SRR9319306.txt',
              'R(35-40)_SRR4037684_L001.txt', 'R(35-40)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(35-40)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(35-40).txt","w")
f.write(output)

with open('R(40-45)_all.txt', 'w') as wfd:
    for f in ['R(40-45)_ERR4074329.txt', 'R(40-45)_HuS3.txt', 'R(40-45)_LambdaS1.txt', 'R(40-45)_SRR3927455.txt',
              'R(40-45)_SRR4034345_L001.txt',
              'R(40-45)_SRR8526281.txt', 'R(40-45)_SRR9118212.txt', 'R(40-45)_SRR9319306.txt',
              'R(40-45)_SRR4037684_L001.txt', 'R(40-45)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(40-45)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(40-45).txt","w")
f.write(output)

with open('R(45-50)_all.txt', 'w') as wfd:
    for f in ['R(45-50)_ERR4074329.txt', 'R(45-50)_HuS3.txt', 'R(45-50)_LambdaS1.txt', 'R(45-50)_SRR3927455.txt',
              'R(45-50)_SRR4034345_L001.txt',
              'R(45-50)_SRR8526281.txt', 'R(45-50)_SRR9118212.txt', 'R(45-50)_SRR9319306.txt',
              'R(45-50)_SRR4037684_L001.txt', 'R(45-50)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(45-50)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(45-50).txt","w")
f.write(output)


with open('R(50-55)_all.txt', 'w') as wfd:
    for f in ['R(50-55)_ERR4074329.txt', 'R(50-55)_HuS3.txt', 'R(50-55)_LambdaS1.txt', 'R(50-55)_SRR3927455.txt',
              'R(50-55)_SRR4034345_L001.txt',
              'R(50-55)_SRR8526281.txt', 'R(50-55)_SRR9118212.txt', 'R(50-55)_SRR9319306.txt',
              'R(50-55)_SRR4037684_L001.txt', 'R(50-55)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(50-55)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(50-55).txt","w")
f.write(output)

with open('R(55-60)_all.txt', 'w') as wfd:
    for f in ['R(55-60)_ERR4074329.txt', 'R(55-60)_HuS3.txt', 'R(55-60)_LambdaS1.txt', 'R(55-60)_SRR3927455.txt',
              'R(55-60)_SRR4034345_L001.txt',
              'R(55-60)_SRR8526281.txt', 'R(55-60)_SRR9118212.txt', 'R(55-60)_SRR9319306.txt',
              'R(55-60)_SRR4037684_L001.txt', 'R(55-60)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(55-60)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(55-60).txt","w")
f.write(output)

with open('R(60-65)_all.txt', 'w') as wfd:
    for f in ['R(60-65)_ERR4074329.txt', 'R(60-65)_HuS3.txt', 'R(60-65)_LambdaS1.txt', 'R(60-65)_SRR3927455.txt',
              'R(60-65)_SRR4034345_L001.txt',
              'R(60-65)_SRR8526281.txt', 'R(60-65)_SRR9118212.txt', 'R(60-65)_SRR9319306.txt',
              'R(60-65)_SRR4037684_L001.txt', 'R(60-65)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(60-65)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(60-65).txt","w")
f.write(output)

with open('R(65-70)_all.txt', 'w') as wfd:
    for f in ['R(65-70)_ERR4074329.txt', 'R(65-70)_HuS3.txt', 'R(65-70)_LambdaS1.txt', 'R(65-70)_SRR3927455.txt',
              'R(65-70)_SRR4034345_L001.txt',
              'R(65-70)_SRR8526281.txt', 'R(65-70)_SRR9118212.txt', 'R(65-70)_SRR9319306.txt',
              'R(65-70)_SRR4037684_L001.txt', 'R(65-70)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(65-70)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(65-70).txt","w")
f.write(output)

with open('R(70-75)_all.txt', 'w') as wfd:
    for f in ['R(70-75)_ERR4074329.txt', 'R(70-75)_HuS3.txt', 'R(70-75)_LambdaS1.txt', 'R(70-75)_SRR3927455.txt',
              'R(70-75)_SRR4034345_L001.txt',
              'R(70-75)_SRR8526281.txt', 'R(70-75)_SRR9118212.txt', 'R(70-75)_SRR9319306.txt',
              'R(70-75)_SRR4037684_L001.txt', 'R(70-75)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(70-75)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(70-75).txt","w")
f.write(output)

with open('R(75-80)_all.txt', 'w') as wfd:
    for f in ['R(75-80)_ERR4074329.txt', 'R(75-80)_HuS3.txt', 'R(75-80)_LambdaS1.txt', 'R(75-80)_SRR3927455.txt',
              'R(75-80)_SRR4034345_L001.txt',
              'R(75-80)_SRR8526281.txt', 'R(75-80)_SRR9118212.txt', 'R(75-80)_SRR9319306.txt',
              'R(75-80)_SRR4037684_L001.txt', 'R(75-80)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(75-80)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(75-80).txt","w")
f.write(output)

with open('R(80-85)_all.txt', 'w') as wfd:
    for f in ['R(80-85)_ERR4074329.txt', 'R(80-85)_HuS3.txt', 'R(80-85)_LambdaS1.txt', 'R(80-85)_SRR3927455.txt',
              'R(80-85)_SRR4034345_L001.txt',
              'R(80-85)_SRR8526281.txt', 'R(80-85)_SRR9118212.txt', 'R(80-85)_SRR9319306.txt',
              'R(80-85)_SRR4037684_L001.txt', 'R(80-85)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(80-85)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(80-85).txt","w")
f.write(output)

with open('R(85-90)_all.txt', 'w') as wfd:
    for f in ['R(85-90)_ERR4074329.txt', 'R(85-90)_HuS3.txt', 'R(85-90)_LambdaS1.txt', 'R(85-90)_SRR3927455.txt',
              'R(85-90)_SRR4034345_L001.txt',
              'R(85-90)_SRR8526281.txt', 'R(85-90)_SRR9118212.txt', 'R(85-90)_SRR9319306.txt',
              'R(85-90)_SRR4037684_L001.txt', 'R(85-90)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(85-90)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(85-90).txt","w")
f.write(output)

with open('R(90-95)_all.txt', 'w') as wfd:
    for f in ['R(90-95)_ERR4074329.txt', 'R(90-95)_HuS3.txt', 'R(90-95)_LambdaS1.txt', 'R(90-95)_SRR3927455.txt',
              'R(90-95)_SRR4034345_L001.txt',
              'R(90-95)_SRR8526281.txt', 'R(90-95)_SRR9118212.txt', 'R(90-95)_SRR9319306.txt',
              'R(90-95)_SRR4037684_L001.txt', 'R(90-95)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(90-95)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(90-95).txt","w")
f.write(output)

with open('R(95-100)_all.txt', 'w') as wfd:
    for f in ['R(95-100)_ERR4074329.txt', 'R(95-100)_HuS3.txt', 'R(95-100)_LambdaS1.txt', 'R(95-100)_SRR3927455.txt',
              'R(95-100)_SRR4034345_L001.txt',
              'R(95-100)_SRR8526281.txt', 'R(95-100)_SRR9118212.txt', 'R(95-100)_SRR9319306.txt',
              'R(95-100)_SRR4037684_L001.txt', 'R(95-100)_WTW_S2.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
with open('R(95-100)_all.txt','r+') as file:
    for line in file:
        if not line.isspace():
            file.write(line)
output=""
with open('R(95-100)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("1_R(95-100).txt","w")
f.write(output)
