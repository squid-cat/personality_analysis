import { FC, useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useRouter } from "next/router";
import { API } from "@/service/API";

const Index: FC = () => {
  const router = useRouter();
  const intervalRef = useRef<NodeJS.Timer | null>(null);

  const getIsAnalysis = useCallback(async () => {
    const res = await API.getAnalysisProgress();
    if (!(res?.data?.isAnalysis ?? false)) {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
      router.push("/analysis/result");
    }
  }, [router]);

  const fetchProgress = useCallback(() => {
    getIsAnalysis();
  }, [getIsAnalysis]);

  useEffect(() => {
    if (!intervalRef.current) {
      intervalRef.current = setInterval(() => {
        fetchProgress();
      }, 3000);
    }
  }, [fetchProgress]);

  return <div>しばらくお待ちください</div>;
};

export default Index;
