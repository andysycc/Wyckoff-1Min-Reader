def main():
    # 确保目录存在
    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # === 修改点：优先读取 stock_list.txt ===
    symbols = []
    
    # 1. 尝试读取仓库里的文件
    if os.path.exists("stock_list.txt"):
        print("📂 发现 stock_list.txt，正在读取持仓列表...")
        try:
            with open("stock_list.txt", "r", encoding="utf-8") as f:
                # 读取每一行，去除空格和换行符，且过滤掉空行
                lines = f.readlines()
                symbols = [line.strip() for line in lines if line.strip() and not line.startswith("#")]
        except Exception as e:
            print(f"   [Error] 读取 stock_list.txt 失败: {e}")

    # 2. 如果文件没找到或为空，回退到使用环境变量 SYMBOLS
    if not symbols:
        print("⚠️ 未找到文件或文件为空，尝试读取环境变量 SYMBOLS...")
        symbols_env = os.getenv("SYMBOLS", "600970")
        symbols = [s.strip() for s in symbols_env.split(",") if s.strip()]

    # 去重
    symbols = list(set(symbols))
    
    print(f"📋 最终待处理股票列表 ({len(symbols)}只): {symbols}")

    if not symbols:
        print("❌ 没有找到任何股票代码，程序结束。")
        return

    # 开始循环处理
    for i, symbol in enumerate(symbols):
        try:
            process_one_stock(symbol)
        except Exception as e:
            print(f"❌ {symbol} 发生严重错误: {e}")
        
        # 除非是最后一个，否则休息一下
        if i < len(symbols) - 1:
            wait_sec = 10
            print(f"⏳ 休息 {wait_sec} 秒...")
            time.sleep(wait_sec)

if __name__ == "__main__":
    main()
