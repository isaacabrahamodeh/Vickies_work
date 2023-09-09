show databases;

use mysql;

CREATE TABLE process_monitor (
    pid INT,
    name VARCHAR(255),
    rss BIGINT,
    vms BIGINT,
    num_page_faults BIGINT,
    num_threads INT,
    ppid INT,
    status VARCHAR(50),
    create_time DATETIME
);


ALTER TABLE process_monitor DROP COLUMN num_page_faults;


SELECT * FROM process_monitor;
