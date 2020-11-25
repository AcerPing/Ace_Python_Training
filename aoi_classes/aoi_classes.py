import codecs

classes =  ["fish1","fish2","fish3"]
# "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor","fish1","fish2","fish3"
print(len(classes))

for every_class in classes:
    file = open("aoi_classes.txt",mode="a") #開啟檔案
    file.write(every_class) #撰寫檔案
    file.write("\r")
file.close() #關閉檔案



    # print(every_class)
