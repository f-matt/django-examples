CREATE TABLE model1 (
    id1 INTEGER,
    id2 INTEGER,
    col1 VARCHAR(10),
    PRIMARY KEY (id1, id2)
);

CREATE TABLE model2 (
    id INTEGER,
    model1_id1 INTEGER,
    model1_id2 INTEGER,
    col1 VARCHAR(10),
    PRIMARY KEY (id),
    FOREIGN KEY (model1_id1, model1_id2) REFERENCES model1 (id1, id2)
);

INSERT INTO model1 (id1, id2, col1) VALUES (1, 1, 'A');
INSERT INTO model1 (id1, id2, col1) VALUES (1, 2, 'B');
INSERT INTO model1 (id1, id2, col1) VALUES (2, 1, 'C');
INSERT INTO model1 (id1, id2, col1) VALUES (2, 2, 'D');

INSERT INTO model2 (id, model1_id1, model1_id2, col1) VALUES (1, 1, 1, 'AB');
INSERT INTO model2 (id, model1_id1, model1_id2, col1) VALUES (2, 1, 1, 'AC');
INSERT INTO model2 (id, model1_id1, model1_id2, col1) VALUES (3, 2, 1, 'AD');
INSERT INTO model2 (id, model1_id1, model1_id2, col1) VALUES (4, 2, 2, 'AE');