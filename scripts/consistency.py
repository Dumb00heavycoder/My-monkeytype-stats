def consistency(df):
   avg = df['consistency'].mean()

   maxi = df['consistency'].max()
   maxi_time = (df['consistency'] == maxi).sum() 

   mini = df['consistency'].min()
   mini_time = (df['consistency'] == mini).sum()
   
   print(f"average consistency: {avg}")
    
   if maxi_time > 1:
       print(f"Maximum consistency: {maxi}, achieved {maxi_time} times")
   else:
       print(f"Maximum consistency: {maxi}, achieved {maxi_time} time")

   if mini_time > 1:
       print(f"Minimum consistency: {mini}, achived {mini_time} times")

   else:
        print(f"Minimum consistency: {mini}, achived {mini_time} time")
