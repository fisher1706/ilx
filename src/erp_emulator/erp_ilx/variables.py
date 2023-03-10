data_case_1 = [
    {"trans": "XX-1", "qnt": 10, "status": "PickUpNow"},
]

data_case_2 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
]

data_case_3 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "PickUpNow"}
]

data_case_4 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 30, "status": "PickUpNow"},
    {"trans": "XX-3", "qnt": 50, "status": "PickUpNow"}
]

data_case_5 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"}
]

data_case_6 = [
    {"trans": "XX-1", "qnt": 110, "status": "Invoice"}
]

data_case_7 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-4", "qnt": 20, "status": "PickUpNow"}
]

data_case_8 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-4", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-5", "qnt": 30, "status": "PickUpNow"}
]

data_case_10 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "Invoice"},
    {"trans": "XX-4", "qnt": 60, "status": "Invoice"},
    {"trans": "XX-5", "qnt": 30, "status": "PickUpNow"}
]

data_case_11 = [
    {"trans": "XX-1", "qnt": 10, "status": "Invoice"},
    {"trans": "XX-2", "qnt": 20, "status": "Invoice"},
    {"trans": "XX-3", "qnt": 50, "status": "PickUpNow"},
    {"trans": "XX-4", "qnt": 60, "status": "PickUpNow"},
    {"trans": "XX-5", "qnt": 30, "status": "PickUpNow"}
]

data_infor = [
    {'orderno': '21982806', 'ordersuf': '05', 'stage': 'Ent', 'custpo': 'SRX VMI', 'qty': 0, 'qty_stk': 0},
    {'orderno': '21982807', 'ordersuf': '06', 'stage': 'Ord', 'custpo': 'SRX VMI', 'qty': 20, 'qty_stk': 20},
    {'orderno': '21982808', 'ordersuf': '07', 'stage': 'Pck', 'custpo': 'SRX VMI', 'qty': 30, 'qty_stk': 30},
    {'orderno': '21982809', 'ordersuf': '08', 'stage': 'Shp', 'custpo': 'SRX VMI', 'qty': 40, 'qty_stk': 40},
    {'orderno': '21982810', 'ordersuf': '09', 'stage': 'Inv', 'custpo': 'SRX VMI', 'qty': 50, 'qty_stk': 50},
    {'orderno': '21982811', 'ordersuf': '10', 'stage': 'Pd', 'custpo': 'SRX VMI', 'qty': 60, 'qty_stk': 60}
]

data_wmi_sync = [
    {"customerId": 60428, "productId": 326, "pageSize": 5, "startIndex": 2},
    {"customerId": 60430, "productId": 745, "pageSize": 4, "startIndex": 1},
    {"customerId": 60437, "productId": 421, "pageSize": 3, "startIndex": 1}
]

data_billing = [
    {"customer": "external-api", "number": 5},
    {"customer": "test-full2", "number": 5}
]

data_price_eclipse = [
    {"customerNumber": 100, "dsku": 200},
    {"customerNumber": 200, "dsku": 100}
]

data_gerrie_electric = [
   {"orderNumber": "123", "customerNumber": "456", "quantityOrdered": 100, "quantityShipped": 200, "type": "QUOTED"},
   {"orderNumber": "789", "customerNumber": "765", "quantityOrdered": 0, "quantityShipped": 200, "type": "ORDERED"},
   {"orderNumber": "345", "customerNumber": "876", "quantityOrdered": 100, "quantityShipped": 0, "type": "SHIPPED"},
   {"orderNumber": "347", "customerNumber": "877", "quantityOrdered": 100, "quantityShipped": 0,
    "type": "DO_NOT_REORDER"},
   {"orderNumber": "348", "customerNumber": "873", "quantityOrdered": 100, "quantityShipped": 0, "type": "SHIPPED"}
]

data_quote_infor = [
    {"custNo": "123", "transactionType": "QUOTED", "invNr": "11596160", "transType": "QU"},
    {"custNo": "456", "transactionType": "ORDERED", "invNr": "11596163", "transType": "SO"},
    {"custNo": "123", "transactionType": "QUOTED", "invNr": "11596160", "transType": "SO"},
]

data_quote_eclipse = [
    {"productId": "S011980089", "status": "QUOTED", "orderStatus": "Bid", "customer": "123"},
    {"productId": "S011980095", "status": "ORDERED", "orderStatus": "Bid", "customer": "1238"},
    {"productId": "S011980089", "status": "QUOTED", "orderStatus": "Bid", "customer": "1234"},
]

data_price_d1 = [
    {"customer": "user_1", "item": "test_1"},
    {"customer": "user_2", "item": "test_2"},
    {"customer": "user_3", "item": "test_3"}
]

data_infor_billing = {'shipToNo': '3', 'qtyOrd': '2', 'sellerProd': '1'}

data_infor_transfers = {'companyNumber': 123,
                        'singleLineNumber': 0,
                        'includeLineData': True,
                        'includeTotalData': False,
                        'includeHeaderData': True,
                        'lineSort': 'a',
                        'operatorPassword': 'logix2020',
                        'operatorInit': '2srx',
                        'cErrorMessage': '170678'
                        }
