orders = [
    "101,SUCCESS,500",
    "102,FAILED,1200",
    "103,FAILED,300",
    "104,SUCCESS,2500",
    "105,FAILED,1800"
]

result = [
    orderId for order in orders for orderId, status, amount in [order.split(",")] if status=='FAILED' and int(amount)>1000
]

print(result)