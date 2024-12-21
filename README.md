# MasteringRAG

本项目包含一个基于 RAG (Retrieval-Augmented Generation) 的文档问答系统，可通过星火 API 或 OpenAI API 进行问答。

## 功能概述
- 支持将本地 txt 文件切分后向量化，并进行检索+问答
- 基于 Flask 提供简单 Web 服务（可选）
- Docker 化部署与远程访问

## 快速开始

1. 克隆或下载本项目:
   ```
   git clone https://github.com/yourusername/MasteringRAG.git
   ```
   或通过下载ZIP方式获取并解压。

2. 安装依赖:
   ```
   pip install -r requirements.txt
   ```

3. 修改配置:
   - 在 `config.py` 文件中配置你的 OpenAI API Key 或其他自定义配置

4. 本地运行:
   ```
   python start.py
   ```
   即可在本地环境中加载文档并与系统交互。

## Web 服务 (Flask)
如需对外提供 HTTP 服务，可使用 `server.py` (需要先创建并实现简单 Flask 路由，可以参考之前的示例).

## Docker 部署

1. 构建镜像:
   ```
   docker build -t masteringrag:latest .
   ```

2. 运行容器:
   ```
   docker run -d -p 8000:8000 masteringrag:latest
   ```

3. 访问服务:
   - 若在本地，访问 http://localhost:8000
   - 若在远程服务器，用服务器 IP + 端口访问

## 目录结构 (简要)
- `start.py`：主程序入口，可进行交互式问答
- `test.py`：加载文档和处理分块逻辑
- `spark_llm.py`：调用星火大模型的逻辑
- `config.py`：全局配置文件
- `requirements.txt`：依赖文件
- `Dockerfile`：构建 Docker 镜像的描述文件

## 注意事项
- 请确保使用前已在 `config.py` 中填写有效的 API Key
- 若需要自定义模型与其他高级功能，可按需调整各文件中的代码
- 如需远程文件存取或其他安全配置，务必保证服务器防火墙与端口已正确开放

