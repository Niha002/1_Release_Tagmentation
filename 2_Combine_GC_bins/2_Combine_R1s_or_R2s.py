import shutil
import sys
# ---------------------------PART A: Bin Files ---------------------------
# Merging sequences below each other
with open('R(0-5)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 0-5.txt', 'Z_HuS3_R2_Range 0-5.txt', 'Z_LambdaS1_R2_Range 0-5.txt', 'Z_SRR3927455_R2_Range 0-5.txt', 'Z_SRR4034345_L001_R2_Range 0-5.txt',
              'Z_SRR4037684_L001_R2_Range 0-5.txt','Z_SRR8526281_R2_Range 0-5.txt','Z_SRR9118212_R2_Range 0-5.txt','Z_SRR9319306_R2_Range 0-5.txt','Z_WTW_S2_R2_Range 0-5.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(0-5)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(0-5).txt","w")
f.write(output)

with open('R(5-10)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 5-10.txt', 'Z_HuS3_R2_Range 5-10.txt', 'Z_LambdaS1_R2_Range 5-10.txt',
              'Z_SRR3927455_R2_Range 5-10.txt', 'Z_SRR4034345_L001_R2_Range 5-10.txt',
              'Z_SRR4037684_L001_R2_Range 5-10.txt', 'Z_SRR8526281_R2_Range 5-10.txt', 'Z_SRR9118212_R2_Range 5-10.txt',
              'Z_SRR9319306_R2_Range 5-10.txt', 'Z_WTW_S2_R2_Range 5-10.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(5-10)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(5-10).txt","w")
f.write(output)

with open('R(10-15)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 10-15.txt', 'Z_HuS3_R2_Range 10-15.txt', 'Z_LambdaS1_R2_Range 10-15.txt',
              'Z_SRR3927455_R2_Range 10-15.txt', 'Z_SRR4034345_L001_R2_Range 10-15.txt',
              'Z_SRR4037684_L001_R2_Range 10-15.txt', 'Z_SRR8526281_R2_Range 10-15.txt', 'Z_SRR9118212_R2_Range 10-15.txt',
              'Z_SRR9319306_R2_Range 10-15.txt', 'Z_WTW_S2_R2_Range 10-15.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(10-15)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(10-15).txt","w")
f.write(output)

with open('R(15-20)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 15-20.txt', 'Z_HuS3_R2_Range 15-20.txt', 'Z_LambdaS1_R2_Range 15-20.txt',
              'Z_SRR3927455_R2_Range 15-20.txt', 'Z_SRR4034345_L001_R2_Range 15-20.txt',
              'Z_SRR4037684_L001_R2_Range 15-20.txt', 'Z_SRR8526281_R2_Range 15-20.txt',
              'Z_SRR9118212_R2_Range 15-20.txt',
              'Z_SRR9319306_R2_Range 15-20.txt', 'Z_WTW_S2_R2_Range 15-20.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(15-20)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(15-20).txt","w")
f.write(output)

with open('R(20-25)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 20-25.txt', 'Z_HuS3_R2_Range 20-25.txt', 'Z_LambdaS1_R2_Range 20-25.txt',
              'Z_SRR3927455_R2_Range 20-25.txt', 'Z_SRR4034345_L001_R2_Range 20-25.txt',
              'Z_SRR4037684_L001_R2_Range 20-25.txt', 'Z_SRR8526281_R2_Range 20-25.txt',
              'Z_SRR9118212_R2_Range 20-25.txt',
              'Z_SRR9319306_R2_Range 20-25.txt', 'Z_WTW_S2_R2_Range 20-25.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(20-25)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(20-25).txt","w")
f.write(output)

with open('R(25-30)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 25-30.txt', 'Z_HuS3_R2_Range 25-30.txt', 'Z_LambdaS1_R2_Range 25-30.txt',
              'Z_SRR3927455_R2_Range 25-30.txt', 'Z_SRR4034345_L001_R2_Range 25-30.txt',
              'Z_SRR4037684_L001_R2_Range 25-30.txt', 'Z_SRR8526281_R2_Range 25-30.txt',
              'Z_SRR9118212_R2_Range 25-30.txt',
              'Z_SRR9319306_R2_Range 25-30.txt', 'Z_WTW_S2_R2_Range 25-30.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(25-30)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(25-30).txt","w")
f.write(output)

with open('R(30-35)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 30-35.txt', 'Z_HuS3_R2_Range 30-35.txt', 'Z_LambdaS1_R2_Range 30-35.txt',
              'Z_SRR3927455_R2_Range 30-35.txt', 'Z_SRR4034345_L001_R2_Range 30-35.txt',
              'Z_SRR4037684_L001_R2_Range 30-35.txt', 'Z_SRR8526281_R2_Range 30-35.txt',
              'Z_SRR9118212_R2_Range 30-35.txt',
              'Z_SRR9319306_R2_Range 30-35.txt', 'Z_WTW_S2_R2_Range 30-35.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(30-35)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(30-35).txt","w")
f.write(output)

with open('R(35-40)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 35-40.txt', 'Z_HuS3_R2_Range 35-40.txt', 'Z_LambdaS1_R2_Range 35-40.txt',
              'Z_SRR3927455_R2_Range 35-40.txt', 'Z_SRR4034345_L001_R2_Range 35-40.txt',
              'Z_SRR4037684_L001_R2_Range 35-40.txt', 'Z_SRR8526281_R2_Range 35-40.txt',
              'Z_SRR9118212_R2_Range 35-40.txt',
              'Z_SRR9319306_R2_Range 35-40.txt', 'Z_WTW_S2_R2_Range 35-40.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(35-40)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(35-40).txt","w")
f.write(output)

with open('R(40-45)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 40-45.txt', 'Z_HuS3_R2_Range 40-45.txt', 'Z_LambdaS1_R2_Range 40-45.txt',
              'Z_SRR3927455_R2_Range 40-45.txt', 'Z_SRR4034345_L001_R2_Range 40-45.txt',
              'Z_SRR4037684_L001_R2_Range 40-45.txt', 'Z_SRR8526281_R2_Range 40-45.txt',
              'Z_SRR9118212_R2_Range 40-45.txt',
              'Z_SRR9319306_R2_Range 40-45.txt', 'Z_WTW_S2_R2_Range 40-45.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(40-45)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(40-45).txt","w")
f.write(output)

with open('R(45-50)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 45-50.txt', 'Z_HuS3_R2_Range 45-50.txt', 'Z_LambdaS1_R2_Range 45-50.txt',
              'Z_SRR3927455_R2_Range 45-50.txt', 'Z_SRR4034345_L001_R2_Range 45-50.txt',
              'Z_SRR4037684_L001_R2_Range 45-50.txt', 'Z_SRR8526281_R2_Range 45-50.txt',
              'Z_SRR9118212_R2_Range 45-50.txt',
              'Z_SRR9319306_R2_Range 45-50.txt', 'Z_WTW_S2_R2_Range 45-50.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(45-50)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(45-50).txt","w")
f.write(output)


with open('R(50-55)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 50-55.txt', 'Z_HuS3_R2_Range 50-55.txt', 'Z_LambdaS1_R2_Range 50-55.txt',
              'Z_SRR3927455_R2_Range 50-55.txt', 'Z_SRR4034345_L001_R2_Range 50-55.txt',
              'Z_SRR4037684_L001_R2_Range 50-55.txt', 'Z_SRR8526281_R2_Range 50-55.txt',
              'Z_SRR9118212_R2_Range 50-55.txt',
              'Z_SRR9319306_R2_Range 50-55.txt', 'Z_WTW_S2_R2_Range 50-55.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(50-55)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(50-55).txt","w")
f.write(output)

with open('R(55-60)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 55-60.txt', 'Z_HuS3_R2_Range 55-60.txt', 'Z_LambdaS1_R2_Range 55-60.txt',
              'Z_SRR3927455_R2_Range 55-60.txt', 'Z_SRR4034345_L001_R2_Range 55-60.txt',
              'Z_SRR4037684_L001_R2_Range 55-60.txt', 'Z_SRR8526281_R2_Range 55-60.txt',
              'Z_SRR9118212_R2_Range 55-60.txt',
              'Z_SRR9319306_R2_Range 55-60.txt', 'Z_WTW_S2_R2_Range 55-60.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(55-60)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(55-60).txt","w")
f.write(output)

with open('R(60-65)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 60-65.txt', 'Z_HuS3_R2_Range 60-65.txt', 'Z_LambdaS1_R2_Range 60-65.txt',
              'Z_SRR3927455_R2_Range 60-65.txt', 'Z_SRR4034345_L001_R2_Range 60-65.txt',
              'Z_SRR4037684_L001_R2_Range 60-65.txt', 'Z_SRR8526281_R2_Range 60-65.txt',
              'Z_SRR9118212_R2_Range 60-65.txt',
              'Z_SRR9319306_R2_Range 60-65.txt', 'Z_WTW_S2_R2_Range 60-65.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(60-65)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(60-65).txt","w")
f.write(output)

with open('R(65-70)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 65-70.txt', 'Z_HuS3_R2_Range 65-70.txt', 'Z_LambdaS1_R2_Range 65-70.txt',
              'Z_SRR3927455_R2_Range 65-70.txt', 'Z_SRR4034345_L001_R2_Range 65-70.txt',
              'Z_SRR4037684_L001_R2_Range 65-70.txt', 'Z_SRR8526281_R2_Range 65-70.txt',
              'Z_SRR9118212_R2_Range 65-70.txt',
              'Z_SRR9319306_R2_Range 65-70.txt', 'Z_WTW_S2_R2_Range 65-70.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(65-70)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(65-70).txt","w")
f.write(output)

with open('R(70-75)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 70-75.txt', 'Z_HuS3_R2_Range 70-75.txt', 'Z_LambdaS1_R2_Range 70-75.txt',
              'Z_SRR3927455_R2_Range 70-75.txt', 'Z_SRR4034345_L001_R2_Range 70-75.txt',
              'Z_SRR4037684_L001_R2_Range 70-75.txt', 'Z_SRR8526281_R2_Range 70-75.txt',
              'Z_SRR9118212_R2_Range 70-75.txt',
              'Z_SRR9319306_R2_Range 70-75.txt', 'Z_WTW_S2_R2_Range 70-75.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(70-75)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(70-75).txt","w")
f.write(output)

with open('R(75-80)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 75-80.txt', 'Z_HuS3_R2_Range 75-80.txt', 'Z_LambdaS1_R2_Range 75-80.txt',
              'Z_SRR3927455_R2_Range 75-80.txt', 'Z_SRR4034345_L001_R2_Range 75-80.txt',
              'Z_SRR4037684_L001_R2_Range 75-80.txt', 'Z_SRR8526281_R2_Range 75-80.txt',
              'Z_SRR9118212_R2_Range 75-80.txt',
              'Z_SRR9319306_R2_Range 75-80.txt', 'Z_WTW_S2_R2_Range 75-80.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(75-80)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(75-80).txt","w")
f.write(output)

with open('R(80-85)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 80-85.txt', 'Z_HuS3_R2_Range 80-85.txt', 'Z_LambdaS1_R2_Range 80-85.txt',
              'Z_SRR3927455_R2_Range 80-85.txt', 'Z_SRR4034345_L001_R2_Range 80-85.txt',
              'Z_SRR4037684_L001_R2_Range 80-85.txt', 'Z_SRR8526281_R2_Range 80-85.txt',
              'Z_SRR9118212_R2_Range 80-85.txt',
              'Z_SRR9319306_R2_Range 80-85.txt', 'Z_WTW_S2_R2_Range 80-85.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(80-85)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(80-85).txt","w")
f.write(output)

with open('R(85-90)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 85-90.txt', 'Z_HuS3_R2_Range 85-90.txt', 'Z_LambdaS1_R2_Range 85-90.txt',
              'Z_SRR3927455_R2_Range 85-90.txt', 'Z_SRR4034345_L001_R2_Range 85-90.txt',
              'Z_SRR4037684_L001_R2_Range 85-90.txt', 'Z_SRR8526281_R2_Range 85-90.txt',
              'Z_SRR9118212_R2_Range 85-90.txt',
              'Z_SRR9319306_R2_Range 85-90.txt', 'Z_WTW_S2_R2_Range 85-90.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(85-90)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(85-90).txt","w")
f.write(output)

with open('R(90-95)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 90-95.txt', 'Z_HuS3_R2_Range 90-95.txt', 'Z_LambdaS1_R2_Range 90-95.txt',
              'Z_SRR3927455_R2_Range 90-95.txt', 'Z_SRR4034345_L001_R2_Range 90-95.txt',
              'Z_SRR4037684_L001_R2_Range 90-95.txt', 'Z_SRR8526281_R2_Range 90-95.txt',
              'Z_SRR9118212_R2_Range 90-95.txt',
              'Z_SRR9319306_R2_Range 90-95.txt', 'Z_WTW_S2_R2_Range 90-95.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
output=""
with open('R(90-95)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(90-95).txt","w")
f.write(output)

with open('R(95-100)_all.txt', 'w') as wfd:
    for f in ['Z_ERR4074329_R2_Range 95-100.txt', 'Z_HuS3_R2_Range 95-100.txt', 'Z_LambdaS1_R2_Range 95-100.txt',
              'Z_SRR3927455_R2_Range 95-100.txt', 'Z_SRR4034345_L001_R2_Range 95-100.txt',
              'Z_SRR4037684_L001_R2_Range 95-100.txt', 'Z_SRR8526281_R2_Range 95-100.txt',
              'Z_SRR9118212_R2_Range 95-100.txt',
              'Z_SRR9319306_R2_Range 95-100.txt', 'Z_WTW_S2_R2_Range 95-100.txt']:
        with open(f, 'r') as fd:
            shutil.copyfileobj(fd, wfd)
            wfd.write("\n")
with open('R(95-100)_all.txt') as f:
    for line in f:
        if not line.isspace():
            output+=line
f = open("R2_R(95-100).txt","w")
f.write(output)
