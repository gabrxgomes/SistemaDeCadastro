CREATE TABLE computers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patrimonio VARCHAR(255),
    funcionario VARCHAR(255),
    departamento VARCHAR(255),
    data_chegada DATE,
    problema TEXT,
    data_saida DATE,
    marca VARCHAR(255),
    reparo_realizado TEXT
);
