# Data dictionary and provenance

All values were invented for this instructor demonstration. There is no external
data source, real business, survey or customer information behind these records.

**Unit of observation:** one product's aggregated sales in one calendar month.
The nine rows cover three products in each of January, February and March 2026.

| Column | Type | Meaning | Example |
| --- | --- | --- | --- |
| month | Text, YYYY-MM | Reporting month | 2026-01 |
| product | Text | Fictional product category | Notebook |
| units_sold | Integer | Total units sold that month | 20 |
| unit_price_ngn | Number | Assumed price of one unit in Nigerian naira | 500 |

Prices are constant for each product across the sample. They are illustrative,
not researched market prices. All values are nonnegative, all nine month/product
pairs are unique, and there are no missing values in the supplied data.

Derived revenue = units_sold × unit_price_ngn. Monthly revenue sums all products.
Revenue is sales value before any costs, discounts, tax or returns, which are not
modelled here. The analysis does not calculate profit or inflation-adjusted growth.
