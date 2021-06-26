import cv2
import time
model=cv2.face.LBPHFaceRecognizer_create()
model.read('face_LBPH.yml')
f=open('member.txt','r')#讀入模型
names=f.readline().split(',')#讀入姓名存於串列
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt2.xml")
cap=cv2.VideoCapture(0)
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
# 10~22行是用攝影機擷取使用者圖片，5秒內按z進行拍攝，如未按鍵，5秒後自動拍攝
timenow=time.time()#取得現在時間數值
while(cap.isOpened()):#cam開啟成功
    count=5 - int(time.time()-timenow)#倒數計時五秒
    ret,img=cap.read()
    if ret==True:
        imgcopy=img.copy()#複製影像
        cv2.putText(imgcopy,str(count),(200,400),cv2.FONT_HERSHEY_SIMPLEX,15,(0,0,255),35)#在複製影像上畫倒數秒數
        cv2.imshow("frame",imgcopy)#顯示複製影像
        k=cv2.waitKey(100)#0.1秒讀鍵盤一次
        if k==ord("z")or k==ord("z")or count==0:#按Z或倒數計時結束
            cv2.imwrite("tem.jpg",img)
            break
cap.release()#關閉CAM
cv2.destroyAllWindows()
#載入模型並取得使用者圖片後，進行臉部辨識判斷是否登入
img=cv2.imread("tem.jpg")#讀取圖片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #進行臉部偵測
faces=face_cascade.detectMultiScale(gray,1.1,3) #進行臉部偵測
for (x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    face_img=cv2.resize(gray[y:y+h,x:x+w],(400,400))#調整成訓練時大小
    try: # 進行臉部辨識
        val=model.predict(face_img)
        if val[1]<50:#辨識成功,顯示登入訊息
            print('歡迎'+name[val[0]]+'登入!',val[1])
        else:
            print('抱歉!你不是會員，無法登入!')
    except:
        print('辨識時產生錯誤')