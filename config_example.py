import os

# OpenAI API配置
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # 请填写您的OpenAI API密钥
OPENAI_API_BASE = "https://api.openai.com/v1"  # OpenAI官方API地址
# 如果使用代理，可以修改为其他地址，例如:
# OPENAI_API_BASE = "https://your-proxy-url/v1"

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE

# 讯飞API配置
SPARK_APP_ID = "YOUR_SPARK_APP_ID"  # 请填写您的讯飞APP ID
SPARK_API_KEY = "YOUR_SPARK_API_KEY"  # 请填写您的讯飞API密钥
SPARK_API_SECRET = "YOUR_SPARK_API_SECRET"  # 请填写您的讯飞API秘密
# 使用精调后的模型接口
SPARK_API_URL = "wss://spark-api.xf-yun.com/v4.0/chat"

# Embedding配置
EMBEDDING_MODEL = "shibing624/text2vec-base-chinese"  # 使用完整的模型标识符

# RAG配置
CHUNK_SIZE = 1000  # 文档分块大小
CHUNK_OVERLAP = 200  # 分块重叠部分
TOP_K = 4  # 检索相关文档数量

# 模型配置
MODEL_NAME = "YOUR_MODEL_NAME"  # 使用的OpenAI模型
TEMPERATURE = 0.7  # 生成温度
