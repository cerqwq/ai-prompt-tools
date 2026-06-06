# 💡 AI Prompt Tools

AI提示工具，支持提示设计、优化、测试。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 💡 提示设计
- ⚡ 提示优化
- 📝 Few-shot示例
- 🧠 思维链设计
- 🤖 系统提示生成
- 🧪 提示测试

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_prompt_tools import create_tools

tools = create_tools()

# 提示设计
prompt = tools.design_prompt("代码审查", ["简洁", "专业"])

# 提示优化
optimized = tools.optimize_prompt(current_prompt, ["输出不一致"])

# Few-shot示例
examples = tools.generate_few_shot_examples("情感分析", 5)

# 思维链
cot = tools.design_chain_of_thought("数学问题")

# 系统提示
system = tools.generate_system_prompt("代码助手", ["代码审查", "重构"])

# 提示测试
test = tools.test_prompt(prompt, test_cases)
```

## 📁 项目结构

```
ai-prompt-tools/
├── tools.py       # 提示工具核心
└── README.md
```

## 📄 许可证

MIT License
