from collections import defaultdict
from datetime import timedelta,date
from src.models import NightSleepSummary, SleepRecord

def is_Apple_Watch(record: SleepRecord) -> bool:
    return "Apple" in record.source and "Watch" in record.source # ve se há Apple e Watch na source

def get_watch_sleep_records(records: list[SleepRecord]) -> list[SleepRecord]:
    WatchRecords = []
    for record in records:
        if is_Apple_Watch(record):
            WatchRecords.append(record)

    return WatchRecords

def get_sleep_date(record: SleepRecord):
    shifted_time = record.start_time - timedelta(hours=12)
    return shifted_time.date() + timedelta(days=1)

def group_sleep_by_night(records: list[SleepRecord]) -> dict:
    nights = defaultdict(list)
    for record in records:
        sleep_date = get_sleep_date(record)
        nights[sleep_date].append(record)
    return nights

def summarize_night(sleep_date, records: list[SleepRecord]) -> NightSleepSummary:
    stage_minutes = {
        "core": 0.0,
        "deep": 0.0,
        "rem": 0.0,
        "awake": 0.0,
    }
    for record in records:
        if record.stage in stage_minutes:
            duration = record.end_time - record.start_time
            minutes = duration.total_seconds() / 60
            stage_minutes[record.stage] += minutes
    
    total_sleep = (stage_minutes["core"] + stage_minutes["deep"] +
                  stage_minutes["rem"])
    
    return NightSleepSummary(
        date=sleep_date,
        total_sleep_minutes=total_sleep,
        core_minutes=stage_minutes["core"],
        deep_minutes=stage_minutes["deep"],
        rem_minutes=stage_minutes["rem"],
        awake_minutes=stage_minutes["awake"],
    )

def build_night_summaries(sleep_nights: dict[date, list[SleepRecord]]) -> list[NightSleepSummary]:
    night_summaries = []
    for date, records in sleep_nights.items():
        summary = summarize_night(date, records)
        night_summaries.append(summary)
    night_summaries = sorted(night_summaries, key=lambda summary: summary.date)
    return night_summaries

def is_valid_night(night_sleep_summary: NightSleepSummary) -> bool:
    return night_sleep_summary.total_sleep_minutes >= 180

def filter_valid_nights(nights: list[NightSleepSummary]) -> list[NightSleepSummary]:
    valid_nights = []
    for night in nights:
        if is_valid_night(night):
            valid_nights.append(night)
    return valid_nights
