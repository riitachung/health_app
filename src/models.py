from dataclasses import dataclass
from datetime import datetime 


# todos os dados sao escritos usando esta métrica
@dataclass
class HealthMetric:
    metric_type: str            # ex: HRV
    value: float                # ex: 87,9
    unit: str                   # ex: ms
    timestamp: datetime         # 2026-09-24 07:32
