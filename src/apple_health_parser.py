from lxml import etree
from datetime import datetime
from src.models import HealthMetric


def get_health_records(file_path: str, apple_type: str, metric_name: str) -> list[HealthMetric]:
    records = []
    context = etree.iterparse(file_path, events=("end",), tag="Record")

    for event, elem in context:
        metric_type = elem.get("type")

        if metric_type == apple_type:
            value = float(elem.get("value"))
            unit = elem.get("unit")
            timestamp = datetime.strptime(elem.get("startDate"), "%Y-%m-%d %H:%M:%S %z")
            metric = HealthMetric(metric_type = metric_name, value = value, unit = unit, timestamp = timestamp)
            records.append(metric)

        elem.clear()

        while elem.getprevious() is not None:           # remove elementos alteriores que ja processámos
            del elem.getparent()[0]

    return records
file_path = "data/apple_health_export/export.xml"

hrv_records = get_health_records(file_path, "HKQuantityTypeIdentifierHeartRateVariabilitySDNN", "hrv")
print(f"Total: {len(hrv_records)}")
print(hrv_records[-1:])
#print(f"HRV records: {hrv_count} Resting HR records: {rhr_count}")