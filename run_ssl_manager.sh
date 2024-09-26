
#!/bin/bash

# Kiểm tra và cài đặt certbot nếu chưa có
if ! command -v certbot &> /dev/null
then
    echo "certbot chưa được cài đặt. Đang cài đặt certbot..."
    sudo apt-get update
    sudo apt-get install -y certbot
fi

# Hiển thị menu
echo "1. Đăng ký SSL cho domain"
echo "2. Gia hạn SSL cho domain"
echo "3. Danh sách domain đã đăng ký SSL thành công"
echo "4. Thoát"
echo "8. Mở port 8080"
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
    8)
        sudo ufw allow 8080
        echo "Port 8080 đã được mở."
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
