"""
Single string variable containing the CREATE
statement for the nal_property_records table
"""

TABLE_CREATE = """CREATE TABLE IF NOT EXISTS nal_property_records (
    PARCEL_ID  VARCHAR NOT NULL PRIMARY KEY,
    COUNTY  VARCHAR,
    CO_NO INT,
    DOR_UC VARCHAR,
    DOR_UC_DESC VARCHAR,
    JV BIGINT,
    ACT_YR_BLT  VARCHAR,
    TOT_LVG_AREA  BIGINT,
    SALE_PRC1 DECIMAL,
    SALE_YR1 VARCHAR,
    SALE_MO1 VARCHAR,
    OWN_NAME VARCHAR, 
    CENSUS_BK VARCHAR,
    PHY_ADDR1 VARCHAR,
    PHY_ADDR2 VARCHAR,
    PHY_CITY VARCHAR,
    PHY_ZIPCD VARCHAR
)"""

