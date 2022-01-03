from server.models import User, Bill, Product

def create_new_user(username):
    user = User(name=username)
    user.save()
    return user.id

def create_new_bill(author_id, products):
    bill = Bill(author=author_id)
    bill.save()
    for p in products:
        new_product = Product(name=p['name'], price=p['price'], quantity=p['quantity'], is_countable=p['is_countable'], bill_id=bill.id)
        new_product.save()
        