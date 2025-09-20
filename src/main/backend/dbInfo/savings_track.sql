CREATE TABLE savings (
    savings_id SERIAL PRIMARY KEY,
    AccHolderName VARCHAR(100) NOT NULL,
    BankName VARCHAR(100) NOT NULL,
    Amount NUMERIC(12, 2) NOT NULL,
    return_percentage NUMERIC(5, 2),
    expiry_date DATE,
    created_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'active',
    country VARCHAR(50)
);
