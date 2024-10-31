CREATE TABLE cpu(
	Cpu_name varchar(255) NOT NULL,
    Price float NOT NULL,
    Core_count int NOT NULL,
    Core_clock float NOT NULL,
    Boost_clock float NOT NULL,
    Tdp int,
    Graphics varchar(255),
    Smt BOOl,
    PRIMARY KEY (Cpu_name)
    );
    
CREATE TABLE motherboard(
	Motherboard_name VARCHAR(255) NOT NULL,
    Price FLOAT NOT NULL,
    Socket VARCHAR (255) NULL,
    Form_factor VARCHAR(255),
    Max_memory INT,
    Memory_slot INT,
    Color VARCHAR(255),
    PRIMARY KEY(Motherboard_name) 
);
