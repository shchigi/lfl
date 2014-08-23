INSERT INTO plays_card (id, type, person_id, minute) VALUES (1, 'Y', 1, 24);

INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (1, 2, 3, 0, 1, 11, 0);
INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (2, 2, 1, 0, 1, 15, 0);
INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (3, 3, null, 1, 1, 58, 0);
INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (4, 4, null, 0, 1, 59, 0);

INSERT INTO plays_match (id, date, time, home_team_id, guest_team_id, home_team_score, guest_team_score) VALUES (1, '2014-08-23', '13:47:10.522072', 1, 2, 2, 2);
INSERT INTO plays_match (id, date, time, home_team_id, guest_team_id, home_team_score, guest_team_score) VALUES (2, '2014-08-30', '13:47:10.645406', 2, 1, 0, 0);

INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id) VALUES (1, 'Денис', 'Щигельский', 'B', 1, 0, '2014-08-23', null, '+79151164158', 'denis.shchigelsky@gmail.com', 1);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id) VALUES (2, 'Илья', 'Станиславский', 'H', 1, 0, '2014-08-23', null, '+79670614948', null, 1);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id) VALUES (3, 'Александр', 'Буров', 'F', 1, 1, '2014-08-23', null, '89197711249', null, 1);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id) VALUES (4, 'Ара', 'Ахян', 'F', 1, 1, '2014-08-23', null, '89123711249', null, 2);

INSERT INTO plays_team (id, name, start_date) VALUES (1, 'Физтех', '2014-08-23');
INSERT INTO plays_team (id, name, start_date) VALUES (2, 'Энитайм', '2014-08-23');