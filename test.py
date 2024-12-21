#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 修改导入
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from spark_llm import SparkAPI
from config import *

class RAGHelper:
    def __init__(self):
        """初始化RAG助手"""
        self.text_splitter = RecursiveCharacterTextSplitter(  # 使用RecursiveCharacterTextSplitter
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""]
        )
        # 修改 Embeddings 初始化方式
        try:
            model = SentenceTransformer(EMBEDDING_MODEL)
            self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        except Exception as e:
            logging.error(f"加载Embedding模型失败，尝试使用备用模型: {str(e)}")
            # 使用备用模型
            self.embeddings = HuggingFaceEmbeddings(model_name="shibing624/text2vec-base-chinese")
        
        self.vector_store = None
        self.spark = SparkAPI()
        
    def load_documents(self, file_paths):
        """加载多个txt文档并创建向量存储"""
        documents = []
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    chunks = self.text_splitter.split_text(text)
                    documents.extend(chunks)
            except Exception as e:
                logging.error(f"读取文件 {file_path} 失败: {str(e)}")
                continue
                
        if not documents:
            raise ValueError("没有成功加载任何文档")
            
        # 创建向量存储
        self.vector_store = FAISS.from_texts(
            documents,
            self.embeddings
        )
        logging.info(f"成功加载 {len(documents)} 个文档片段")
        
    def query(self, question, k=4):
        """执行RAG查询"""
        if not self.vector_store:
            raise ValueError("请先加载文档")
            
        # 检索相关文档
        docs = self.vector_store.similarity_search(question, k=k)
        
        # 构建上下文
        context = "\n".join([d.page_content for d in docs])
        
        # 构建prompt
        messages = [{
            "role": "user",
            "content": f"基于以下内容回答问题:\n\n{context}\n\n问题: {question}"
        }]
        
        # 使用讯飞大模型生成答案
        return self.spark.chat(messages)

def chunk(filename, binary=None, lang="Chinese", callback=None, **kwargs):
    """初始化RAG系统"""
    if isinstance(filename, list) and all(f.endswith('.txt') for f in filename):
        rag = RAGHelper()
        rag.load_documents(filename)
        return rag
    else:
        raise ValueError("目前只支持txt格式文件")

if __name__ == "__main__":
    import sys

    def dummy(prog=None, msg=""):
        pass
        
    if len(sys.argv) < 2:
        print("使用示例：")
        print("python test.py 文件路径1 [文件路径2 ...]")
        print("\n或者直接运行 start.py 进行交互式问答")
        sys.exit(1)
        
    chunk(sys.argv[1:], callback=dummy)  # 修改为接收所有参数