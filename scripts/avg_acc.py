def avg_acc(df):
    avg = df['acc'].mean()
    mini = df['acc'].min()
    mini_time = (df['acc'] == df['acc'].min()).sum()
    maxi = df['acc'].max()
    maxi_time = (df['acc'] == df['acc'].max()).sum()

    print(f"The average accuracy of dhruv is {avg}")
    if maxi_time > 1:
       print(f"The maximum accuracy of dhruv in a test is {maxi} which has been achived {maxi_time} times")
    else:
       print(f"The maximum accuracy of dhruv in a test is {maxi} which has been achived only {maxi_time} time")

    if mini_time > 1:
       print(f"The minimum accuraacy of dhruv in a test is {mini} which has been achived {mini_time} times")
    else:
       print(f"The minimum accuraacy of dhruv in a test is {mini} which has been achived only {mini_time} time")




