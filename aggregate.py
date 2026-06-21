import requests
import json

# یکی از سورس‌های فعال که آی‌پی‌های کلودفلر را بر اساس پینگ ایران آپدیت می‌کند
# در صورت نیاز در آینده به راحتی می‌توانی سورس‌های جدیدی به این لیست اضافه کنی
SOURCES = [
    "https://raw.githubusercontent.com/ircfspace/cf2dns/master/list/ipv4.json"
]

def update_my_ips():
    print("⏳ Fetching IPs from active sources...")
    my_clean_ips = {"mci": [], "mtn": [], "mkh": []}
    
    try:
        # دریافت دیتا از سورس فعال
        response = requests.get(SOURCES[0], timeout=15)
        response.raise_for_status()
        
        # فرض می‌کنیم دیتای این سورس یک لیست ساده از آی‌پی‌ها یا جیسون است
        # سایت cf2dns معمولا آی‌پی‌های برتر را لیست می‌کند
        data = response.json()
        
        # استخراج آی‌پی‌ها (در اینجا به عنوان نمونه برای همراه اول)
        if isinstance(data, list):
            for item in data[:10]: # ۱۰ آی‌پی برتر
                if "ip" in item:
                    my_clean_ips["mci"].append(item["ip"])
        
        # ذخیره خروجی در یک فایل اختصاصی برای خودت
        with open("my-clean-ips.json", "w", encoding="utf-8") as f:
            json.dump(my_clean_ips, f, indent=4)
            
        print("✅ my-clean-ips.json created successfully!")
        
    except Exception as e:
        print(f"❌ Error during update: {e}")

if __name__ == "__main__":
    update_my_ips()
