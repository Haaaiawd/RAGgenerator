from spark_llm import SparkAPI
import logging

logging.basicConfig(level=logging.DEBUG)

def test_signature():
    """测试API签名生成"""
    spark = SparkAPI()
    url = spark._generate_url()
    
    print("\n" + "="*50)
    print("生成的URL:")
    print(url)
    print("="*50 + "\n")
    
    # 解析并显示各个组成部分
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    
    print("URL组成部分:")
    print(f"协议: {parsed.scheme}")
    print(f"域名: {parsed.netloc}")
    print(f"路径: {parsed.path}")
    print("\n参数:")
    for key, value in params.items():
        print(f"{key}: {value[0]}")

if __name__ == "__main__":
    test_signature()
