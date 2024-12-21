from config import *
import logging

logging.basicConfig(level=logging.INFO)

def test_config():
    """测试API配置是否正确"""
    logging.info("-" * 50)
    logging.info("讯飞API配置信息:")
    logging.info(f"APP_ID: {SPARK_APP_ID}")
    logging.info(f"API_KEY: {SPARK_API_KEY[:5]}...")
    logging.info(f"API_SECRET: {SPARK_API_SECRET[:5]}...")
    logging.info(f"API_URL: {SPARK_API_URL}")
    logging.info("-" * 50)
    
    # 验证配置有效性
    if not all([SPARK_APP_ID, SPARK_API_KEY, SPARK_API_SECRET, SPARK_API_URL]):
        raise ValueError("讯飞API配置不完整")
    
    # 检查URL格式
    if not SPARK_API_URL.startswith("wss://"):
        raise ValueError("API_URL 必须以 wss:// 开头")
        
    logging.info("配置验证通过！")

if __name__ == "__main__":
    test_config()
