# Question:
# You are given a list of orders.
# Each order has: orderId , status , amount
# Print all orderIds where:
# - status is "FAILED"
# - amount is greater than 1000
# Use list comprehension.

orders = [
    "101,SUCCESS,500",
    "102,FAILED,1200",
    "103,FAILED,300",
    "104,SUCCESS,2500",
    "105,FAILED,1800"
]

# Answer:
# Split each order into orderId, status, amount
# Filter only FAILED orders with amount > 1000
# Store only orderId

result = [
    orderId for order in orders for orderId, status, amount in [order.split(",")] if status=='FAILED' and int(amount)>1000
]

print(result)