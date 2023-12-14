-- Creates an index on the names table using the
-- first letter of name(s) and the score
CREATE INDEX idx_name_first_score ON names(names(1), score);
