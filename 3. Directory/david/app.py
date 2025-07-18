from flask import Flask, request, Response
import os
from io import BytesIO
from gtts import gTTS
#환경 : 외부 패키지 및 모듈 설치(불러오기)

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():
    text = "Hello, DevOps"
    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text,lang,"com").write_to_fp(fp)
    return Response(fp.getvalue(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run('0.0.0.0', 80)