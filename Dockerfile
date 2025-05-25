# Sử dụng image python
FROM python:3.11

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy toàn bộ file vào container
COPY . .

# Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Chạy ứng dụng với uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]

