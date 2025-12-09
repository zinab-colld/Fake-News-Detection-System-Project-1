import re

# كلمات مشهورة في الأخبار الكاذبة
CLICKBAIT_WORDS = [
    "عاجل", "خطير", "لن تصدق", "صدمة", "كارثة", "تحذير", "فضيحة"
]

# مصادر غير موثوقة
UNTRUSTED_SOURCES = [
    "facebook.com", "tiktok.com", "whatsapp.com", "rumor", "blogspot"
]


def clean_text(text):
    """
    تنظيف النص باستخدام NLP بسيطة:
    - إزالة الرموز
    - توحيد المسافات
    - Lowercase
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9أ-ي\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def score_news(title="", text="", source=""):
    """
    تحليل الخبر وإعطاء Score ثم النتيجة:
    Fake / Real / Not Sure
    """

    full_text = (title or "") + " " + (text or "")
    clean = clean_text(full_text)

    score = 0
    reasons = []

    # كشف الكلمات المثيرة
    for word in CLICKBAIT_WORDS:
        if word in full_text:
            score += 15
            reasons.append(f"clickbait_word:{word}")

    # علامات التعجب
    exclam = full_text.count("!")
    if exclam >= 2:
        score += 10
        reasons.append("too_many_exclamation_marks")

    # حروف Capital
    if full_text.isupper():
        score += 10
        reasons.append("all_caps_text")

    # طول النص
    if len(clean.split()) < 25:
        score += 5
        reasons.append("text_too_short")

    # المصدر
    if source:
        for bad in UNTRUSTED_SOURCES:
            if bad in source.lower():
                score += 20
                reasons.append(f"untrusted_source:{source}")

    # تحديد النتيجة
    if score >= 35:
        result = "fake"
    elif score <= 15:
        result = "real"
    else:
        result = "not_sure"

    return {
        "result": result,
        "score": score,
        "reasons": reasons
    }
