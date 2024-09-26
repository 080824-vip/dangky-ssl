
import os

def register_ssl(domain):
    os.system(f"sudo certbot certonly --standalone -d {domain}")

def renew_ssl(domain):
    os.system(f"sudo certbot renew --cert-name {domain}")

def list_ssl():
    os.system("sudo certbot certificates")

def main():
    action = os.getenv('ACTION')
    if action == 'register':
        domain = input("Nhập domain: ")
        register_ssl(domain)
    elif action == 'renew':
        domain = input("Nhập domain (hoặc để trống để gia hạn tất cả): ")
        if domain:
            renew_ssl(domain)
        else:
            os.system("sudo certbot renew")
    elif action == 'list':
        list_ssl()
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
