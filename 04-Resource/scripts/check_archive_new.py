#!/usr/bin/env python3
"""检查指定会话是否有新内容需要归档
用法: python check_archive_new.py <会话标题> <会话时间> [归档目录]
"""
import sys, os, re, glob
from datetime import datetime

def find_session_file(archive_dir, session_title):
    """查找指定会话的归档文件"""
    # 按文件名匹配会话标题
    for f in glob.glob(os.path.join(archive_dir, "*.md")):
        basename = os.path.splitext(os.path.basename(f))[0]
        if session_title in basename:
            return f
    return None

def get_last_archived(filepath):
    """从文件 frontmatter 提取 last_archived"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read(2000)
    m = re.search(r'last_archived:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})', content)
    if m:
        return datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M")
    return None

def check(session_title, session_time_str, archive_dir="98-Archive"):
    """检查会话是否有新内容"""
    try:
        session_time = datetime.strptime(session_time_str, "%Y-%m-%dT%H:%M")
    except:
        print(f"❌ 时间格式错误: {session_time_str}，正确: YYYY-MM-DDTHH:MM")
        return False

    session_file = find_session_file(archive_dir, session_title)

    if session_file is None:
        print(f"📂 会话 [{session_title}] 无归档文件，可新建归档")
        print(f"   文件名: {session_time.strftime('%Y-%m-%d')} {session_title}.md")
        return True

    last = get_last_archived(session_file)
    if last is None:
        print(f"⚠️ 会话文件存在但无时间戳，建议重建")
        return True

    print(f"会话文件: {os.path.basename(session_file)}")
    print(f"上次归档: {last.strftime('%Y-%m-%dT%H:%M')}")
    print(f"当前时间: {session_time_str}")

    if session_time > last:
        delta = session_time - last
        print(f"✅ 有新内容 (新 {delta})")
        return True
    else:
        print(f"⏭️ 无新内容，跳过归档")
        return False

def list_sessions(archive_dir="98-Archive"):
    """列出所有已归档的会话"""
    files = sorted(glob.glob(os.path.join(archive_dir, "*.md")))
    if not files:
        print("📂 归档目录为空")
        return

    print(f"📋 已归档会话 ({len(files)} 个):")
    for f in files:
        basename = os.path.splitext(os.path.basename(f))[0]
        last = get_last_archived(f)
        time_str = last.strftime('%Y-%m-%dT%H:%M') if last else "无时间戳"
        print(f"  {basename} (最后归档: {time_str})")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--list":
        list_sessions()
        sys.exit(0)

    if len(sys.argv) < 3:
        print("用法:")
        print("  python check_archive_new.py <会话标题> <会话时间>")
        print("  python check_archive_new.py --list")
        print("示例:")
        print('  python check_archive_new.py "Obsidian关联确认" 2026-07-04T16:30')
        sys.exit(1)

    session_title = sys.argv[1]
    session_time = sys.argv[2]
    archive_dir = sys.argv[3] if len(sys.argv) > 3 else "98-Archive"

    ok = check(session_title, session_time, archive_dir)
    sys.exit(0 if ok else 1)
