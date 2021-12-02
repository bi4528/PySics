
#import tarfile

#tar = tarfile.open("F:\\MyFolder\\MIVIA\\eta3.tar.gz", "r:gz")

#a = tar.next()

#while a in tar.list():
#    print(a)
#    a = tar.next()

#file = tar.extractfile("lab8_nonuni_eta2\\target\\si2_rnd_eta02_m300.B13.grf")

#print("1")

#print(file.read())

#tar.close()

file = open("F:\\MyFolder\\MIVIA\\eta2.tar\\eta2 2\\lab8_nonuni_eta2\\target\\si2_rnd_eta02_m300.B30.grf")
count = 0

while True:
    count += 1
 
    # Get next line from file
    line = file.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
 
file.close()