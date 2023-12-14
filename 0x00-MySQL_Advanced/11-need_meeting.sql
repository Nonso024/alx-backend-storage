-- Script creates a view for students under
-- 80 since last month's meeting
DROP VIEW need_meeting;
CREATE VIEW need_meeting AS SELECT name FROM students
WHERE score < 80 AND
(last_meeting IS NULL OR last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH));
