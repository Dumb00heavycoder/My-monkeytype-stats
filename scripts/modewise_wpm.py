def modewise_wpm(df):
    sec15 = df[(df['mode'] == 'time') & (df['mode2'] == '15')]['wpm'].max()
    sec30 = df[(df['mode'] == 'time') & (df['mode2'] == '30')]['wpm'].max()
    sec60 = df[(df['mode'] == 'time') & (df['mode2'] == '60')]['wpm'].max()
    sec120 = df[(df['mode'] == 'time') & (df['mode2'] == '120')]['wpm'].max()
    
    asec15 = df[(df['mode'] == 'time') & (df['mode2'] == '15')]['acc'].max()
    asec30 = df[(df['mode'] == 'time') & (df['mode2'] == '30')]['acc'].max()
    asec60 = df[(df['mode'] == 'time') & (df['mode2'] == '60')]['acc'].max()
    asec120 = df[(df['mode'] == 'time') & (df['mode2'] == '120')]['acc'].max()



    print(f"In 15 second:- {sec15} wpm and {asec15} acc ")
    print(f"In 30 second:- {sec30} wpm and {asec30} acc ")
    print(f"In 60 second:- {sec60} wpm and {asec60} acc")
    print(f"In 120 second:- {sec120} wpm and {asec120} acc")
    


