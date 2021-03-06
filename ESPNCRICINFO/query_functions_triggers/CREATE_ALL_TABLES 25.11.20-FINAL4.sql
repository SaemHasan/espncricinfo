--25.11.20
DROP TABLE STAT CASCADE CONSTRAINTS;
DROP TABLE TEAM_STAT CASCADE CONSTRAINTS;
DROP TABLE PLAYER_STAT CASCADE CONSTRAINTS;
DROP TABLE PERSON CASCADE CONSTRAINTS;
DROP TABLE UMPIRE CASCADE CONSTRAINTS;
DROP TABLE COACH CASCADE CONSTRAINTS;
DROP TABLE PLAYER CASCADE CONSTRAINTS;
DROP TABLE GROUND CASCADE CONSTRAINTS;
DROP TABLE SERIES CASCADE CONSTRAINTS;
DROP TABLE TEAM CASCADE CONSTRAINTS;
DROP TABLE MATCH CASCADE CONSTRAINTS;
DROP TABLE PLAYER_SCORE CASCADE CONSTRAINTS;
DROP TABLE UMPIRE_MATCH CASCADE CONSTRAINTS;
DROP TABLE TEAM_PLAYER CASCADE CONSTRAINTS;
DROP TABLE TEAM_MATCH CASCADE CONSTRAINTS;
DROP TABLE TEAM_SERIES CASCADE CONSTRAINTS;
DROP TABLE SERIES_PARTICIPANTS CASCADE CONSTRAINTS;

CREATE TABLE PERSON(
    PERSON_ID VARCHAR2(500 CHAR) PRIMARY KEY,
    FIRST_NAME VARCHAR2(50 CHAR) NOT NULL,
    LAST_NAME VARCHAR2(50 CHAR),
    NATIONALITY VARCHAR2(50 CHAR) NOT NULL,
    DATE_OF_BIRTH DATE,
    IMAGE VARCHAR2(150 CHAR)
);
CREATE TABLE PLAYER(
    PLAYER_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    ROLE VARCHAR2(50 CHAR) NOT NULL,
    BATTING_STYLE VARCHAR2(50 CHAR),
    BOWLING_STYLE VARCHAR2(50 CHAR)
);
CREATE TABLE TEAM(
    TEAM_ID VARCHAR2(50 CHAR) PRIMARY KEY,
    NAME VARCHAR2(50 CHAR) NOT NULL,
    IMAGE VARCHAR2(150 CHAR)
);

CREATE TABLE UMPIRE(
    UMPIRE_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    PLAYER_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID)

);

CREATE TABLE COACH(
    COACH_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    TEAM_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    PLAYER_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    START_YEAR NUMBER NOT NULL,
    START_DATE DATE,
    END_DATE DATE

);



CREATE TABLE GROUND(
    GROUND_ID VARCHAR2(500 CHAR) PRIMARY KEY,
    NAME VARCHAR2(50 CHAR) NOT NULL,
    CITY VARCHAR2(50 CHAR) NOT NULL,
    STREET_NO VARCHAR2(50 CHAR),
    ZIP_CODE NUMBER,
    IMAGE VARCHAR2(150 CHAR)
);

CREATE TABLE SERIES(
    SERIES_ID VARCHAR2(500 CHAR) PRIMARY KEY,
    NAME VARCHAR2(50 CHAR),
    HOST_COUNTRY VARCHAR2(50 CHAR) NOT NULL,
    MOTM VARCHAR2(50 CHAR),
    WINNER VARCHAR2(50 CHAR),
    IMAGE VARCHAR2(150 CHAR)

);



CREATE TABLE MATCH(
    MATCH_ID VARCHAR2(500 CHAR) PRIMARY KEY,
    GROUND_ID VARCHAR2(500 CHAR) REFERENCES GROUND(GROUND_ID),
    SERIES_ID VARCHAR2(500 CHAR) REFERENCES SERIES(SERIES_ID),
    TYPE VARCHAR2(50 CHAR) NOT NULL,
    MOTM VARCHAR2(50 CHAR),
    WEATHER VARCHAR2(50 CHAR),
    WINNER VARCHAR2(50 CHAR),
    TEAM1_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    TEAM2_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    VIDEO VARCHAR2(150 CHAR)
);

CREATE TABLE PLAYER_SCORE(
    MATCH_ID VARCHAR2(500 CHAR) REFERENCES MATCH(MATCH_ID),
    PLAYER_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    SCORED_RUNS NUMBER,
    NUM_OF_BALLS_BATTED NUMBER,
    NUM_OF_FOURS NUMBER,
    NUM_OF_SIXES NUMBER,
    NOT_OUT VARCHAR2(50 CHAR),
    NUM_OF_OVERS_BOWLED NUMBER,
    GIVEN_RUNS NUMBER,
    NUM_OF_WICKETS NUMBER
);

CREATE TABLE UMPIRE_MATCH(
    UMPIRE_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    MATCH_ID VARCHAR2(500 CHAR) REFERENCES MATCH(MATCH_ID)

);

CREATE TABLE TEAM_PLAYER(
    TEAM_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    PLAYER_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID)

);

CREATE TABLE TEAM_MATCH(
    TEAM_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    MATCH_ID VARCHAR2(500 CHAR) REFERENCES MATCH(MATCH_ID),
    MATCH_DATE DATE NOT NULL

);

CREATE TABLE TEAM_SERIES(
    TEAM_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    SERIES_ID VARCHAR2(500 CHAR) REFERENCES SERIES(SERIES_ID),
    START_DATE DATE NOT NULL,
    END_DATE DATE NOT NULL

);

CREATE TABLE SERIES_PARTICIPANTS(
    TEAM_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    SERIES_ID VARCHAR2(500 CHAR) REFERENCES SERIES(SERIES_ID)
);
CREATE TABLE STAT(
    STAT_ID VARCHAR2(500 CHAR) PRIMARY KEY,
    NUM_OF_MATCHES NUMBER DEFAULT 0,
    RATING NUMBER DEFAULT 0

);
CREATE TABLE TEAM_STAT(
    STAT_ID VARCHAR2(500 CHAR) REFERENCES STAT(STAT_ID),
    TEAM_ID VARCHAR2(50 CHAR) REFERENCES TEAM(TEAM_ID),
    TOTAL_WIN NUMBER DEFAULT 0,
    TOTAL_LOSE NUMBER DEFAULT 0,
    NOT_PLAYED NUMBER DEFAULT 0

);
CREATE TABLE PLAYER_STAT(
    STAT_ID VARCHAR2(500 CHAR) REFERENCES STAT(STAT_ID),
    PLAYER_ID VARCHAR2(500 CHAR) REFERENCES PERSON(PERSON_ID),
    SCORED_RUN NUMBER DEFAULT 0,
    NUM_OF_MOTM NUMBER DEFAULT 0,
    NUM_OF_HUNDRED NUMBER DEFAULT 0,
    NUM_OF_FIFTY NUMBER DEFAULT 0,
    TOTAL_RUN NUMBER DEFAULT 0,
    NOT_OUT NUMBER DEFAULT 0,
    AVERAGE_SCORED_RUN NUMBER DEFAULT 0,
    STRIKE_RATE NUMBER DEFAULT 0,
    NUM_OF_WICKETS NUMBER DEFAULT 0,
    NUM_OF_FIVE_WICKETS NUMBER DEFAULT 0,
    NUM_OF_OVERS NUMBER DEFAULT 0,
    GIVEN_RUN NUMBER DEFAULT 0,
    BOWLING_AVG NUMBER DEFAULT 0,
    BOWLING_STRIKE_RATE NUMBER DEFAULT 0

);








