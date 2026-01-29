  def insert(self, intervals, new_interval):
    merged = []
    leng = len(intervals)
    for index, interval in enumerate(intervals):
      if new_interval.end < interval.start:
        merged.append(new_interval)
        merged = merged + intervals[index:]
        break
      elif new_interval.start > interval.end:
        merged.append(interval)
      elif new_interval.start >= interval.start and new_interval.end <= interval.end:
        merged = intervals
        break
      elif new_interval.start >= interval.start and new_interval.end > interval.end and \
        new_interval.start <= interval.end:
        new_interval = Interval(start=interval.start, end=new_interval.end)
      elif new_interval.start <= interval.start and new_interval.end < interval.end and \
        new_interval.end >= interval.start:
        new_interval = Interval(start=new_interval.start, end=interval.end)
      elif new_interval.start < interval.start and new_interval.end > interval.end:
        new_interval = Interval(start=new_interval.start, end=new_interval.end)

      if index == leng - 1:
          merged.append(new_interval)
    
    return merged
