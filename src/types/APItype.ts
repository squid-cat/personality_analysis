type APIresult = {
  message: string;
};

export type IConnect = APIresult & { data?: { connect: boolean } };

export type IPostResult = APIresult;

export type IAnalysisProgress = APIresult & {
  data?: { isAnalysis: boolean; isResult: boolean };
};

export type IActionUnitDetail = {
  name: string;
  average: number;
  median: number;
};

export type IAnalysisResult = APIresult & { data?: IActionUnitDetail[] };
