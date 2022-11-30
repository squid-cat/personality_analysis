import { FC, useEffect } from 'react';
import { useRouter } from 'next/router';

const Index: FC = () => {
  const router = useRouter();
  useEffect(() => {
    router.push("/register");
  }, []);
  return <></>;
}

export default Index;
