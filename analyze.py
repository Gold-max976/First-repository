"""Reproduce the teaching example using Python 3 and its standard library.

All sales records are fictional. Run: python analyze.py
Outputs: monthly_summary.csv, analysis_report.md, sales_chart.svg.
"""
import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
from datetime import datetime
from html import escape

ROOT = Path(__file__).resolve().parent


def main():
    monthly = defaultdict(lambda: [0, Decimal('0')])
    seen = set()
    with (ROOT / 'sales.csv').open(newline='', encoding='utf-8') as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ['month', 'product', 'units_sold', 'unit_price_ngn']:
            raise ValueError('Unexpected CSV columns')
        for row in reader:
            month, product = row['month'], row['product'].strip()
            if datetime.strptime(month, '%Y-%m').strftime('%Y-%m') != month or not product:
                raise ValueError('Invalid month or empty product')
            key = (month, product)
            if key in seen:
                raise ValueError(f'Duplicate monthly product record: {key}')
            seen.add(key)
            units, price = int(row['units_sold']), Decimal(row['unit_price_ngn'])
            if units < 0 or not price.is_finite() or price < 0:
                raise ValueError('Units and price must be nonnegative finite values')
            monthly[month][0] += units
            monthly[month][1] += units * price
    if not monthly:
        raise ValueError('Dataset is empty')
    months = sorted(monthly)
    with (ROOT / 'monthly_summary.csv').open('w', newline='', encoding='utf-8') as dest:
        writer = csv.writer(dest)
        writer.writerow(['month', 'units_sold', 'revenue_ngn'])
        for month in months:
            units, revenue = monthly[month]
            writer.writerow([month, units, f'{revenue:.2f}'])
    first, last = monthly[months[0]][0], monthly[months[-1]][0]
    growth = f'{(last-first)/first*100:.1f}%' if first else 'undefined (starting value is zero)'
    total_units = sum(v[0] for v in monthly.values())
    total_revenue = sum(v[1] for v in monthly.values())
    table = '\n'.join(f'| {m} | {monthly[m][0]} | {monthly[m][1]:,.0f} |' for m in months)
    report = f'''# Sales analysis report

**Fictional teaching dataset. No real shop or customer records.**

## Question
How did total units sold and sales revenue change across the supplied months?

## Method and checks
Each source row represents one product in one month. Revenue is units sold multiplied
by unit price. The script sums units and revenue by month, sorts months chronologically,
and checks column names, dates, nonnegative values and duplicate month/product pairs.
The supplied dataset contains {len(seen)} records. No rows were removed or imputed.
These checks do not prove that a real-world source is accurate or complete.

## Results
| Month | Units sold | Revenue (NGN) |
| --- | ---: | ---: |
{table}

- Total units sold: **{total_units:,}**.
- Total revenue: **NGN {total_revenue:,.0f}**.
- Units changed from {first} in {months[0]} to {last} in {months[-1]}: **{growth}**.
- Percentage change = (last value - first value) / first value × 100.

![Monthly units sold, using fictional data](sales_chart.svg)

## Interpretation and limits
The original example shows rising monthly sales. This describes the supplied sample;
it does not establish why sales changed or predict future demand. The data has only
three months, three products and deliberately simple values. Revenue is not profit:
costs, discounts, returns and tax are not included. No causal or market claims are made.

## Next analytical step
For a real project, obtain authorized records for a longer period, check missing months,
and examine prices, stock availability and promotions before recommending purchases.
'''
    (ROOT / 'analysis_report.md').write_text(report, encoding='utf-8')
    maximum = max(v[0] for v in monthly.values()) or 1
    height = 170 + len(months) * 75
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}">',
           '<title>Monthly units sold — fictional teaching data</title>',
           '<rect width="100%" height="100%" fill="#f5f8fc"/>',
           '<g font-family="Arial, sans-serif" fill="#172b4d">',
           '<text x="40" y="45" font-size="28" font-weight="bold">Monthly units sold</text>',
           '<text x="40" y="75" font-size="17">Fictional teaching data • bar length starts at zero</text>']
    for i, month in enumerate(months):
        y = 110 + i * 75
        value = monthly[month][0]
        width = value / maximum * 540
        svg += [f'<text x="40" y="{y+28}" font-size="20">{escape(month)}</text>',
                f'<rect x="190" y="{y}" width="{width:.2f}" height="42" fill="#167d9a"/>',
                f'<text x="{205+width:.2f}" y="{y+28}" font-size="20">{value}</text>']
    svg += [f'<text x="190" y="{height-25}" font-size="16">0 → Units sold | Source: sales.csv</text>', '</g></svg>']
    (ROOT / 'sales_chart.svg').write_text('\n'.join(svg), encoding='utf-8')
    print(f'Validated {len(seen)} records; {total_units} units; NGN {total_revenue:,.0f} revenue.')


if __name__ == '__main__':
    main()
