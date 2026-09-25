from datetime import datetime
from lxml import etree
from collections import Counter
from src.models import HealthMetric,SleepRecord


METRIC_TYPES = {
    "HKQuantityTypeIdentifierHeartRateVariabilitySDNN": "hrv",
    "HKQuantityTypeIdentifierRestingHeartRate": "resting_heart_rate",
    "HKQuantityTypeIdentifierRespiratoryRate": "respiratory_rate",
}

SLEEP_STAGES = {"HKCategoryValueSleepAnalysisAwake": "awake",
    "HKCategoryValueSleepAnalysisAsleepCore": "core",
    "HKCategoryValueSleepAnalysisAsleepDeep": "deep",
    "HKCategoryValueSleepAnalysisAsleepREM": "rem",
    "HKCategoryValueSleepAnalysisAsleepUnspecified": "asleep_unspecified",
    "HKCategoryValueSleepAnalysisInBed": "in_bed"}



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

def import_sleep_records(file_path: str) -> list[SleepRecord]:
    sleep_records = []

    context = etree.iterparse(
        file_path,
        events=("end",),
        tag="Record"
    )

    for event, elem in context:
        if elem.get("type") == "HKCategoryTypeIdentifierSleepAnalysis":

            stage = SLEEP_STAGES.get(elem.get("value"))

            if stage is not None:
                start_time = datetime.strptime(
                    elem.get("startDate"),
                    "%Y-%m-%d %H:%M:%S %z"
                )

                end_time = datetime.strptime(
                    elem.get("endDate"),
                    "%Y-%m-%d %H:%M:%S %z"
                )

                sleep_records.append(
                    SleepRecord(
                        stage=stage,
                        start_time=start_time,
                        end_time=end_time,
                        source=elem.get("sourceName")
                    )
                )

        elem.clear()

        while elem.getprevious() is not None:
            del elem.getparent()[0]

    return sleep_records