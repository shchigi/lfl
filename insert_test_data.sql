INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$12000$nyuwydxEqnDw$yx+FKGvjQkoBQtm8e3BAUGekmvaZd4FdSNl54L3cqVk=', '2014-09-14 16:15:59.287623', 1, 'rakot', '', '', '', 1, 1, '2014-09-14 14:14:37.713147');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$12000$qJTtRfZjdnxf$nxsoNI+5riMM7PnE7+URm3di4EG6sDg6WWoX6ZB9eAU=', '2014-09-14 16:16:32', 0, 'stanis', '', '', '', 0, 1, '2014-09-14 16:16:32');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (3, 'pbkdf2_sha256$12000$VeyxuIkl5a5S$NjmNHlvTd1dJ/LIYKhc5E3NE8c1Z8qrZm+AEF+d8D3U=', '2014-09-14 16:17:06', 0, 'demid', '', '', '', 0, 1, '2014-09-14 16:17:06');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (4, 'pbkdf2_sha256$12000$1aWSY1R42I9t$s91nVqPsWwgodcxlTRHAit7WB1popTDpXUmkd0rzMtc=', '2014-09-14 16:56:27.027438', 0, 'burov', '', '', '', 0, 1, '2014-09-14 16:56:27.027468');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (5, 'pbkdf2_sha256$12000$DmMpbLoTLRXw$o9dZkxm3qoYBYTkf5wSxVtOI9SroYXxSyjQVQqXS8Vs=', '2014-09-14 16:58:20.426204', 0, 'ara', '', '', '', 0, 1, '2014-09-14 16:58:20.426234');


INSERT INTO plays_team (id, name, start_date) VALUES (1, 'Физтех', '2014-08-23');
INSERT INTO plays_team (id, name, start_date) VALUES (2, 'Энитайм', '2014-08-23');

INSERT INTO plays_match (id, date, time, home_team_id, guest_team_id, home_team_score, guest_team_score) VALUES (1, '2014-08-23', '13:47:10', 1, 2, 2, 1);
INSERT INTO plays_match (id, date, time, home_team_id, guest_team_id, home_team_score, guest_team_score) VALUES (2, '2014-08-30', '13:47:10.645406', 2, 1, 1, 0);

INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id, user_id) VALUES (1, 'Денис', 'Щигельский', 'B', 1, 0, '2014-08-23', null, '+79151164158', 'denis.shchigelsky@gmail.com', 1, 1);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id, user_id) VALUES (5, 'Демид', 'Сычев', 'H', 1, 0, '2014-09-13', 2014-09-13, '89123711249', '', 1, 3);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id, user_id) VALUES (2, 'Илья', 'Станиславский', 'H', 1, 0, '2014-08-23', null, '+79670614948', '', 1, 2);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id, user_id) VALUES (3, 'Александр', 'Буров', 'F', 1, 1, '2014-08-23', null, '89197711249', '', 1, 4);
INSERT INTO plays_person (id, first_name, last_name, position, is_active, is_captain, start_date, finish_date, cell_phone, email, team_id, user_id) VALUES (4, 'Ара', 'Ахян', 'F', 1, 1, '2014-08-23', null, '89123711249', '', 2, 5);

INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (2, 2, 1, 0, 1, 15, 0);
INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (3, 3, null, 1, 1, 58, 0);
INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (6, 2, 3, 0, 1, null, 0);
INSERT INTO plays_goal (id, player_scored_id, player_assisted_id, own_goal, match_id, minute, is_penalty) VALUES (8, 4, null, 0, 2, null, 0);

INSERT INTO plays_card (id, type, person_id, minute) VALUES (1, 'Y', 1, 24);

INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (1, 2, 1);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (2, 2, 2);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (3, 4, 1);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (4, 4, 2);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (5, 3, 1);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (6, 3, 2);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (7, 1, 1);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (8, 1, 2);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (9, 5, 1);
INSERT INTO plays_person_matches_played (id, person_id, match_id) VALUES (10, 5, 2);

INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (1, 2, 1);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (2, 2, 2);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (3, 4, 1);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (4, 4, 2);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (5, 3, 1);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (6, 3, 2);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (7, 1, 1);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (8, 1, 2);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (9, 5, 1);
INSERT INTO plays_person_matches_intended (id, person_id, match_id) VALUES (10, 5, 2);
