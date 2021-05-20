import cbpro
public_client = cbpro.PublicClient()
def a(Coin):
    return float(public_client.get_product_order_book('MKR-USD')["bids"][0][0])*Coin

while(True): 
    
    print(a(0.1))