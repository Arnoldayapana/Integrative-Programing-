# python file (your_name.py) 
# think of an item (15) that have different attributes
# create a dictionary from that item with attributes as
# values
# perform adding items, updating items, removing items,
# clear items
PhoneBrand = {
    "OppoReno" : {
    "Color " : "Blue ",
    "USB" : "type C",
    "RAM" : "6/8GB",
    "Size" : "6.4 inch",
    "price" : 16999 
},
    "Vivo_Y20" : {
    "Color" : "Red",
    "USB" : "type C",
    "RAM" : "3/6GB",
    "Size" : "6.51 inch",
    "price" : 7999   
    },
    "Huawei_Nova9" : {
    "Color" : "Starry Blue",
    "USB" : "type C",
    "RAM" : "3/6GB",
    "Size" : "6.57 inch",
    "price" : 19999
    },
    "CherryMobile_AquaS9" : {
    "Color" : "Black",
    "USB" : "type C",
    "RAM" : "2/4 GB",
    "Size" : "6.52 inch",
    "price" : 3999
    },
    "Lenovo Legion pro" : {
    "Color" : "Storm grey",
    "USB" : "type C",
    "RAM" : "8-16 GB",
    "Size" : "6.65 inch",
    "price" : 19799
    },
    "Samsung Galaxy A71" : {
    "Color" : "Prism Crush Pink",
    "USB" : "type C",
    "RAM" : "6/8GB",
    "Size" : "6.7 inch",
    "price" : 18449 
    },
    "Xiaomi 12 pro" : {
    "Color " : "Purple",
    "USB" : "type C", 
    "RAM" : "12GB",
    "Size" : "6.7 inch",
    "price" : 48999   
    },
    "Realme 8pro" : {
    "Color" : "Infinite Blue",
    "USB" : "type C",
    "RAM" : "8GB",
    "Size" : "6.4 inch",
    "price" : 16990
    },
    "Myphone MyXI1 Pro" : {
    "Color" : " Blue",
    "USB" : "micro USB",
    "RAM" : "3GB",
    "Size" : "5.99 inch",
    "price" : 3999
    },
    "Apple iPhone 14 Pro Max" : {
    "Color" : "Space Black",
    "USB" : "Lightning Port",
    "RAM" : "6GB",
    "Size" : "6.7 inch",
    "price" : 77990
    },
    " Nokia G21" : {
    "Color" : " Nordic Blue",
    "USB" : "type C",
    "RAM" : "6GB",
    "Size" : "6.5 inch",
    "price" : 9990
    
    },
    "Asus Zenfone 9" : {
    "Color" : "Infinite Blue",
    "USB" : "type C",
    "RAM" : "8GB",
    "Size" : "6.4 inch",
    "price" : 1699
    
    },
    "Infinix Note 12 PRO 5G" : {
    "Color" : "Snowfall",
    "USB" : "type C",
    "RAM" : "8GB",
    "Size" : "6.7 inch",
    "price" : 12499
    },
    "Meizu C9 Pro" : {
    "Color" : "Gold",
    "USB" : "Micro USB",
    "RAM" : "3GB",
    "Size" : "5.45 inch",
    "price" : 4572
    },
    "Sony Xperia 1 IV" : {
    "Color" : "White",
    "USB" : "type C",
    "RAM" : "12GB",
    "Size" : "6.5 inch",
    "price" : 77200    
    }
}
# method of adding item
PhoneBrand["POCO X4pro"]= {"Color": "LaserBlue","USB":"Type-C","RAM":"5GB","Size":"6.67 inch","price":16990}

 #method of updating items
PhoneBrand["OppoReno"]= {"Color": "Red Velvet","USB":"Type C","RAM":"12GB","Size":"6.67 inch","price":29990}

#method of clear Items
#PhoneBrand.clear()

print(PhoneBrand)