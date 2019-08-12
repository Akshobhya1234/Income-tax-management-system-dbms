GAIN_CAT = (
    ("HIGH", ("HIGH")),
    ("LOW", ("LOW"))
    )
ASSET_TYPE = (
    ("HOUSE", ("HOUSE")),
    ("FIXED DEPOSIT", ("FIXED DEPOSIT")),
    ("SHARES", ("SHARES")),
    ("CASH IN HAND", ("CASH IN HAND")),
    ("LAND PROPERTY", ("LAND PROPERTY"))
    )
TAX_PER = (
    (15, ("HOUSE: 15")),
    (12, ("FIXED DEPOSIT: 12")),
    (10,("SHARES/CASH IN HAND: 10")),
    (14,("LAND PROPERTY: 14"))
    )

AGE_CAT = (
    ("<18", ("<18")),
    ("18-35",("18-35")),
    ("35-60",("35-60")),
    (">60",(">60"))
    )
TAP = (
    ("<5,00,000",("<5,00,000")),
    ("5,00,001-20,00,000",("5,00,001-20,00,000")),
    (">20,00,000",(">20,00,000"))
    )
TAP1 = (
    (5,("<5,00,000: 5")),
    (15,("5,00,001-20,00,000: 15")),
    (30,(">20,00,000: 30"))
    )
