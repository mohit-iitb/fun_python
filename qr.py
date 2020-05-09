import qrcode
# example data
# output file name
data = "https://www.facebook.com/mohit.agarwala.496"
filename = "mohit_fb.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

####START COMPETITIVE CODING FROM TODAY,WATCH RAVI BABU AND 9HRS
#LONG LECTURE,ALSO DO ML AND PANDAS
