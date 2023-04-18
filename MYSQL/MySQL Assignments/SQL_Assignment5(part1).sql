CREATE DATABASE SQL_ASSIGN5;
USE SQL_ASSIGN5;

CREATE TABLE EMP
(SNO INT, NAME VARCHAR(20), EID VARCHAR(6), ADDR VARCHAR(50), CITY VARCHAR(10), PHONE VARCHAR(11), EMAIL_ID VARCHAR(50));
 

INSERT INTO EMP(SNO, NAME, EID, ADDR, CITY, PHONE, EMAIL_ID)
VALUES(1, 'Suman', 'E0001', 'Sansar pokhar lahisarai bihar', 'Patna', 8294446839, 'sumansourabh096@gmail.com');

INSERT INTO EMP(SNO, NAME, EID, ADDR, CITY, PHONE, EMAIL_ID)
VALUES(2, 'Ravi', 'E0002', 'Ashok Nagar,MP', 'Bhopal', 7004507029, 'ravitiwari088@yahoo.com');

INSERT INTO EMP
VALUES(3, 'Sourabh', 'E0003', 'Nagavara, karnataka', 'Bangalore', 2346789000, 'saurav.s031996@gmail.com');

INSERT INTO EMP
VALUES(4, 'Shekhar', 'E0004', 'Defence Colony,Mumbai', 'Pune', 6667778880, 'shekhar17.4@yahoo.com');

Insert INTO EMP
VALUES(5, 'Manu', 'E0005', 'Rammurthy Nagar, chennai', 'Kerala', 7774443568, 'manugreat@gmail.com');

INSERT INTO EMP
VALUES(6, 'Pawan', 'E0006', 'Gokuldham Nagar, Goregao', 'Delhi', 1112223334, 'pawankhode@yahoo.com');

INSERT INTO EMP
VALUES(7, 'Venkat Gopal', 'E0007', 'Muttur', 'Kerala', 2223323453, 'venkatgopal093@gmail.com');

INSERT INTO EMP
VALUES(8, 'Venu Iyyer', 'E0008', 'Rameswaram', 'Tamil Nadu', 2344566789, 'venugpliyr@yahoo.com');

INSERT INTO EMP
VALUES(9, 'Parvati', 'E0009', 'Kankarbagh, bihar', 'Patna', 1000380094, 'parvati2242@gmail.com');

INSERT INTO EMP (SNO, NAME, EID, ADDR, CITY, PHONE, EMAIL_ID)
VALUES(10, 'Priya Singh', 'E0010', 'banka, Bihar', 'Bhagalpur', 1002003004, 'Priy.s03@yahoo.com');

SELECT * FROM EMP;



CREATE TABLE EMP_SAL
(S_NO INT, NAME VARCHAR(15), DESI VARCHAR(20), DEPT VARCHAR(20),DOJ DATE, SALARY BIGINT);

ALTER TABLE EMP_SAL 
ADD BONUS BIGINT;

INSERT INTO EMP_SAL
VALUES(1, 'Suman', 'AI Engineer', 'IT', '06-JUNE-2019', 180000, 30000, 10000);

INSERT INTO EMP_SAL
VALUES(2, 'Ravi', 'Marketing Manager', 'Sales and Marketing', '15-JAN-2016', 150000, 15000, 7000);

INSERT INTO EMP_SAL
VALUES(3, 'Sourabh', 'HR Specialist', 'HR', '20-FEB-2020', 90000, 20000, 7000);

INSERT INTO EMP_SAL
VALUES(4, 'Shekhar', 'Finance Analyst', 'Finance', '25-MAY-2020', 180000, 50000, 8000);

INSERT INTO EMP_SAL
VALUES(5, 'Manu', 'SDE', 'IT', '19-OCT-2020',  35000, 12000, 6000);

INSERT INTO EMP_SAL
VALUES(6, 'Pawan', 'SDE', 'IT', '20-JULY-2020', 35000, 12000, 6000 );

INSERT INTO EMP_SAL
VALUES(7, 'Venkat Gopal', 'HR Specialist', 'HR', '16-AUG-2022', 120000, 20000, 12000);

INSERT INTO EMP_SAL
VALUES(8, 'Venu Iyyer', 'Supply Chain Analyst', 'Supply Chain Management', '5-MAR-2022', 200000, 70000,15000);

INSERT INTO EMP_SAL
VALUES(9, 'Parvati', 'Finance Analyst', 'Finance', '30-JULY-2018', 180000, 50000,10000);

INSERT INTO EMP_SAL
VALUES(10, 'Priya Singh', 'SDE', 'IT', '17-NOV-2017', 120000, 15000, 6000);


SELECT * FROM EMP_SAL;
SELECT * FROM EMP;

SELECT EMP.NAME, EMP.EID, EMP.CITY, EMP_SAL.DOJ, EMP_SAL.DEPT, EMP_SAL.DESI, EMP_SAL.SALARY 
FROM EMP
FULL JOIN EMP_SAL
ON EMP.NAME = EMP_SAL.NAME
WHERE CITY = 'DELHI';


