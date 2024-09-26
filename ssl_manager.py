
import os

def register_ssl(domain):
    os.system(f"sudo certbot certonly --standalone -d {domain} --http-01-port 8080")

def renew_ssl(domain):
    os.system(f"sudo certbot renew --cert-name {domain}")

def list_ssl():
    os.system("sudo certbot certificates")

def main():
    while True:
        print("1. Đăng ký SSL cho domain")
        print("2. Gia hạn SSL cho domain")
        print("3. Danh sách domain đã đăng ký SSL thành công")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            domain = input("Nhập domain: ")
            register_ssl(domain)
        elif choice == '2':
            domain = input("Nhập domain (hoặc để trống để gia hạn tất cả): ")
            if domain:
                renew_ssl(domain)
            else:
                os.system("sudo certbot renew")
        elif choice == '3':
            list_ssl()
        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
