import re
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup

HTML_PATH = Path("data/index.html")
OUT_CSV = Path("data/cses.csv")


def parse_html(path: Path):
    with path.open(encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    problems = []

    for li in soup.select("li.task"):
        a = li.find("a")
        if not a:
            continue

        title = a.get_text(strip=True)
        url = a["href"]
        task_id_match = re.search(r"task/(\d+)", str(url))
        task_id = task_id_match.group(1) if task_id_match else url

        # example text: "148105 / 155094"
        detail = li.find("span", class_="detail")
        solved, total = 0, 0
        if detail:
            match = re.search(r"(\d+)\s*/\s*(\d+)", detail.get_text())
            if match:
                solved, total = map(int, match.groups())

        # done?
        score = li.find("span", class_="task-score")
        done = "full" in score["class"] if score else False

        problems.append(
            {
                "id": task_id,
                "title": title,
                "solvers": solved,
                "total": total,
                "url": url,
                "done": done,
            }
        )

    return pd.DataFrame(problems)


def main():
    df = parse_html(HTML_PATH)
    df.sort_values("solvers", ascending=False).to_csv(OUT_CSV, index=False)
    print(f"extracted {len(df)} problems -> {OUT_CSV}")
    done_count = df["done"].sum()
    print(f"you've already solved {done_count} problems!")


if __name__ == "__main__":
    main()
