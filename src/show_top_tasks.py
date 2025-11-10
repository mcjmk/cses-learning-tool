import pandas as pd

CSV_PATH = "data/cses.csv"
TOP_N = 10


def main():
    df = pd.read_csv(CSV_PATH)

    if "done" in df.columns:
        df = df[~df["done"].astype(bool)]

    if df.empty or not isinstance(df, pd.DataFrame):
        print("No unsolved problems found")
        return

    top = df.nlargest(TOP_N, "solvers")[["id", "title", "solvers", "url"]].reset_index(
        drop=True
    )

    print(f"Top {TOP_N} most-solved yet unsolved problems:")
    for i, (_, row) in enumerate(top.iterrows(), 1):
        print(f"{i}. {row['title']} — {row['solvers']} solvers")
        print(f"   {row['url']}")
        print()


if __name__ == "__main__":
    main()
