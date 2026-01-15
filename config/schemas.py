#columns to drop
DROP_COLS = [
    "CustomerID"
] 

#target column(s)
TARGET_COL = "Churn"

#numeric columns
NUM_COLS = [
    "Tenure",
    "WarehouseToHome",
    "HourSpendOnApp",
    "NumberOfDeviceRegistered",
    "SatisfactionScore",
    "NumberOfAddress",
    "OrderAmountHikeFromlastYear",
    "CouponUsed",
    "OrderCount",
    "DaySinceLastOrder",
    "CashbackAmount"
]

#categorical columns
CAT_COLS = [
    "PreferredLoginDevice",
    "CityTier",
    "PreferredPaymentMode",
    "Gender",
    "PreferedOrderCat",
    "MaritalStatus"
]

#binary columns
BIN_COLS = [
    "Complain"
]

