from flask import Flask, request, jsonify
from scipy.io.wavfile import read, write
import numpy as np
import io, datetime
          
app = Flask (__name__)

def dump_pcm(f, d):
    write(f, 16000, d.astype(np.int16))

@app.route('/dump', methods= ['GET', 'POST'])
def stt():
    headers = request.headers
    auth = headers.get("Api-Key")

    # 리퀘스트 확인
    if auth != "YWRtaW46YnJhMW5zb2Z0ZG90YSE=":
        return jsonify({"message": "not Authorized"}), 401 
    elif not('POST' in request.method):
        return jsonify({"message": f"use POST method [{request.method}]"}), 401 

    if 'file' not in request.files:
        return jsonify({"message": "no file"}), 401 

    file = request.files['file']
    filename = file.filename

    # pcm 혹은 wav 대응
    if not ('wav' in filename.split('.')[-1] or 
            'pcm' in filename.split('.')[-1]):
        return jsonify({"message": "pcm or wav are allowed"}), 401 
    
    upload_filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%fff')}.pcm"
    print(upload_filename)

    byte_input = file.stream.read()

    if 'wav' in filename.split('.')[-1]:
        print('WAV processing')
        rate, int_audio = read(io.BytesIO(byte_input))
        audio = int_audio / 32767.

    if 'pcm' in filename.split('.')[-1]:
        print('PCM processing')
        int_audio = np.fromstring(byte_input, "int16")
        audio = int_audio / 32767.

    dump_pcm(upload_filename, int_audio)

    return jsonify({"message": f"save done at {upload_filename}"}) 

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=2193)
