menu = {
    "esp" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "coffee" : 24,
            "milk" : 150
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "coffee" : 24,
            "milk" : 200
        },
        "cost" : 3.0
    }
}
resources = {
    "water" : 300,
    "coffee" : 100,
    "milk" : 200
}

for name, info in menu.items():
    print(name)
    for key, value in info.items():
        print(key)
        for lable, ava in value.items():
            print(lable)

