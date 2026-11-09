# Reproduce the example in Excel

Use the fictional `sales.csv`. This is a manual alternative to running Python.

1. Open the CSV. Check that columns A–D contain month, product, units_sold and
   unit_price_ngn. Units and prices must be numeric.
2. In E1 type `revenue_ngn`. In E2 enter `=C2*D2` and copy down to E10.
3. Check `=SUM(C2:C10)` returns **225**, and `=SUM(E2:E10)` returns **76500**.
4. Select A1:E10 and insert a PivotTable. Put `month` in Rows and `units_sold`
   and `revenue_ngn` in Values. Set both value summaries to **Sum**, not Count.
5. Check January = 60 units / NGN 20,500; February = 75 / NGN 25,500;
   March = 90 / NGN 30,500. Keep the months chronological.
6. Chart monthly units with a column or bar chart, excluding the grand total.
   Start the numerical axis at zero; title it “Monthly units sold — fictional data”.
7. Calculate January-to-March growth with `=(90-60)/60`; apply Percentage format
   to display **50%**. In your own workbook, reference the relevant result cells.
8. Save as an Excel workbook (.xlsx) to retain the formulas, PivotTable and chart.
   CSV does not preserve these workbook features.

State what the chart shows, then explain what the data cannot tell you: the reason
for the increase, profitability, or what will happen in the next month.
