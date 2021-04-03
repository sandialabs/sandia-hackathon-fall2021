CREATE DATABASE IF NOT EXISTS fitnessDemo;
USE fitnessDemo;
CREATE TABLE IF NOT EXISTS Exercises(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    description VARCHAR(150),
    impact VARCHAR(10),
    intensity VARCHAR(10),
    category VARCHAR(15),
    PRIMARY KEY(id)
);

INSERT INTO Exercises(name, description, impact, intensity, category) 
VALUES ('Weights','Freeweights for arm workouts', 'low', 'high', 'strength');
INSERT INTO Exercises(name, description, impact, intensity, category) 
VALUES ('Treadmill','That thing that makes you lungs hurt','medium','high','endurance');
INSERT INTO Exercises(name, description, impact, intensity, category) 
VALUES ('Yoga','Slow breathing, long stretches','low','low','flexibility');

CREATE TABLE IF NOT EXISTS Users(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(75),
    password VARCHAR(50) NOT NULL,
    userStatus INT NOT NULL,
    PRIMARY KEY(id)
);
INSERT INTO Users(username, firstName,lastName,email,password,userStatus)
VALUES ('root', 'Administrator','Account','god@google.com','abc123',0);
INSERT INTO Users(username, firstName,lastName,email,password,userStatus)
VALUES ('user1', null,null,null,'abc123',0);

CREATE TABLE IF NOT EXISTS Workouts (
    id INT NOT NULL AUTO_INCREMENT,
    nickname VARCHAR(100),
    ownerId INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(ownerId) REFERENCES Users(id)
);
INSERT INTO Workouts(nickname,ownerId)
VALUES('Thursday Abs',2);
INSERT INTO Workouts(nickname,ownerId)
VALUES('MondayCardio',2);
INSERT INTO Workouts(nickname,ownerId)
VALUES('Around the World Muscles',1);

CREATE TABLE IF NOT EXISTS Goals(
    id INT NOT NULL AUTO_INCREMENT,
    linkId INT NOT NULL,
    numReps INT,
    numSets INT,
    ownerId INT NOT NULL,
    weight INT,
    duration INT,
    PRIMARY KEY(id),
    FOREIGN KEY(ownerId) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS ExerciseWorkoutLinks(
    id INT NOT NULL AUTO_INCREMENT,
    exerciseId INT NOT NULL,
    workoutId INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(exerciseId) REFERENCES Exercises(id),
    FOREIGN KEY(workoutId) REFERENCES Workouts(id)
);

INSERT INTO ExerciseWorkoutLinks(exerciseId,workoutId)
VALUES(1,3);
INSERT INTO Goals(linkId, numReps, numSets, ownerId, weight, duration) 
VALUES(1, 10, 5, 2, 25, null);

INSERT INTO ExerciseWorkoutLinks(exerciseId,workoutId)
VALUES(3,3);
INSERT INTO Goals(linkId, numReps, numSets, ownerId, weight, duration) 
VALUES(2, null, null, 2, null, 45);

CREATE OR REPLACE VIEW FullLinkView (ExerciseName, User, NumReps, NumSets, Weight, Duration)
as
(SELECT ex.name, u.username, g.numReps, g.numSets, g.weight, g.duration FROM ExerciseWorkoutLinks as e
INNER JOIN Exercises as ex on ex.id = e.exerciseId
INNER JOIN Workouts as w on e.workoutId = w.id
INNER JOIN Goals as g on g.linkId = e.id
INNER JOIN Users as u on g.ownerId = u.id);