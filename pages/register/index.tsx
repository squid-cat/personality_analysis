import { API } from "@/service/API";
import { FC, useEffect, useState } from "react";
import styled from "styled-components";

const Register: FC = () => {
  const [isConnect, setIsConnect] = useState<boolean>();

  // 接続状態のチェック
  const checkConnect = async () => {
    const res = await API.getConnect();
    setIsConnect(res?.data?.connect || false);
  };

  useEffect(() => {
    const fetch = async () => {
      await checkConnect();
    };
    fetch();
  }, []);

  return (
    <Container>
      <ContainerConnectInfo>
        <TextConnectInfo>接続状態:</TextConnectInfo>
        <TextConnectStatus isConnect={isConnect}>
          {isConnect === undefined && "取得中"}
          {isConnect === false && "接続NG"}
          {isConnect === true && "接続OK"}
        </TextConnectStatus>
        <ButtonConnectCheck onClick={() => checkConnect()}>
          再度チェック
        </ButtonConnectCheck>
      </ContainerConnectInfo>
      <TextRegisterInfo>
        動画ファイルを選択して送信ボタンを押してください
      </TextRegisterInfo>
    </Container>
  );
};

export default Register;

const Container = styled.div``;
const ContainerConnectInfo = styled.div`
  margin: 20px 0;
`;

const TextConnectInfo = styled.text``;
const TextConnectStatus = styled.text<{ isConnect?: boolean }>`
  color: ${({ isConnect }) => (isConnect ? "green" : "red")};
`;
const ButtonConnectCheck = styled.button`
  margin: 0 20px;
`;

const TextRegisterInfo = styled.div`
  font-size: 20px;
`;
