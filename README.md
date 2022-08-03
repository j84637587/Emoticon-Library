# Emoticon-Library
此專案利用pyqt6製作顏文字庫，以提供快速、自訂化的顏文字庫。

UI使用 QT Designer設計

### 需求
- Python > 3.9

### 使用方法
將所需記錄的顏文字依照以下格式加入至 `emojis.json`

`text` 為要記錄的顏文字

`tags` 是該顏文字之標籤，可自行設計。並於後續加入之搜尋功能中使用。

```
  {
    "text": "( ⁎ᵕᴗᵕ⁎ )❤︎",
    "tags": [
        "愛"
    ]
  }
```
配置完成後執行以下指令
```
python3 controller.py
```

### DEMO
![image](https://user-images.githubusercontent.com/29170077/182717066-50ac2b53-7901-4a66-b37f-b3690edcf324.png)


### TODO
- [x] 顏文字複製
- [ ] 搜尋功能
- [ ] GUI內新增顏文字功能 
- [ ] 修正部分符號顯示異常(不影響複製)
