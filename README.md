# Sample Data Analyst Portfolio

**Instructor demonstration • Fictional data • Beginner level**

This repository demonstrates how to communicate a small analysis clearly: ask a
question, describe the data, show calculations, visualize results and explain limits.
It is a teaching sample, not evidence of a student's completed work or employment.

## Featured project: Stationery sales analysis

**Question:** How did units sold and revenue change from January to March 2026?

The dataset contains nine invented monthly product records. It is supplied solely
for practice and does not represent a real business or Nigerian market prices.

| Measure | January | February | March |
| --- | ---: | ---: | ---: |
| Units sold | 60 | 75 | 90 |
| Revenue (NGN) | 20,500 | 25,500 | 30,500 |

**Finding:** Units increased by 50% from January to March: `(90 - 60) / 60 × 100`.
Total revenue was NGN 76,500. This does not establish the cause of the increase.

![Monthly units sold — fictional data](sales_chart.svg)

## Explore the evidence

| File | Purpose |
| --- | --- |
| [sales.csv](sales.csv) | Fictional source data |
| [data_dictionary.md](data_dictionary.md) | Field meanings, units and assumptions |
| [analysis_report.md](analysis_report.md) | Method, results, interpretation and limitations |
| [monthly_summary.csv](monthly_summary.csv) | Calculated monthly totals |
| [sales_chart.svg](sales_chart.svg) | Chart with a zero baseline |
| [analyze.py](analyze.py) | Reproducible analysis using Python's standard library |
| [excel_walkthrough.md](excel_walkthrough.md) | Equivalent calculations for Excel learners |
| [skills_checklist.md](skills_checklist.md) | Editable self-assessment; no invented proficiency claims |
| [UPLOAD_GUIDE.md](UPLOAD_GUIDE.md) | Upload and customization instructions |

## Reproduce the analysis

Python is optional for viewing this portfolio. The report and chart are included.
To regenerate the summary, report and SVG chart, install Python 3, open a terminal
in this folder and run:

```bash
python analyze.py
```

On a system where Python 3 uses the command `python3`, use `python3 analyze.py`.
No additional packages are needed. The script reads files relative to its own location.
If you change the data, regenerate the outputs and update this README's results and
the report's interpretation to match the new dataset.

## Skills illustrated

- Defining an analytical question and documenting data provenance.
- Checking records, aggregating data and calculating percentage change.
- Creating a labelled chart and communicating a finding without claiming causation.
- Organizing a repository and documenting reproducible steps.

## Make this portfolio your own

Add your name and a truthful short introduction. Replace this demonstration with
your own authorized analysis, or keep it clearly labelled as guided practice.
Explain your contribution and acknowledge any assistance. Add further projects only
when you have evidence to show. Review the skills checklist after each project.
