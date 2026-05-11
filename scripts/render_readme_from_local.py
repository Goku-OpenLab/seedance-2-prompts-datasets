#!/usr/bin/env python3
import json
import re
from datetime import datetime

ROOT_METADATA = "metadata.jsonl"
README_EN = "README.MD"
README_ZH = "README_zh.md"

MARKER_START = "<!-- STATS_START -->"
MARKER_END = "<!-- STATS_END -->"

CDN_BASE = "https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets/resolve/main"


def clean_media_path(p):
    if not p:
        return ""
    while p.startswith("./") or p.startswith("/"):
        p = p[2:] if p.startswith("./") else p[1:]
    return p


def clean_prompt(prompt):
    if prompt is None:
        return ""
    s = re.sub(r"[\r\n]+", " ", str(prompt))
    s = s.replace("|", "\\|")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_jsonl(path):
    items = []
    total = 0
    today_count = 0
    today = datetime.utcnow().strftime("%Y-%m-%d")

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            total += 1
            if item.get("date") == today:
                today_count += 1
            items.append(item)

    return items, total, today_count, today


def render_updates(items):
    latest = items[-15:][::-1]
    blocks = []

    for item in latest:
        item_id = str(item.get("id", ""))
        media = item.get("media") or {}
        spec = item.get("spec") or {}
        i18n = item.get("i18n") or {}
        en = i18n.get("en") or {}

        title = str(en.get("t", "") or "").strip()

        cover = clean_media_path(media.get("c", ""))
        video = clean_media_path(media.get("v", ""))
        prompt = clean_prompt(en.get("p", ""))
        ratio = spec.get("ratio", "")
        duration = spec.get("duration", "")

        cover_url = f"{CDN_BASE}/{cover}" if cover else ""
        video_url = f"{CDN_BASE}/{video}" if video else ""

        slug = str(item.get("slug", "")).strip()
        slug_part = f"{slug}-" if slug else ""
        hub_url = f"https://prompthub.gokuscraper.com/en/seeddance2/prompt/{slug_part}{item_id}"

        heading = title if title else item_id
        block = (
            f"### 🎬 {heading}\n"
            f"<img src=\"{cover_url}\" width=\"480\" alt=\"{item_id}\"><br>\n"
            f"<a href=\"{hub_url}\">🌐 View on Prompt Hub</a>\n\n"
            f"#### 📝 Prompt\n"
            f"```\n{prompt}\n```\n\n"
            f"#### 📌 Details\n"
            f"- Ratio: `{ratio}` | Duration: `{duration}s`\n\n"
            f"---"
        )
        blocks.append(block)

    return "\n\n".join(blocks)


def build_section(total, today_count, today, updates_block):
    return (
        "## 📊 Statistics\n"
        f"- Total Prompts: **{total}**\n"
        f"- Updated Today (UTC {today}): **{today_count}**\n\n"
        "## 🎬 Today's Updates\n"
        f"{updates_block}\n"
    )


def update_readme(path, section):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    if MARKER_START not in content or MARKER_END not in content:
        if content and not content.endswith("\n"):
            content += "\n"
        content += f"\n{MARKER_START}\n{MARKER_END}\n"

    pattern = re.compile(
        re.escape(MARKER_START) + r"[\s\S]*?" + re.escape(MARKER_END)
    )
    replacement = f"{MARKER_START}\n\n{section}\n{MARKER_END}"
    content = pattern.sub(replacement, content, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    items, total, today_count, today = parse_jsonl(ROOT_METADATA)
    updates_block = render_updates(items)
    section = build_section(total, today_count, today, updates_block)

    update_readme(README_EN, section)
    update_readme(README_ZH, section)


if __name__ == "__main__":
    main()
