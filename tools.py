"""
AI Prompt Tools - AI提示工具
支持提示设计、优化、测试
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIPromptTools:
    """
    AI提示工具
    支持：设计、优化、测试
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_prompt(self, task: str, constraints: List[str]) -> Dict:
        """设计提示"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        constraints_text = ", ".join(constraints)

        prompt = f"""请为以下任务设计提示：

任务：{task}
约束：{constraints_text}

请返回JSON格式：
{{
    "system_prompt": "系统提示",
    "user_prompt_template": "用户提示模板",
    "variables": ["变量"],
    "examples": ["示例"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"prompt": content}

    def optimize_prompt(self, current_prompt: str, issues: List[str]) -> Dict:
        """优化提示"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        issues_text = ", ".join(issues)

        prompt = f"""请优化以下提示：

当前提示：{current_prompt[:500]}
问题：{issues_text}

请返回JSON格式：
{{
    "optimized_prompt": "优化后的提示",
    "improvements": ["改进点"],
    "expected_results": "预期效果"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def generate_few_shot_examples(self, task: str, count: int = 3) -> List[Dict]:
        """生成Few-shot示例"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为{task}生成{count}个Few-shot示例：

请返回JSON格式：
[
    {{"input": "输入", "output": "输出", "explanation": "解释"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"examples": content}]

    def design_chain_of_thought(self, task: str) -> Dict:
        """设计思维链"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{task}设计思维链提示：

请返回JSON格式：
{{
    "cot_prompt": "思维链提示",
    "steps": ["推理步骤"],
    "examples": ["示例"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"chain_of_thought": content}

    def generate_system_prompt(self, role: str, capabilities: List[str]) -> str:
        """生成系统提示"""
        if not self.client:
            return "LLM客户端未配置"

        caps_text = ", ".join(capabilities)

        prompt = f"""请为{role}生成系统提示：

能力：{caps_text}

要求：
1. 角色定义
2. 行为规范
3. 输出格式
4. 约束条件"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def test_prompt(self, prompt: str, test_cases: List[Dict]) -> Dict:
        """测试提示"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        cases_text = json.dumps(test_cases[:5], ensure_ascii=False)

        prompt_text = f"""请测试以下提示：

提示：{prompt[:500]}
测试用例：{cases_text}

请返回JSON格式：
{{
    "results": [
        {{"input": "输入", "expected": "预期", "actual": "实际", "pass": true/false}}
    ],
    "pass_rate": "通过率"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"test_results": content}


def create_tools(**kwargs) -> AIPromptTools:
    """创建提示工具"""
    return AIPromptTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Prompt Tools")
    print()

    # 测试
    prompt = tools.design_prompt("代码审查", ["简洁", "专业"])
    print(json.dumps(prompt, ensure_ascii=False, indent=2))
