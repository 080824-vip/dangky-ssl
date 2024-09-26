
import os
import requests

def register_ssl(domain, api_token, zone_id):
    def add_txt_record(domain, txt_value):
        url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        data = {
            "type": "TXT",
            "name": f"_acme-challenge.{domain}",
            "content": txt_value,
            "ttl": 120
        }
        response = requests.post(url, json=data, headers=headers)
        return response.status_code == 200

    import time
    import random
    import string

    # Tạo giá trị ngẫu nhiên cho bản ghi TXT
    txt_value = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    if add_txt_record(domain, txt_value):
        print("Đã thêm bản ghi TXT. Chờ 60 giây để DNS cập nhật...")
        time.sleep(60)  # Chờ 60 giây để DNS cập nhật
        os.system(f"sudo certbot certonly --manual --preferred-challenges dns -d {domain} --manual-auth-hook 'python3 /home/user/dangky-ssl/add_txt_record.py {domain} {txt_value} {api_token} {zone_id}'")
    else:
        print("Failed to add TXT record to Cloudflare.")

def renew_ssl(domain):
    os.system(f"sudo certbot renew --cert-name {domain}")

def list_ssl():
    os.system("sudo certbot certificates")

def main():
    api_token = input("Nhập API Token của Cloudflare: ")
    zone_id = input("Nhập Zone ID của Cloudflare: ")
    
    while True:
        print("1. Đăng ký SSL cho domain")
        print("2. Gia hạn SSL cho domain")
        print("3. Danh sách domain đã đăng ký SSL thành công")
        print("4. Thoát")
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            domain = input("Nhập domain: ")
            register_ssl(domain, api_token, zone_id)
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
