# dockerに関する操作を定義するもの
import docker 
from docker.models.images import Image # 型定義 Image: https://docker-py.readthedocs.io/en/stable/images.html#image-objects

class Openface:

  def __init__(self) -> None:
    """
    起動時に実行され、以下を実行
    - 定数の定義
    - docker clientと接続をする(docker engineが起動していること)
    - openfaceのコンテナを起動
    """

    # 定数の定義
    self.image_name = "algebr/openface:latest" # openfaceのコンテナ名（最新バージョンを指定） https://hub.docker.com/r/algebr/openface/

    # dockerのclient情報を取得
    try:
      self.client = docker.from_env()
    except Exception as error:
      # エラー時確認事項をコメント
      message_init_error = "====================================================================\n\ndocker情報の取得に失敗しました、以下を確認してください\n\n- docker engineが起動しているか\n\n===================================================================="
      print(message_init_error)
      raise error

    # openfaceのコンテナを起動
    # ターゲットのimageがあるか確認
    if not self.isHaveContainer(self.image_name):
      # 無い場合はコンテナを走らせてimageを作成
      print("imageの新規作成中... (target: {})".format(self.image_name))
      self.client.containers.run(image=self.image_name, remove=True)
      print("imageの作成終了 (target: {})".format(self.image_name))
    

  def getImageList(self) -> list[Image]:
    """
    docker imagesの一覧を取得
    """
    return self.client.images.list()


  def isHaveContainer(self, container_name: str) -> bool:
    """
    対象のコンテナが含まれているか確認
    container_name: 対象のコンテナ名
    """
    for image in self.getImageList():
      if container_name in image.tags:
        return True
    return False
