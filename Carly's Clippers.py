hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Total Price
total_price = 0
for i in prices:
  total_price +=  i
  #print(total_price)

#Average Price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

#New Price
new_price = [i-5 for i in prices]
#print(new_price)

#Total Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  
print("Total Revenue:", total_revenue)

#Average Daily Revenue
average_daily_revenue = total_revenue / 7
print("Avergae Daily Revenue is:", average_daily_revenue)

#Price of haircuts under $30 based on new price
cuts_under_30 = [ hairstyles[i] for i in range(len(new_price)) if new_price[i] < 30]
print(cuts_under_30) 