def modewise_wpm(df):
    sec15 = df[(df['mode'] == 'time') & (df['mode2'] == '15')]['wpm'].max()
    sec30 = df[(df['mode'] == 'time') & (df['mode2'] == '30')]['wpm'].max()
    sec60 = df[(df['mode'] == 'time') & (df['mode2'] == '60')]['wpm'].max()
    sec120 = df[(df['mode'] == 'time') & (df['mode2'] == '120')]['wpm'].max()
    print(f"Maximum wpm in 15 second:-  {sec15} wpm")
    print(f"Maximum wpm in 30 second:- {sec30} wpm")
    print(f"Maximum wpm in 60 second:- {sec60} wpm")
    print(f"Maximum wpm in 120 second:- {sec120} wpm")


