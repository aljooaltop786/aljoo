import requests

# حط التوكن بتاع البوت هنا
TOKEN = "8178136334:AAEZYQvn5AAFtp63T8NRlc8zSI3VEhVCd0g"
# حط الـ chat_id بتاعك (ممكن تجيبه من @userinfobot)
CHAT_ID = "7947593681"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("✅ تم إرسال الرسالة بنجاح!")
    else:
        print("❌ حصل خطأ:", response.text)

# مثال على الإرسال
send_message("مرحبا من بوت تيليجرام بسيط 👋")