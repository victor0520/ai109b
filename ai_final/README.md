# AI期末-臉部辨識
* 本專案修改自上學期<Python初學特訓班>14.2.2 , 14.2.3 之程式碼，在程式碼裡加上一些註釋，並展示實行結果
## 簡介
* 本專案使用OpenCV的模組，並使用LBPH(Local Binary Pattern Histogram)演算法訓練、辨識
* create_data.py
    * 先用擷取用戶的100張照片，依照使用者輸入的名字作為一個資料夾存入[images](https://github.com/victor0520/ai109b/tree/main/ai_final/images)\
    ![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/3.png)
    * 再用LBPH訓練模型，並存入[face_LBPH.yml](https://github.com/victor0520/ai109b/blob/main/ai_final/face_LBPH.yml)

* recogface.py
    * 先用攝影機擷取使用者圖片，5秒內按z進行拍攝，如未按鍵，5秒後自動拍攝
    * 載入模型並取得使用者圖片後，進行臉部辨識判斷是否登入
    * 辨識差異度小於50就辨識成功可以登錄

## 展示
### 建立資料庫並訓練模型
* [create_data.py](https://github.com/victor0520/ai109b/blob/main/ai_final/create_data.py)\
![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/1.png)

### 進行臉部辨識登錄入
* [recogface.py](https://github.com/victor0520/ai109b/blob/main/ai_final/recogface.py)\
![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/2.png)

## 本專案只用於學習所用