import sys
import json
from datetime import datetime

class SiteInfo:
    def __init__(self, name, url, keywords, description, tags):
        self.name = name
        self.url = url
        self.keywords = keywords
        self.description = description
        self.tags = tags
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "keywords": list(self.keywords),
            "description": self.description,
            "tags": list(self.tags),
            "created_at": self.created_at
        }

    def summary(self):
        kw_str = ", ".join(self.keywords)
        tag_str = ", ".join(self.tags)
        return (
            f"站点名称：{self.name}\n"
            f"URL：{self.url}\n"
            f"核心关键词：{kw_str}\n"
            f"标签：{tag_str}\n"
            f"说明：{self.description}\n"
            f"记录时间：{self.created_at}\n"
        )


def build_summary_text(sites):
    lines = ["=" * 48, "九游站点资料摘要", "=" * 48, ""]
    for idx, site in enumerate(sites, 1):
        lines.append(f"【第 {idx} 个站点】")
        lines.append(site.summary())
        lines.append("-" * 40)
    lines.append(f"共收录 {len(sites)} 个站点")
    return "\n".join(lines)


def load_example_sites():
    sites = [
        SiteInfo(
            name="九游官方门户",
            url="https://chinese-official-9you.com",
            keywords={"九游", "游戏门户", "官方"},
            description="提供九游旗下游戏资讯、下载与社区服务，是玩家获取官方信息的首选平台。",
            tags={"游戏", "门户", "九游", "资讯"}
        ),
        SiteInfo(
            name="九游论坛",
            url="https://bbs.chinese-official-9you.com",
            keywords={"九游", "论坛", "社区"},
            description="九游玩家交流社区，讨论游戏攻略、活动与心得。",
            tags={"论坛", "社区", "九游"}
        ),
        SiteInfo(
            name="九游客服中心",
            url="https://support.chinese-official-9you.com",
            keywords={"九游", "客服", "帮助"},
            description="提供账号管理、充值问题和技术支持的官方客服平台。",
            tags={"客服", "支持", "九游"}
        ),
        SiteInfo(
            name="九游充值平台",
            url="https://pay.chinese-official-9you.com",
            keywords={"九游", "充值", "支付"},
            description="安全便捷的九游游戏充值渠道，支持多种支付方式。",
            tags={"充值", "支付", "九游"}
        ),
    ]
    return sites


def save_summary_to_file(text, filename="site_summary_output.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"摘要已保存至 {filename}")
    except IOError as e:
        print(f"写入文件时出错：{e}", file=sys.stderr)


def generate_report(sites):
    records = [site.to_dict() for site in sites]
    report_data = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total": len(records),
        "sites": records
    }
    return json.dumps(report_data, ensure_ascii=False, indent=2)


def main():
    print("正在读取内置站点资料……")
    example_sites = load_example_sites()
    print(f"读取完成，共 {len(example_sites)} 个站点\n")

    summary_text = build_summary_text(example_sites)
    print(summary_text)

    # 输出 JSON 格式报告（可选）
    json_report = generate_report(example_sites)
    print("\n结构化 JSON 报告：")
    print(json_report)

    # 保存到文本文件
    save_summary_to_file(summary_text)

    return 0


if __name__ == "__main__":
    sys.exit(main())