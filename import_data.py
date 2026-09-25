from collections import Counter

from src.health_importer import import_health_metrics
from src.health_importer import import_sleep_records
from src.sleep_analysis import (get_watch_sleep_records, group_sleep_by_night,
                                summarize_night, build_night_summaries, filter_valid_nights)

FILE_PATH = "data/apple_health_export/export.xml"

print("Importing sleep data...")

sleep_records = import_sleep_records(FILE_PATH)
watch_sleep = get_watch_sleep_records(sleep_records)
nights = group_sleep_by_night(watch_sleep)

print(f"Number of nights: {len(nights)}")

latest_date = max(nights.keys())
latest_summary = summarize_night(
    latest_date,
    nights[latest_date]
)

print("\nLatest night summary")
print(f"Date: {latest_summary.date}")
print(f"Total sleep: {latest_summary.total_sleep_minutes:.0f} min")
print(f"Core: {latest_summary.core_minutes:.0f} min")
print(f"Deep: {latest_summary.deep_minutes:.0f} min")
print(f"REM: {latest_summary.rem_minutes:.0f} min")
print(f"Awake: {latest_summary.awake_minutes:.0f} min")
print(f"Latest night: {latest_date}")
print(f"Records in latest night: {len(nights[latest_date])}")
#print(f"All sleep records: {len(sleep_records)}")
#print(f"Apple Watch sleep records: {len(watch_sleep)}")
summaries = build_night_summaries(nights)

print(f"Sleep summaries: {len(summaries)}")
print("First:", summaries[0])
print("Latest:", summaries[-1])
valid_summaries = filter_valid_nights(summaries)

print(f"All nights: {len(summaries)}")
print(f"Valid nights: {len(valid_summaries)}")
print("First valid:", valid_summaries[0])
print("Latest valid:", valid_summaries[-1])