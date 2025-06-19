
-- CREATE TABLE Person(
-- 	driver_id INTEGER PRIMARY KEY,
-- 	p_name VARCHAR(100),
-- 	address VARCHAR(100)
-- );

-- CREATE TABLE Car(
-- 	regno VARCHAR(100) PRIMARY KEY,
-- 	model VARCHAR(100) ,
-- 	r_Year DATE
-- );

-- CREATE TABLE Accident(
-- 	reportno INTEGER PRIMARY KEY,
-- 	rep_Date DATE,
-- 	Location VARCHAR(100)
-- );

-- CREATE TABLE Participated (
-- 	driver_id INTEGER ,
-- 	regno VARCHAR(100),
-- 	reportno INTEGER,
--  damage_amt INTEGER,
-- 	FOREIGN KEY(driver_id) REFERENCES Person(driver_id),
-- 	FOREIGN KEY (regno) REFERENCES Car(regno),
-- 	FOREIGN KEY (reportno) REFERENCES Accident(reportno)
-- );

-- CREATE TABLE owns (
-- 	driver_id INTEGER ,
-- 	regno VARCHAR(100),
-- 	FOREIGN KEY(driver_id) REFERENCES Person(driver_id),
-- 	FOREIGN KEY (regno) REFERENCES Car(regno)
-- );


INSERT INTO Person VALUES (0, 'Jenson Button', 'University St');
INSERT INTO Person VALUES (1, 'Rubens Barrichello', '1st Ave');
INSERT INTO Person VALUES (2, 'Sebastian Vettel', '1st Ave');
INSERT INTO Person VALUES (3, 'Mark Webber', '1st Ave');
INSERT INTO Person VALUES (4, 'Lewis Hamilton', '1st Ave');
INSERT INTO Person VALUES (5, 'Felipe Massa', 'University St');


INSERT INTO Car VALUES ('SZM813', 'Honda', TO_DATE('2009', 'YYYY'));
INSERT INTO Car VALUES ('SZM814', 'Toyota', TO_DATE('2009', 'YYYY'));
INSERT INTO Car VALUES ('SZM815', 'BMW', TO_DATE('2009', 'YYYY'));
INSERT INTO Car VALUES ('SZM816', 'Honda', TO_DATE('2009', 'YYYY'));
INSERT INTO Car VALUES ('SZM817', 'Honda', TO_DATE('2008', 'YYYY'));
INSERT INTO Car VALUES ('SZM818', 'BMW', TO_DATE('2008', 'YYYY'));
INSERT INTO Car VALUES ('SZM819', 'BMW', TO_DATE('2008', 'YYYY'));
INSERT INTO Car VALUES ('SZM820', 'Toyota', TO_DATE('2008', 'YYYY'));

INSERT INTO Accident VALUES (1, TO_DATE('2008-04-13', 'YYYY-MM-DD'), 'Monza');
INSERT INTO Accident VALUES (2, TO_DATE('2008-07-22', 'YYYY-MM-DD'), 'Indianapolis');
INSERT INTO Accident VALUES (3, TO_DATE('2008-07-22', 'YYYY-MM-DD'), 'Indianapolis');
INSERT INTO Accident VALUES (4, TO_DATE('2008-07-22', 'YYYY-MM-DD'), 'New York');
INSERT INTO Accident VALUES (5, TO_DATE('2008-07-27', 'YYYY-MM-DD'), 'New York');
INSERT INTO Accident VALUES (6, TO_DATE('2009-01-27', 'YYYY-MM-DD'), 'Highland Heights');
INSERT INTO Accident VALUES (7, TO_DATE('2009-02-15', 'YYYY-MM-DD'), 'Highland Heights');


INSERT INTO owns VALUES (0, 'SZM813');
INSERT INTO owns VALUES (1, 'SZM814');
INSERT INTO owns VALUES (2, 'SZM815');
INSERT INTO owns VALUES (3, 'SZM816');
INSERT INTO owns VALUES (4, 'SZM817');
INSERT INTO owns VALUES (5, 'SZM818');
INSERT INTO owns VALUES (5, 'SZM819');
INSERT INTO owns VALUES (4, 'SZM820');


INSERT INTO Participated VALUES (0, 'SZM813', 1, 4000);
INSERT INTO Participated VALUES (1, 'SZM814', 2, 6000);
INSERT INTO Participated VALUES (4, 'SZM815', 3, 6000);
INSERT INTO Participated VALUES (1, 'SZM814', 4, 1000);
INSERT INTO Participated VALUES (4, 'SZM817', 5, 6000);
INSERT INTO Participated VALUES (5, 'SZM815', 6, 5000);
INSERT INTO Participated VALUES (0, 'SZM819', 7, 5000);
INSERT INTO Participated VALUES (4, 'SZM817', 4, 3000);
INSERT INTO Participated VALUES (3, 'SZM813', 5, 4000);
INSERT INTO Participated VALUES (3, 'SZM814', 6, 2000);
INSERT INTO Participated VALUES (1, 'SZM814', 7, 1000);
INSERT INTO Participated VALUES (4, 'SZM820', 7, 6000);
INSERT INTO Participated VALUES (3, 'SZM813', 7, 4000);


-- Write a SQL query to update the damage amount for the car with a specific
-- register number in the accident with report number between 1 & 5.

-- RegisterNumber -> reportNo -> -
UPDATE Participated
SET damage_amt = 7500
where regno ='SZM813'
AND reportno BETWEEN 1 AND 5;

SELECT * FROM Participated;



-- iv) Query to find the total number of people who owned the cars that were
-- involved in accidents in 2008


SELECT * FROM PERSON p
JOIN owns o on o.driver_id = p.driver_id
join participated pr on  pr.regno = o.regno
join accident a on a.reportno = pr.reportno
WHERE EXTRACT(YEAR FROM a.rep_date) = 2008;


-- Query to check if a person with a specific driver_id has met with an accident
-- in 2009.
SELECT DISTINCT p.driver_id, p.p_name
FROM Person p
JOIN Participated pa ON p.driver_id = pa.driver_id
JOIN Accident a ON pa.reportno = a.reportno
WHERE EXTRACT(YEAR FROM a.rep_date) = 2009
  AND p.driver_id = 3;  -- Change 3 to the driver_id you want to check



