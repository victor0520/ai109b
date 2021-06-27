# AI期末-臉部辨識
* 本專案修改自上學期<Python初學特訓班>14.2.2 , 14.2.3 之程式碼，在程式碼裡加上一些註釋，並展示實行結果
## 簡介
### [OpenCV](https://zh.wikipedia.org/wiki/OpenCV)
* OpenCV的全稱是Open Source Computer Vision Library，是一個跨平台的電腦視覺庫
* OpenCV可用於開發即時的圖像處理、電腦視覺以及圖型識別程式
* 應用領域
    * 擴增實境
    * 臉部辨識
    * 手勢辨識
    * 人機互動
    * 動作辨識
    * 運動跟蹤
    * 物體辨識
    * 圖像分割
    * 機器人

### [LBPH](https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b)
* 原始的LBP算子定義為在3\*3的窗口內，以窗口中心像素為閾值，將相鄰的8個像素的灰度值與其進行比較，若周圍像素值大於或等於中心像素值，則該像素點的位置被標記為1，否則為0。這樣，3\*3鄰域內的8個點經比較可產生8位二進制數（通常轉換為十進制數即LBP碼，共256種），如下圖所示\
![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/4.png)
* 基本的LBP算子的最大缺陷在於它只覆蓋了一個固定半徑范圍內的小區域，這顯然不能滿足不同尺寸和頻率紋理的需要。為了適應不同尺度的紋理特征，Ojala等對LBP算子進行了改進，將3×3鄰域擴展到任意鄰域，並用圓形鄰域代替了正方形鄰域，改進后的LBP算子允許在半徑為R的圓形鄰域內有任意多個像素點，從而得到了諸如半徑為R的圓形區域內含有P個采樣點的LBP算子，OpenCV中正是使用圓形LBP算子，下圖示意了圓形LBP算子：\
![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/5.png)
* LBP算子在每個像素點都可以得到一個LBP“編碼”，那么，對一幅圖像（記錄的是每個像素點的灰度值）提取其原始的LBP算子之后，得到的原始LBP特征依然是“一幅圖片”，範例如下:\
![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/6.png)
### final
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

### 進行臉部辨識登入
* [recogface.py](https://github.com/victor0520/ai109b/blob/main/ai_final/recogface.py)\
![PICTURE](https://github.com/victor0520/ai109b/blob/main/ai_final/2.png)


## 本專案只用於學習所用
* [LICENSE](https://github.com/victor0520/ai109b/blob/main/ai_final/LICENSE.md)
### 資料來源
* [kelvins/lbph-Local Binary Patterns Histograms (LBPH)](https://github.com/kelvins/lbph)
* [OpenCV人臉識別LBPH算法源碼分析](https://zh.codeprj.com/blog/5da48a1.html)