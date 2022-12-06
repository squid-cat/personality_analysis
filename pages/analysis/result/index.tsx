import { FC, useEffect, useState } from "react";
import { useRouter } from "next/router";
import { IActionUnitDetail } from "@/types";
import { API } from "@/service/API";

const Index: FC = () => {
  const [result, setResult] = useState<IActionUnitDetail[]>([]);

  useEffect(() => {
    const fetch = async () => {
      const res = await API.getAnalysisResult();
      setResult(res?.data || []);
    };
    fetch();
  }, []);

  return (
    <>
      <div>あなたのMBTIタイプは○○です</div>
      <div>AU詳細</div>
      {result.map((r) => {
        return (
          <>
            <div>AU名: {r.name}</div>
            <div>平均値: {r.average}</div>
            <div>中央値: {r.median}</div>
          </>
        );
      })}
    </>
  );
};

export default Index;
