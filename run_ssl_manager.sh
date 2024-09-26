
#!/bin/bash

# Hiển thị menu
echo "1. Đăng ký SSL cho domain"
echo "2. Gia hạn SSL cho domain"
echo "3. Danh sách domain đã đăng ký SSL thành công"
echo "4. Thoát"
read -p "Chọn một tùy chọn: " choice

# Thiết lập biến môi trường ACTION dựa trên lựa chọn của người dùng
case $choice in
    1)
        export ACTION="register"
        ;;
    2)
        export ACTION="renew"
        ;;
    3)
        export ACTION="list"
        ;;
    4)
        exit 0
        ;;
    *)
        echo "Lựa chọn không hợp lệ. Vui lòng thử lại."
        exit 1
        ;;
esac

# Tải về script Python từ GitHub
curl -O https://raw.githubusercontent.com/080824-vip/dangky-ssl/main/ssl_manager.py

# Chạy script Python
python3 ssl_manager.py
