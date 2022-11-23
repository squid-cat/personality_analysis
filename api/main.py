import sys
import time

# 独自ライブラリのimport
import docker_openface

def main():
  try:
    # openfaceのインストラクタ作成
    openface = docker_openface.Openface()
    openface.start()
    openface.copyToDocker("./api/data/input.mp4")
    
    # TEST: 5秒停止
    time.sleep(5)
  
  finally:
    # 処理終了時に必ず実行
    openface.stop()
    pass

if __name__ == "__main__":
    sys.exit(main())
