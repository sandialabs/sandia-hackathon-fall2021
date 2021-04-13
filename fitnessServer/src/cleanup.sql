-- Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
-- Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
-- certain rights in this software.
USE fitnessDemo;
DROP TABLE IF EXISTS ExerciseWorkoutLinks;
DROP TABLE IF EXISTS Goals;
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS Workouts;
DROP TABLE IF EXISTS Users;

DROP VIEW IF EXISTS FullLinkView;

DROP DATABASE IF EXISTS fitnessDemo;