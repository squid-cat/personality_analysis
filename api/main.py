import os
import atexit

# api周辺のライブラリ
from flask import Flask, jsonify, request
from flask_cors import CORS

# 独自ライブラリのimport
import docker_openface
import AU_analysis

app = Flask(__name__)
CORS(app)
currentPath = os.getcwd()

# openfaceのインストラクタ作成
openface = docker_openface.Openface()
openface.start()

# [GET] 接続テスト
@app.route("/connect", methods=["GET"])
def getTest():
  return jsonify({"message": "ok",
                  "data": {"connect": True}}), 200
  
# [POST] 動画をアップロードする
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
  # 解析を実行
  openface.exeAnalysis()
  return jsonify({"message": "Success uploaded."}), 200

# [GET] 進捗確認をする
@app.route("/analysis/progress", methods=["GET"])
def getAnalysisProgress():
  return jsonify({"message": "ok",
                  "data": {"is_analysis": openface.isAnalysis, "is_result": openface.isResult}}), 200

# [GET] 判定結果を返却する
@app.route("/analysis/result", methods=["GET"])
def getAnalysisResult():
  # ファイルを取得する
  openface.getResultFile(currentPath + "/api/data")

  # AUの分析を行う

  return jsonify({"message": "ok"}), 200

@app.after_request
def afterRequest(res):
  res.headers['Access-Control-Allow-Headers'] = '*'
  return res

# 終了時に必ず実行
@atexit.register
def exeStop():
  openface.stop()


app.run()
