import { IAnalysisProgress, IConnect, IPostResult } from "@/types";
import axios from "axios";

const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

const axiosInstance = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Content-Type": "application/json",
  },
});

// [GET] API接続テスト
const getConnect = () => {
  const res = axiosInstance
    .get<IConnect>("/connect")
    .then((res) => res.data)
    .catch((e) => {
      console.error(e);
      return null;
    });
  return res;
};

// [POST] 解析する動画をpost
const postMovie = (file: File) => {
  const params = new FormData();
  params.append("file", file);
  const res = axiosInstance
    .post<IPostResult>("/movie", params, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .catch((e) => {
      console.error(e);
      return null;
    });
  return res;
};

// [GET] 分析進捗を取得する
const getAnalysisProgress = () => {
  const res = axiosInstance
    .get<IAnalysisProgress>("/analysis/progress")
    .then((res) => res.data)
    .catch((e) => {
      console.error(e);
      return null;
    });
  return res;
};

export const API = {
  getConnect,
  postMovie,
  getAnalysisProgress,
};
