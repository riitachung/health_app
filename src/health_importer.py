from datetime import datetime
from lxml import etree
from src.models import HealthMetric

METRIC_TYPES = {
    "HKQuantityTypeIdentifierHeartRateVariabilitySDNN": "hrv",
    "HKQuantityTypeIdentifierRestingHeartRate": "resting_heart_rate",
    "HKQuantityTypeIdentifierRespiratoryRate": "respiratory_rate",
}



def import_health_metrics(file_path: str) -> list[HealthMetric]:
    metrics = []
    context = etree.iterparse(file_path, events=("end",), tag="Record")

    for event, elem in context:
        apple_type = elem.get("type")

        if apple_type in METRIC_TYPES:
            value = float(elem.get("value"))
            
            timestamp = datetime.strptime(elem.get("startDate"), "%Y-%m-%d %H:%M:%S %z")
            metric = HealthMetric(metric_type = METRIC_TYPES[apple_type],
                value = value, unit = elem.get("unit"), timestamp = timestamp)
            metrics.append(metric)

        elem.clear()

        while elem.getprevious() is not None:           # remove elementos alteriores que ja processámos
            del elem.getparent()[0]

    return metrics