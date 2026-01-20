  def insert(self, intervals, new_interval):
    merged = []
    leng = len(intervals)
    # TODO: Write your code here
    for index, interval in enumerate(intervals):
      if new_interval.end < interval.start:
        merged.append(new_interval)
        #merged.append(interval)
        merged = merged + intervals[index:]
        break
      elif new_interval.start > interval.end:
        merged.append(interval)
        # if index == leng - 1:
        #   merged.append(new_interval)
        # continue
      elif new_interval.start >= interval.start and new_interval.end <= interval.end:
        # merged.append(interval)
        # merged = merged + intervals[index:]
        merged = intervals
        break
        # continue
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
    
    # if len(merged) < leng:
    #   merged = merged + intervals[len(merged):]
    return merged
