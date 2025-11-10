import pandas as pd

CSV_PATH = "data/cses.csv"
TOP_N = 10


def main():
    df = pd.read_csv(CSV_PATH)

    if "done" in df.columns:
        df = df[~df["done"]]

    df_sorted = df.sort_values("solvers", ascending=False)

    top = df_sorted.head(TOP_N)[["id", "title", "solvers", "url"]]

    print(f"Top {TOP_N} most-solved yet unsolved problems:")
    for i, (_, row) in enumerate(top.iterrows(), 1):
        print(f"{i}. {row['title']} — {row['solvers']} solvers")
        print(f"   {row['url']}")
        print()


if __name__ == "__main__":
    main()
