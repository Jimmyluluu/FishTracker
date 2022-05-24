## 使用虛擬環境

### 使用 virtualenv 環境
```
pip3 install virtualenv
```

### 如果有看到一個檔案叫 venv 可以跳到進入環境 也不需要下載所需套件

### 使用安裝 python 3.8 環境
```
virtualenv --python=/opt/python-3.8/bin/python venv
```

### 建立安裝好的虛擬環境
```
python3 -m venv venv
```

### 進入此環境
```
source ./venv/bin/activate
```
### 下載所需套件
```
pip install -r requirements.txt 
```