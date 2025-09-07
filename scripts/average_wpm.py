def average_wpm(df):
    avg = df['wpm'].mean()
    maxi = df['wpm'].max()
    mini = df['wpm'].min()
    max_time = (df['wpm'] == df['wpm'].max()).sum()
    mini_time =(df['wpm'] == df['wpm'].min()).sum()
    print(f"The average wpm of dhruv is {avg}")
    print(f"The maximum wpm of dhruv is {maxi} which has been achived {max_time} times")
    print(f"The minimum wpn of dhruv is {mini} which has been achived {mini_time} times")
    return {
        'average': avg,
        'maximum': maxi,
        'max_count': max_time,
        'minimum': mini,
        'min_count': mini_time
    }

