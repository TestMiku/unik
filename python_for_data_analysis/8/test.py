import pandas as pd

# Laboratory
customers=pd.read_excel("customers.xlsx")
items_ordered=pd.read_excel("items_ordered.xlsx") #['customerid', 'order_date', 'item', 'quantity', 'price']

items_ordered.price = pd.to_numeric(items_ordered.price, errors='coerce')
items_ordered.order_date = pd.to_datetime(items_ordered.order_date, errors='coerce')

phone_data=pd.read_csv("phone_data.csv")

# 1 Find the maximum price of any item ordered in the items_ordered. //1250.00
items_ordered_max_price = items_ordered["price"].max()

# 2 Calculate the average price of all of the items ordered that were purchased in the month of Dec. //174.312500
items_ordered_mean_price_december = items_ordered[items_ordered.order_date.dt.month==12].price.mean()

# 3 What are the total number of rows in the items_ordered table? //32
total_rows_items_ordered = len(items_ordered)

# 4 For all of the tents that were ordered in the items_ordered table, 
# what is the price of the lowest tent? //79.99
min_for_tent = items_ordered[items_ordered.item=='Tent'].price.min()

#5 How many people are in each unique state in the customers.xlsx? 
# Indicate the state and display the number of people in each.
states = customers.groupby("state").size()

# 6From the items_ordered table, select the item, maximum price, and minimum price
#for each specific item in the table. Hint: The items will need to be broken
#up into separate groups.
items = items_ordered.groupby("item")["price"].agg(['max','mean'])

#7 How many orders did each customer make? Use the items_ordered.
#Find the customerid, number of orders they made, and the sum of their orders.
customer_order_stats = items_ordered.groupby('customerid').agg(
    number_of_orders=('order_date', 'size'),  # Count orders per customer
    total_order_sum=('price', 'sum')          # Sum of all orders per customer
)

print(
    items_ordered_max_price,
    items_ordered_mean_price_december,
    total_rows_items_ordered,
    min_for_tent,
    states,
    items,
    customer_order_stats,

    sep='\n'
)
