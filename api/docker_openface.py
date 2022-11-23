# dockerに関する操作を定義するもの
import docker
import os
import tarfile

# 型定義
# Image: https://docker-py.readthedocs.io/en/stable/images.html#image-objects
# Model: 
from docker.models.images import Image
from docker.models.containers import Container

class Openface:

  def __init__(self) -> None:
    """
    起動時に実行され、以下を実行
    - 定数の定義
    - docker clientと接続をする(docker engineが起動していること)
    - openfaceのコンテナを起動
    """

    # 定数の定義
    self.image_name = "algebr/openface:latest" # openfaceのimage名（最新バージョンを指定） https://hub.docker.com/r/algebr/openface/

    # dockerのclient情報を取得
    try:
      self.client = docker.from_env()
    except Exception as error:
      # エラー時確認事項をコメント
      message_init_error = "====================================================================\n\ndocker情報の取得に失敗しました、以下を確認してください\n\n- docker engineが起動しているか\n\n===================================================================="
      print(message_init_error)
      raise error

    # ターゲットのimageがあるか確認
    if not self.isHaveImage(self.image_name):
      # 無い場合はコンテナを走らせてimageを作成
      self.createImage(self.image_name)
      
    return

  def start(self) -> None:
    """
    openfaceを起動する
    - コンテナを作成し起動する
    """
    self.container_openface = self.createContainer()
    self.container_openface.start()
    return 


  def stop(self) -> None:
    """
    openfaceを停止する
    - コンテナを停止して削除する
    """
    self.container_openface.stop()
    self.container_openface.remove()
    return

  def copyToDocker(self, src: str) -> None:
    """
    localからコンテナへファイルをコピーする
    """
    # tar形式に変換
    os.chdir(os.path.dirname(src))
    srcname = os.path.basename(src)

    with tarfile.open("copy.tar", 'w') as tar:
      try:
        tar.add(srcname)
      finally:
        tar.close()

    with open('copy.tar', 'rb') as fd:
      ok = self.container_openface.put_archive(path="/home/openface-build", data=fd)
      if not ok:
        raise Exception('ファイルコピーに失敗しました ({} -> {}:/home/openface-build)'.format(src, self.container_openface.short_id))
      else:
        print("{} -> {}:/home/openface-build にコピーしました".format(src, self.container_openface.short_id))
    
    return


  def createContainer(self) -> Container:
    """
    コンテナを作成する
    """
    return self.client.containers.create(self.image_name, detach=True, tty=True)


  def getImageList(self) -> list[Image]:
    """
    docker imagesの一覧を取得
    """
    return self.client.images.list()


  def isHaveImage(self, image_name: str) -> bool:
    """
    対象のimageが含まれているか確認
    image_name: 対象のコンテナ名
    """
    for image in self.getImageList():
      if image_name in image.tags:
        return True
    return False


  def createImage(self, image_name: str) -> None:
    """
    imageを取得・作成
    """
    print("imageの新規作成中... (target: {})".format(image_name))
    self.client.containers.run(image=image_name, remove=True)
    print("imageの作成終了 (target: {})".format(image_name))
    return
