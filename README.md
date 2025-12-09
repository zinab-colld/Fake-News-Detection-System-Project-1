[google_checker.py](https://github.com/user-attachments/files/24059834/google_checker.py)
import requests
from config import GOOGLE_API_KEY

def check_with_google_factchecker(query):
    """
    إرسال نص الخبر إلى Google Fact Check Tools API
    والعودة بنتيجة التحقق إذا كانت موجودة.
    """
    
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    params = {
        "query": query,
        "key": GOOGLE_API_KEY
    }

    # إرسال الطلب
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    # لو مفيش Claims → يبقى مفيش خبر مشابه
    if "claims" not in data or len(data["claims"]) == 0:
        return None

    return data["claims"]
