from datetime import datetime
from src.models import HealthMetric

hrv_measurement = HealthMetric("hrv", 52.4, "ms", datetime.now())
resting_hr = HealthMetric("rhr", 56, "bpm",datetime.now())
respiratory_rate = HealthMetric("rr", 14.2, "breaths/min ",datetime.now())

today_metrics = [hrv_measurement,resting_hr, respiratory_rate]
def print_metrics(metrics : list[HealthMetric]) -> None:
    for metric in metrics:
        print(f"{metric.metric_type}: {metric.value} {metric.unit}")
print_metrics(today_metrics)