-- SQL-команды для создания таблиц

CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title text NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE customers
(
    customer_id varchar(50) NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(50) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
)