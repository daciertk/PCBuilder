LOAD DATA LOCAL INFILE '../csv/cpu.csv'
INTO TABLE cpu
FIELDS TERMINATED BY ',' ENCLOSED BY '""'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '../csv/mothorboard.csv'
INTO TABLE mothorboard
FIELDS TERMINATED BY ',' ENCLOSED BY '""'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;