from dataclasses import dataclass
from datetime import datetime, date 


# todos os dados sao escritos usando esta métrica
@dataclass
class HealthMetric:
    metric_type: str            # ex: HRV
    value: float                # ex: 87,9
    unit: str                   # ex: ms
    timestamp: datetime         # 2026-09-24 07:32


@dataclass
class SleepRecord:
    stage: str
    start_time: datetime
    end_time: datetime
    source: str

@dataclass
class NightSleepSummary:
    date: date
    total_sleep_minutes: float
    core_minutes: float
    deep_minutes: float
    rem_minutes: float
    awake_minutes: float