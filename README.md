# CSES Learning Tool

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A simple Python script to sort unsolved CSES problems by popularity, helping you learn more effectively by recommending [CSES Problem Set](https://cses.fi/problemset/) problems based on popularity (which correlates with difficulty and importance).

## Why This Tool?

Reduce decision fatigue and avoid wasting time on obscure niche algorithms when you should be building fundamentals first. CSES lacks this essential sorting feature.

## Features

- Parse your CSES problem set progress
- Get top N most-solved problems you haven't completed yet

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

### Using uv (recommended)

```bash
# Clone the repository
git clone https://github.com/mcjmk/cses-learning-tool.git
cd cses-learning-tool

# Install dependencies
uv sync

# Activate the environment (optional, uv run handles this)
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Using pip

```bash
pip install -r requirements.txt
# Note: You'll need to generate requirements.txt from pyproject.toml
```

## Setup

1. **Get your CSES problem set HTML:**
   - Go to [CSES Problem Set](https://cses.fi/problemset/)
   - Log in
   - Save the page as `data/index.html` (Right-click → Save As → index.html)

2. **Parse your data:**
   ```bash
   uv run python src/html_parser.py
   ```
   This creates `data/cses.csv` with all problems and your progress.

## Usage

### Get problem recommendations

```bash
uv run python src/show_top_tasks.py
```

This shows the top 10 most-solved problems that you haven't completed yet, along with their URLs.

**Example output:**
```
Top 10 most-solved yet unsolved problems:
1. Apartments — 53476 solvers
   https://cses.fi/problemset/task/1084

2. Concert Tickets — 48903 solvers
   https://cses.fi/problemset/task/1091

...
```

### Customize

Edit constants in `src/show_top_tasks.py`:
- `TOP_N = 10` - Change number of recommendations
- `CSV_PATH = "data/cses.csv"` - Change data location

## Project Structure

```
cses-learning-tool/
├── src/
│   ├── html_parser.py      # Parses CSES HTML → CSV
│   ├── show_top_tasks.py   # Shows top unsolved problems
│   └── main.py             # Placeholder for future features
├── data/
│   ├── index.html          # Your CSES problem set page (YOU provide this)
│   └── cses.csv            # Generated from index.html
├── pyproject.toml          # Dependencies & config
└── README.md
```

## Development

```bash
# Install dev dependencies
uv sync --dev

# Run linter
uv run ruff check src/

# Run type checker
uv run pyright

# Install pre-commit hooks
uv run pre-commit install
```

## Roadmap / Future Ideas

- [ ] Web scraping automation (no manual HTML saving)
- [ ] Progress visualization

## Contributing

This is an alpha-stage project, but contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

MIT License - see LICENSE file

## Acknowledgments

- [CSES Problem Set](https://cses.fi/) by Antti Laaksonen

---

*Note: Alpha version, things will change*
