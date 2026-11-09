"""Reproduce the stationery-sales teaching analysis using Python 3.

All records in sales.csv are fictional.
Run from this folder with: python analyze.py

The script creates:
- monthly_summary.csv
- analysis_report.md
- sales_chart.svg

Only Python's standard library is required.
"""

import csv
from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    monthly = defaultdict(lambda: [0, Decimal("0")])
    seen = set()

    # Read and validate the source data.
    with (ROOT / "sales.csv").open(
        newline="", encoding="utf-8"
    ) as source:
        reader = csv.DictReader(source)

        expected_columns = [
            "month",
            "product",
            "units_sold",
            "unit_price_ngn",
        ]
        if reader.fieldnames != expected_columns:
            raise ValueError(
                f"Unexpected CSV columns. Expected: {expected_columns}"
            )

        for row in reader:
            month = row["month"]
            product = row["product"].strip()

            # Check that the month uses YYYY-MM format.
            if (
                datetime.strptime(month, "%Y-%m").strftime("%Y-%m")
                != month
                or not product
            ):
                raise ValueError("Invalid month or empty product name.")

            key = (month, product)
            if key in seen:
                raise ValueError(
                    f"Duplicate monthly product record: {key}"
                )
            seen.add(key)

            units = int(row["units_sold"])
            price = Decimal(row["unit_price_ngn"])

            if units < 0 or not price.is_finite() or price < 0:
                raise ValueError(
                    "Units and unit price must be nonnegative "
                    "finite values."
                )

            monthly[month][0] += units
            monthly[month][1] += units * price

    if not monthly:
        raise ValueError("The sales.csv dataset is empty.")

    months = sorted(monthly)

    # Write the monthly summary CSV.
    with (ROOT / "monthly_summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as destination:
        writer = csv.writer(destination)
        writer.writerow(["month", "units_sold", "revenue_ngn"])

        for month in months:
            units, revenue = monthly[month]
            writer.writerow([month, units, f"{revenue:.2f}"])

    first_units = monthly[months[0]][0]
    last_units = monthly[months[-1]][0]

    if first_units:
        growth = f"{(last_units - first_units) / first_units * 100:.1f}%"
    else:
        growth = "undefined (starting value is zero)"

    total_units = sum(values[0] for values in monthly.values())
    total_revenue = sum(
        (values[1] for values in monthly.values()), Decimal("0")
    )

    table_rows = "\n".join(
        f"| {month} | {monthly[month][0]} | "
        f"{monthly[month][1]:,.2f} |"
        for month in months
    )

    # Create the written analysis report.
    report = f"""# Sales analysis report

**Fictional teaching dataset. No real shop or customer records.**

## Question

How did total units sold and sales revenue change across the supplied months?

## Method and checks

Each source row represents one product in one month. Revenue is calculated
by multiplying units sold by unit price. The script adds units and revenue
by month, sorts the months chronologically, and checks column names, dates,
nonnegative values, and duplicate month/product pairs.

The supplied dataset contains {len(seen)} records. No rows were removed
or imputed. These checks do not prove that a real-world source is accurate
or complete.

## Results

| Month | Units sold | Revenue (NGN) |
| --- | ---: | ---: |
{table_rows}

- Total units sold: **{total_units:,}**.
- Total revenue: **NGN {total_revenue:,.2f}**.
- Units changed from {first_units} in {months[0]} to {last_units}
  in {months[-1]}: **{growth}**.
- Percentage change = (last value - first value) / first value × 100.

![Monthly units sold, using fictional data](sales_chart.svg)

## Interpretation and limits

The results describe only the supplied sample. They do not establish why
sales changed or predict future demand. A short dataset may not represent
long-term patterns. Revenue is not profit: costs, discounts, returns, and
tax are not included. No causal or market claims are made.

## Next analytical step

For a real project, obtain authorized records for a longer period, check
for missing months, and examine prices, stock availability, and promotions
before making recommendations.
"""

    (ROOT / "analysis_report.md").write_text(
        report, encoding="utf-8"
    )

    # Create an SVG bar chart of units sold.
    maximum = max(values[0] for values in monthly.values()) or 1
    height = 170 + len(months) * 75

    svg = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="900" height="{height}" '
            f'viewBox="0 0 900 {height}">'
        ),
        "<title>Monthly units sold — fictional teaching data</title>",
        '<rect width="100%" height="100%" fill="#f5f8fc"/>',
        '<g font-family="Arial, sans-serif" fill="#172b4d">',
        (
            '<text x="40" y="45" font-size="28" '
            'font-weight="bold">Monthly units sold</text>'
        ),
        (
            '<text x="40" y="75" font-size="17">'
            "Fictional teaching data • bar length starts at zero</text>"
        ),
    ]

    for index, month in enumerate(months):
        y_position = 110 + index * 75
        value = monthly[month][0]
        bar_width = value / maximum * 540

        svg.extend(
            [
                (
                    f'<text x="40" y="{y_position + 28}" '
                    f'font-size="20">{escape(month)}</text>'
                ),
                (
                    f'<rect x="190" y="{y_position}" '
                    f'width="{bar_width:.2f}" height="42" '
                    'fill="#167d9a"/>'
                ),
                (
                    f'<text x="{205 + bar_width:.2f}" '
                    f'y="{y_position + 28}" font-size="20">'
                    f"{value}</text>"
                ),
            ]
        )

    svg.extend(
        [
            (
                f'<text x="190" y="{height - 25}" font-size="16">'
                "0 → Units sold | Source: sales.csv</text>"
            ),
            "</g></svg>",
        ]
    )

    (ROOT / "sales_chart.svg").write_text(
        "\n".join(svg), encoding="utf-8"
    )

    print(
        f"Analysis complete! Validated {len(seen)} records; "
        f"{total_units} units sold; "
        f"NGN {total_revenue:,.2f} revenue."
    )
    print(
        "Created: monthly_summary.csv, "
        "analysis_report.md, and sales_chart.svg"
    )


if __name__ == "__main__":
    main()
