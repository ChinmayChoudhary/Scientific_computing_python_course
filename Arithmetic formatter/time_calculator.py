def add_time(start, duration,day=None):
    
    day_index={'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5,'sunday':6}
    
    day_of_week=['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    duration_split=duration.split(':')
    duration_hours=int(duration_split[0])
    duration_mins=int(duration_split[1])
    
    
    start_split=start.split(' ')
    am_or_pm=start_split[1]
    
    start_split.pop(1)
    
    start_time=start.split(':')
    start_hours=int(start_time[0])
    start_mins=int(start_time[1].split(' ')[0])

    
    am_pm_change={'AM':'PM','PM':'AM'}
    
    no_of_days=int(duration_hours/24)
    
    end_mins=start_mins+duration_mins
    if end_mins>=60:
        start_hours+=1
        end_mins=end_mins-60
    
    no_of_am_pm_change=int((start_hours+duration_hours)/12)
    
    end_hours=(start_hours+duration_hours)%12
    
    end_mins=end_mins if end_mins>9 else '0'+str(end_mins)
    
    end_hours=12 if end_hours==0 else end_hours

    if (am_or_pm=='PM' and (start_hours+duration_hours)>=12):
        no_of_days+=1
    
    am_or_pm=am_pm_change[am_or_pm] if no_of_am_pm_change%2==1 else am_or_pm
    
    time=str(end_hours) + ':' + str(end_mins) + ' ' + am_or_pm
    
    if day!=None:
        day=day.lower()
        index=int((day_index[day]) + no_of_days)%7
        new_day=day_of_week[index]
        time+=', ' + new_day
    
    if no_of_days==1:
        return time + ' ' + '(next day)'
    elif no_of_days>1:
        return time + " (" + str(no_of_days) + ' days later)'

    return time