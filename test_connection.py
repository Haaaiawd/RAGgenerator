import websocket
import ssl
from urllib.parse import urlparse
from config import SPARK_API_URL
import logging

logging.basicConfig(level=logging.DEBUG)
websocket.enableTrace(True)

def test_connection():
    """测试与讯飞API的WebSocket连接"""
    url = urlparse(SPARK_API_URL)
    test_url = f"wss://{url.netloc}"
    
    try:
        ws = websocket.create_connection(
            test_url,
            sslopt={"cert_reqs": ssl.CERT_NONE},
            timeout=10
        )
        logging.info("WebSocket连接测试成功！")
        ws.close()
    except Exception as e:
        logging.error(f"连接测试失败: {str(e)}")

if __name__ == "__main__":
    test_connection()
