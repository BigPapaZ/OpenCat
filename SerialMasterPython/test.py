from ardSerial import wrapper


schedule = [['ktr',10],\
            ['kbalance',5],\
            ['ksit',5],\
            ['ktr',5],\
            ['kwk',5],\
            ['d',2]]

for task in schedule:
    wrapper(task)
