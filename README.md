# 使用虛擬環境

## 首次進入
### 使用 virtualenv 環境
```
pip3 install virtualenv
```

### 使用安裝 python 3.8 環境(可省略)
```
virtualenv --python=/opt/python-3.8/bin/python venv
```

### 建立安裝好的虛擬環境
```
python3 -m venv venv
```

### 進入此環境 mac
```
source ./venv/bin/activate
```
### 進入此環境 windows
```
 .\venv\Scripts\activate.ps1 
```
### 下載所需套件
```
pip install -r requirements.txt 
```
### 執行
```
python FishTracker.py
```
## 創建好虛擬環境後
### 進入此環境
```
source ./venv/bin/activate
```
### 執行
```
python FishTracker.py
```