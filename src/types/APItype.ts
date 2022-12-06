type APIresult = {
  message: string;
};

export type IConnect = APIresult & { data?: { connect: boolean } };

export type IPostResult = APIresult;

export type IAnalysisProgress = APIresult & {
  data?: { isAnalysis: boolean; isResult: boolean };
};
