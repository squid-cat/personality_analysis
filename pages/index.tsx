import { FC, useEffect } from "react";
import { useRouter } from "next/router";

const Index: FC = () => {
  const router = useRouter();
  useEffect(() => {
    router.push("/register");
  }, [router]);
  return <></>;
};

export default Index;
