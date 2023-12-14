-- validatimg email using the database
DROP TRIGGER IF EXISTS check_email;
DELIMITER ||
CREATE TRIGGER check_email
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF OLD.email != New.email THEN
			SET New.valid_email = 0;
		ELSE
			SET New.valid_email = New.valid_email;
		END IF;
	END ||
DELIMITER ;
