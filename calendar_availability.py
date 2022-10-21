from itertools import chain

Interval = tuple[int, int]


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    merged_intervals = [intervals[0]]
    for start_time, end_time in intervals[1:]:
        if merged_intervals[-1][1] >= start_time:
            merged_intervals[-1][1] = max(end_time, merged_intervals[-1][1])
        else:
            merged_intervals.append([start_time, end_time])
    return merged_intervals


def find_available_times(
    schedules: list[list[Interval]], min_slot_length: int
) -> list[Interval]:
    # flatten and sort all intervals
    intervals = list(sorted(chain(*schedules)))
    # merge intervals
    merged_intervals = merge_intervals(intervals)
    # the slots between intervals constitute the availabities
    available_slots = []
    for (_, meeting1_end_time), (meeting2_start_time, _) in zip(
        merged_intervals, merged_intervals[1:]
    ):
        slot_length = meeting2_start_time - meeting1_end_time
        if slot_length >= min_slot_length:
            available_slots.append((meeting1_end_time, meeting2_start_time))
    return available_slots
