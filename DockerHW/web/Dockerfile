# 使用 Python 基礎映像
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製當前目錄所有檔案到容器中
COPY . /app

# 安裝 Flask（如果你的網頁是 Flask 應用）
RUN pip install --no-cache-dir -r requirements.txt

# 設定 Flask 入口
CMD ["python", "main.py"]
