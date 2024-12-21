import logging
import os
from test import chunk
import config

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 改回 INFO 级别，让输出更清晰
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    # 检查文件路径
    files = [
        r'G:\MasteringRAG-main\111梅花易数白话解 (（宋）邵雍著；刘光本，荣益译) (Z-Library).txt'
    ]
    
    # 验证文件存在
    missing_files = [f for f in files if not os.path.exists(f)]
    if missing_files:
        print("\n❌ 错误：以下文件不存在：")
        for f in missing_files:
            print(f"   - {f}")
        print("\n请确保文件路径正确，或修改 start.py 中的文件路径")
        return

    try:
        print("\n正在初始化系统...")
        print("1. 加载文档...")
        rag = chunk(files)
        print("2. 文档加载完成")
        print("3. 系统初始化成功！")
        
        print("\n" + "="*50)
        print("欢迎使用RAG文档问答系统")
        print("提示：")
        print("- 输入问题并按回车发送")
        print("- 输入'q'退出程序")
        print("="*50 + "\n")
        
        while True:
            question = input("\n🤔 请输入问题: ")
            if question.lower() == 'q':
                print("\n感谢使用，再见！")
                break
                
            try:
                print("\n🤖 正在思考...")
                answer = rag.query(question, k=config.TOP_K)
                print(f"\n📝 回答: {answer}\n")
            except Exception as e:
                logging.error(f"处理问题时出错: {str(e)}")
                print("\n❌ 抱歉，处理问题时出现错误，请重试。")
            
    except Exception as e:
        logging.error(f"系统错误: {str(e)}")
        print(f"\n系统启动失败: {str(e)}")

if __name__ == "__main__":
    main()