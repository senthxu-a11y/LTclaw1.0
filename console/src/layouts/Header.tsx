import { Layout, Space } from "antd";
import { useEffect, useState } from "react";
import LanguageSwitcher from "../components/LanguageSwitcher/index";
import ThemeToggleButton from "../components/ThemeToggleButton";
import styles from "./index.module.less";
import api from "../api";
import { useTheme } from "../contexts/ThemeContext";

const { Header: AntHeader } = Layout;

export default function Header() {
  useTheme();
  const [version, setVersion] = useState<string>("");

  useEffect(() => {
    api
      .getVersion()
      .then((res) => setVersion(res?.version ?? ""))
      .catch(() => {});
  }, []);

  return (
    <AntHeader className={styles.header}>
      <div className={styles.logoWrapper}>
        <span className={styles.logoText}>LTCLAW-GY.X</span>
        {version && (
          <>
            <div className={styles.logoDivider} />
            <span className={styles.logoVersion}>v{version}</span>
          </>
        )}
      </div>
      <Space size="middle">
        <LanguageSwitcher />
        <ThemeToggleButton />
      </Space>
    </AntHeader>
  );
}
