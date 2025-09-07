def modewise_wpm(df):
    #time
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
    
    #words
    wrd10 = df[(df['mode'] == 'words') & (df['mode2'] == '10')]['wpm'].max()
    wrd25 = df[(df['mode'] == 'words') & (df['mode2'] == '25')]['wpm'].max()
    wrd50 = df[(df['mode'] == 'words') & (df['mode2'] == '50')]['wpm'].max()
    wrd100 = df[(df['mode'] == 'words') & (df['mode2'] == '100')]['wpm'].max()

    awrd10 = df[(df['mode'] == 'words') & (df['mode2'] == '10')]['acc'].max()
    awrd25 = df[(df['mode'] == 'words') & (df['mode2'] == '25')]['acc'].max()
    awrd50 = df[(df['mode'] == 'words') & (df['mode2'] == '50')]['acc'].max()
    awrd100 = df[(df['mode'] == 'words') & (df['mode2'] == '100')]['acc'].max()



    print(f"In 10 words:- {wrd10} wpm and {awrd10} acc ")
    print(f"In 25 words:- {wrd25} wpm and {awrd25} acc ")
    print(f"In 50 words:- {wrd50} wpm and {awrd50} acc")
    print(f"In 100 words:- {wrd100} wpm and {awrd100} acc")

