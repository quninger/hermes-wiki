#!/usr/bin/env python3
"""会话归档字数验证脚本
用法: python verify_archive.py <file.md> [--limit N]
规则:
  - 单个子会话 ≤ 500 字
  - 整篇 ≤ 动态上限（默认5000，可指定）
"""
import sys, re

def count_chars(text):
    """去除空白和markdown符号后计数"""
    body = re.sub(r'\s+', '', text)
    body = re.sub(r'[#\-*>|\[\]()]', '', body)
    return len(body)

def split_sections(content):
    """按二级标题拆分为子会话"""
    body = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    sections = re.split(r'(?=^## )', body, flags=re.MULTILINE)
    return [s for s in sections if s.strip()]

def verify(filepath, total_limit=5000):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = split_sections(content)
    total = count_chars(content)
    sub_limit = 500
    all_pass = True

    print(f"文件: {filepath}")
    print(f"整篇字数: {total}/{total_limit}")
    print()

    for i, sec in enumerate(sections):
        title = sec.split('\n')[0].strip('# ').strip()
        chars = count_chars(sec)
        status = "✅" if chars <= sub_limit else "❌"
        if chars > sub_limit:
            all_pass = False
        print(f"  {status} {title}: {chars}/{sub_limit}")

    print()
    if total > total_limit:
        print(f"❌ 整篇 FAIL - 需压缩 {total - total_limit} 字")
        all_pass = False
    elif not all_pass:
        print(f"❌ 子会话 FAIL - 有子会话超过 {sub_limit} 字")
    else:
        print(f"✅ PASS (整篇 {total}/{total_limit}, 子会话均 ≤{sub_limit})")

    return all_pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python verify_archive.py <file.md> [--limit N]")
        sys.exit(1)

    filepath = sys.argv[1]
    limit = 5000
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        limit = int(sys.argv[idx + 1])

    ok = verify(filepath, limit)
    sys.exit(0 if ok else 1)
