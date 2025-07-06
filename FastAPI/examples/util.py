# ~business logic
def item_value(item_id, name):
    return {"item_id":item_id, "name": name}

if __name__=="__main__":
    test = item_value(234,"jegan")
    print(test)
    print(type(test))