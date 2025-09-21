def countDays(days, meetings):
    if not meetings:
        return days
        
    valid_meetings = [m for m in meetings if m[0] <= days]
    if not valid_meetings:
        return days
        
    valid_meetings.sort(key=lambda x: x[0])
    
    merged = []
    start_curr, end_curr = valid_meetings[0]
    for i in range(1, len(valid_meetings)):
        s, e = valid_meetings[i]
        if s <= end_curr + 1:
            end_curr = max(end_curr, e)
        else:
            merged.append([start_curr, end_curr])
            start_curr, end_curr = s, e
    merged.append([start_curr, end_curr])
    
    covered_days = 0
    for inter in merged:
        s, e = inter
        actual_end = min(e, days)
        covered_days += actual_end - s + 1
        
    return days - covered_days

day=10
meeting=[[5,7],[1,3],[9,10]]
print(countDays(day,meeting))