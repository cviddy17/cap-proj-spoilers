SELECT s.id, s.name
FROM students s JOIN applications a on s.id=a.stud_id
WHERE a.date < "2014-06-01";

SELECT c.id, c.name, COUNT(s.id) as cnt
FROM companies c JOIN applications a, students s
ON c.id = a.comp_id AND s.id = a.stud_id;
