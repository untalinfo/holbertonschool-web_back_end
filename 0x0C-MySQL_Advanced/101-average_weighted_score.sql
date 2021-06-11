-- Average weighted score
--
delimiter //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	SET average_score = (SELECT sum(p.weight * c.score) / sum(p.weight)
						 FROM projects AS p
						 INNER JOIN corrections AS c
							ON p.id = c.project_id
                         WHERE c.user_id = users.id);
END;
//