
# Comment Classification (Python + Flask)

Một ứng dụng web dùng **Flask** để phân loại bình luận nhận xét của về sản phẩm trên sàn thương mại điện tử

---

## Nội dung

* `app.py`: file chính khởi chạy ứng dụng Flask, xử lý route, nhận đầu vào từ người dùng, trả kết quả phân loại. ([GitHub][1])
* `templates/`: chứa các file HTML dùng để render giao diện người dùng. ([GitHub][1])
* `static/`: chứa các tài nguyên CSS, hình ảnh, JS . ([GitHub][1])
* `requirements.txt`: liệt kê các thư viện Python cần cài để chạy app. ([GitHub][1])
* File phụ trợ: `word (1).txt` — từ vựng (vocabulary) dùng trong mô hình phân loại. ([GitHub][1])

---

## Cài đặt & sử dụng

Dưới đây là các bước để chạy ứng dụng này trên máy local:

1. Clone repo:

   ```bash
   git clone https://github.com/thesea58/Comment-classification-python-flask.git
   cd Comment-classification-python-flask
   ```

2. Tạo môi trường ảo (virtual environment) (khuyến nghị):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # trên Linux/macOS
   # hoặc
   venv\Scripts\activate      # trên Windows
   ```

3. Cài các thư viện cần thiết:

   ```bash
   pip install -r requirements.txt
   ```

4. Chạy ứng dụng Flask:

   ```bash
   python app.py
   ```

   hoặc nếu muốn bật chế độ debug:

   ```bash
   export FLASK_ENV=development
   python app.py
   ```

5. Mở trình duyệt và truy cập:

   ```
   http://localhost:5000
   ```

   (Port mặc định có thể là 5000, nếu bạn thay đổi trong `app.py` thì theo đó)

---

## Cấu trúc API / các route chính

* Trang chủ (`/`) — dạng GET, hiện form để nhập/bình luận cần phân loại.
* POST route (có thể `/predict` hoặc tương tự) — nhận dữ liệu comment từ form, xử lý (tiền xử lý, lọc, sử dụng mô hình) → trả kết quả phân loại.
* Giao diện hiển thị kết quả phân loại tới người dùng (có thể cùng trang hoặc trang riêng).

---

## Yêu cầu hệ thống

* Python 3.x
* Các thư viện trong `requirements.txt`
---

## Hướng phát triển / mở rộng

Một số ý tưởng để cải thiện app:

* Thêm mô hình machine learning rõ ràng trong repo (nếu chưa có) cùng file weights, hoặc đường dẫn tới mô hình đã train.
* Thêm xử lý tiền xử lý (preprocessing) comment: loại ký tự đặc biệt, chuyển chữ hoa → chữ thường, bỏ stopwords, stemming/lemmatization nếu cần.
* Thêm AJAX hoặc API để có thể gọi từ frontend mà không reload trang.
* Thêm test tự động (unit tests) để kiểm tra chức năng phân loại.
* Triển khai lên server (Heroku, AWS, Render, …) và thêm hướng dẫn deploy.

---

## Cách đóng góp

Nếu bạn muốn đóng góp:

1. Fork repo này.
2. Tạo branch mới cho tính năng hoặc sửa lỗi: `git checkout -b feature-ten-feature`.
3. Làm thay đổi, commit.
4. Gửi Pull Request.
