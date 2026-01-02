print("File download time calculator: ")
filesize=float(input("Enter the filesize in Megabytes(MB): "))
downloadspeed=float(input("Enter the download speed(MB/s): "))
time=filesize/downloadspeed
print("The time taken to download the file(in seconds) with the given speed is: ",round(time,2))