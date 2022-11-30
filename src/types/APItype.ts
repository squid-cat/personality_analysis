type APIresult = {
  message: string;
};

export type IConnect = APIresult & { data?: { connect: boolean } };
