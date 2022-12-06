import pandas as pd

AU_COLUMNS = [" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r"," AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]

def __openResultCsv(filePath: str) -> pd.DataFrame | None:
  data = pd.read_csv(filePath)
  return data 

def getAUdataFromCsv(filePath: str) -> list:
  global AU_COLUMNS

  data = __openResultCsv(filePath)
  AU_result = [] 
  
  # ファイルが開けなかった場合は空を返す
  if data is None:
    return []

  for targetAU in AU_COLUMNS:
    target_data = data[targetAU]
    data_format = {"name": targetAU, "average": target_data.mean(), "median": target_data.median()}
    AU_result.append(data_format)

  return AU_result
