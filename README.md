# BIG DATA TEST PROJECT

Dự án kiểm thử và xử lý dữ liệu Big Data (H&M Dataset).

## Thành phần
- `01_ingest_bronze.ipynb`: Notebook xử lý dữ liệu chính.
- `src/`: Thư mục mã nguồn xử lý dữ liệu.
- `tests/`: Thư mục chứa Unit Test (sử dụng pytest).
- `.github/workflows/`: Thiết lập CI/CD chạy tự động trên GitHub Actions.

## Cài đặt
1. Cài đặt Python 3.9+
2. Cài đặt dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Cài đặt Java 11 (yêu cầu để chạy Spark).

## Chạy Test
Sử dụng lệnh sau để chạy unit test:
```bash
pytest tests/
```

## CI/CD
Dự án được tích hợp GitHub Actions, tự động chạy test mỗi khi có thay đổi được push lên repository.
