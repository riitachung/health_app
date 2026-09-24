from collections import Counter

from src.health_importer import import_health_metrics


FILE_PATH = "data/apple_health_export/export.xml"

print("Importing Apple Health data...")

metrics = import_health_metrics(FILE_PATH)

counts = Counter(metric.metric_type for metric in metrics)

print("\nImport complete.")

for metric_type, count in counts.items():
    print(f"{metric_type}: {count}")