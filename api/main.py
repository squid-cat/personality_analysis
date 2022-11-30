import os
import atexit

# api周辺のライブラリ
from flask import Flask, jsonify, request

# 独自ライブラリのimport
import docker_openface

app = Flask(__name__)
currentPath = os.getcwd()

# openfaceのインストラクタ作成
openface = docker_openface.Openface()
openface.start()

@app.route("/test", methods=["GET"])
def getTest():
  return jsonify({"message": "hello world!"}), 200

@app.route("/movie", methods=["POST"])
def postMovie():

  # ファイルがなかった場合、2つ以上の場合
  if len(request.files) == 0:
    return jsonify({"message": "Could not found files."}), 400
  elif len(request.files) > 1:
    return jsonify({"message": "Only one file can be sent."}), 400

  if 'file' not in request.files:
    return jsonify({"message": "Could not found send name \"file\"."}), 400

  # データの取り出し
  upload_file = request.files['file']

  # 拡張子が動画ファイルでない場合
  if not upload_file.filename.endswith(".mp4"):
    return jsonify({"message": "Not a video file."}), 400

  # 動画をアップロード
  upload_file.save(currentPath + "/api/data/input.mp4")
  # dockerに転送
  openface.copyToDocker(currentPath + "/api/data/input.mp4")
  return jsonify({"message": "Success uploaded."}), 200


# 終了時に必ず実行
@atexit.register
def exeStop():
  openface.stop()


app.run()
