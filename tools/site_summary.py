import json
from datetime import datetime

class SiteProfile:
    def __init__(self, name, url, tags, description, keywords):
        self.name = name
        self.url = url
        self.tags = tags
        self.description = description
        self.keywords = keywords
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "tags": self.tags,
            "description": self.description,
            "keywords": self.keywords,
            "created_at": self.created_at
        }

    def formatted_summary(self):
        tag_line = " | ".join(self.tags)
        kw_line = ", ".join(self.keywords)
        lines = []
        lines.append("=" * 50)
        lines.append(f"站点名称   : {self.name}")
        lines.append(f"URL        : {self.url}")
        lines.append(f"标签       : {tag_line}")
        lines.append(f"关键词     : {kw_line}")
        lines.append(f"简介       : {self.description}")
        lines.append(f"生成时间   : {self.created_at}")
        lines.append("=" * 50)
        return "\n".join(lines)

def load_builtin_data():
    profiles = []
    data_list = [
        {
            "name": "爱游戏",
            "url": "https://cnweb-i-game.com.cn",
            "tags": ["游戏", "娱乐", "互动平台"],
            "description": "提供丰富在线游戏和互动体验的综合游戏平台，覆盖多种类型与受众。",
            "keywords": ["爱游戏", "在线游戏", "网页游戏"]
        },
        {
            "name": "游戏天地",
            "url": "https://example-game-world.com",
            "tags": ["单机", "攻略", "社区"],
            "description": "专注单机游戏评测、攻略与玩家社区交流。",
            "keywords": ["游戏天地", "单机游戏", "攻略"]
        },
        {
            "name": "电竞前线",
            "url": "https://esports-frontline.cn",
            "tags": ["电竞", "赛事", "直播"],
            "description": "实时追踪国内外电竞赛事，提供赛程、数据与直播聚合。",
            "keywords": ["电竞前线", "电子竞技", "赛事"]
        }
    ]
    for item in data_list:
        p = SiteProfile(
            name=item["name"],
            url=item["url"],
            tags=item["tags"],
            description=item["description"],
            keywords=item["keywords"]
        )
        profiles.append(p)
    return profiles

def generate_summary_report(profiles):
    report_lines = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines.append(f"站点摘要报告  ({timestamp})")
    report_lines.append("")
    for idx, profile in enumerate(profiles, 1):
        report_lines.append(f"--- 站点 {idx} ---")
        report_lines.append(profile.formatted_summary())
        report_lines.append("")
    report_lines.append("报告结束")
    return "\n".join(report_lines)

def export_to_json(profiles, filepath="site_profiles.json"):
    data = []
    for p in profiles:
        data.append(p.to_dict())
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return filepath

def main():
    print("正在加载内置站点资料...")
    site_list = load_builtin_data()
    print(f"共加载 {len(site_list)} 个站点资料。\n")

    print("生成结构化摘要：")
    summary = generate_summary_report(site_list)
    print(summary)

    json_path = export_to_json(site_list)
    print(f"\nJSON 数据已导出至: {json_path}")

    print("\n--- 演示：单个站点摘要 ---")
    demo = site_list[0]
    print(demo.formatted_summary())

if __name__ == "__main__":
    main()