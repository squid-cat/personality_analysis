import sys

# 独自ライブラリのimport
import docker_openface

def main():
  try:
    # openfaceのインストラクタ作成
    openface = docker_openface.Openface()
    openface.start()
    
    while True:
      pass
  
  finally:
    # 処理終了時に必ず実行
    openface.stop()
    pass

if __name__ == "__main__":
    sys.exit(main())
