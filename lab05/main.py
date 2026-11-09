from logstats import count_levels, format_report, top_errors

path = input().strip()

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

total = sum(counts.values())
print(total)
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open("report.txt", "w", encoding="utf-8") as report:
    report.write(format_report(counts, errors))
