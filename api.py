from flask import Flask, request, jsonify
from google_checker import check_with_google_factchecker
from rule_detector import score_news

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """
    نقطة النهاية الرئيسية:
    1) استقبال الخبر
    2) محاولة التحقق من Google
    3) إن فشل → استخدام Rule-Based
    """

    data = request.get_json(force=True)

    title = data.get("title", "")
    text = data.get("text", "")
    source = data.get("source", "")

    if not title and not text:
        return jsonify({"error": "يجب إرسال عنوان أو نص الخبر"}), 400

    # 1) محاولة التحقق من Google
    google_check = check_with_google_factchecker(text or title)

    if google_check:
        return jsonify({
            "result": "verified_by_google",
            "google_data": google_check
        }), 200

    # 2) التحقق الداخلي Rule-Based
    result = score_news(title=title, text=text, source=source)

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
