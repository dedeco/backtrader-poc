
Select *
from bitmex_trade_1T_candle
INTO OUTFILE '/Users/dedeco/Projetos/backtrader/bitmex_trade_1T_candle.csv' 
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

CREATE DATABASE tempus_market_data;
CREATE USER 'backtest'@'localhost' IDENTIFIED BY 'pass';
grant all privileges on tempus_market_data.* to 'backtest'@'localhost' ;
FLUSH PRIVILEGES;

CREATE TABLE `marketprices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quote` VARCHAR(6)  NOT NULL,
  `date` datetime  NOT NULL,
  `price_first` decimal(13,8) NULL,
  `price_max`  decimal(13,8)  NULL,
  `price_min` decimal(13,8)  NULL,
  `price_last` decimal(13,8) NULL,
  `volume` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO marketprices(quote,price_first,price_max,price_min,price_last,volume, date)
SELECT 'BITMEX',
       price_first,
       price_max,
       price_min,
       price_last,
       volume,
       cast(STR_TO_DATE(date,'%Y-%m-%d %T') AS datetime) AS date
FROM bitmex_trade_1T_candle;
#+--------------------+------------+------+-----+---------+-------+
#| Field              | Type       | Null | Key | Default | Extra |
#+--------------------+------------+------+-----+---------+-------+
#| ('price', 'first') | double     | YES  |     | NULL    |       |
#| ('price', 'max')   | double     | YES  |     | NULL    |       |
#| ('price', 'min')   | double     | YES  |     | NULL    |       |
#| ('price', 'last')  | double     | YES  |     | NULL    |       |
#| ('volume', 'sum')  | bigint(20) | YES  |     | NULL    |       |
#| ('datetime', '')   | text       | YES  |     | NULL    |       |
#+--------------------+------------+------+-----+---------+-------+

