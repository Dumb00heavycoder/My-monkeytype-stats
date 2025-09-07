def modewise_wpm(df):
    time_modes = {}
    sec15 = df[(df['mode'] == 'time') & (df['mode2'] == '15')]['wpm'].max()
    asec15 = df[(df['mode'] == 'time') & (df['mode2'] == '15')]['acc'].max()
    time_modes['15'] = {'wpm': sec15, 'acc': asec15}
    
    sec30 = df[(df['mode'] == 'time') & (df['mode2'] == '30')]['wpm'].max()
    asec30 = df[(df['mode'] == 'time') & (df['mode2'] == '30')]['acc'].max()
    time_modes['30'] = {'wpm': sec30, 'acc': asec30}
    
    sec60 = df[(df['mode'] == 'time') & (df['mode2'] == '60')]['wpm'].max()
    asec60 = df[(df['mode'] == 'time') & (df['mode2'] == '60')]['acc'].max()
    time_modes['60'] = {'wpm': sec60, 'acc': asec60}
    
    sec120 = df[(df['mode'] == 'time') & (df['mode2'] == '120')]['wpm'].max()
    asec120 = df[(df['mode'] == 'time') & (df['mode2'] == '120')]['acc'].max()
    time_modes['120'] = {'wpm': sec120, 'acc': asec120}
    
    word_modes = {}
    
    wrd10 = df[(df['mode'] == 'words') & (df['mode2'] == '10')]['wpm'].max()
    awrd10 = df[(df['mode'] == 'words') & (df['mode2'] == '10')]['acc'].max()
    word_modes['10'] = {'wpm': wrd10, 'acc': awrd10}
    
    wrd25 = df[(df['mode'] == 'words') & (df['mode2'] == '25')]['wpm'].max()
    awrd25 = df[(df['mode'] == 'words') & (df['mode2'] == '25')]['acc'].max()
    word_modes['25'] = {'wpm': wrd25, 'acc': awrd25}
    
    wrd50 = df[(df['mode'] == 'words') & (df['mode2'] == '50')]['wpm'].max()
    awrd50 = df[(df['mode'] == 'words') & (df['mode2'] == '50')]['acc'].max()
    word_modes['50'] = {'wpm': wrd50, 'acc': awrd50}
    
    wrd100 = df[(df['mode'] == 'words') & (df['mode2'] == '100')]['wpm'].max()
    awrd100 = df[(df['mode'] == 'words') & (df['mode2'] == '100')]['acc'].max()
    word_modes['100'] = {'wpm': wrd100, 'acc': awrd100}
    
    return {
        'time': time_modes,
        'words': word_modes
    }
