/* Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
   Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
   certain rights in this software.
*/

import 'dart:developer';
import 'package:flutter/material.dart';
import '../globals.dart' as global;
import 'exercises.dart';

class Navigation extends StatelessWidget {
  @override
  TextStyle style = TextStyle(fontFamily: 'Montserrat', fontSize: 20.0);

  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          color: Colors.white,
          child: Padding(
            padding: const EdgeInsets.all(36.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text("My Fitness App",
                    textAlign: TextAlign.center,
                    style:
                        TextStyle(fontWeight: FontWeight.bold, fontSize: 25)),
                SizedBox(
                  height: 20.0,
                ),
                SizedBox(
                    height: 150.0,
                    child: GestureDetector(
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) {
                                return Exercises();
                              },
                            ),
                          );
                        },
                        child: Image.asset('assets/muscle.jpg',
                            fit: BoxFit.contain))),
                Text("Exercises",
                    textAlign: TextAlign.center,
                    style: TextStyle(fontWeight: FontWeight.bold)),
                SizedBox(
                  height: 50.0,
                ),
                SizedBox(
                    height: 150.0,
                    child: GestureDetector(
                        onTap: () {
                          log("TEST");
                        },
                        child: Image.asset('assets/stretch.jpg',
                            fit: BoxFit.contain))),
                Text("My workouts",
                    textAlign: TextAlign.center,
                    style: TextStyle(fontWeight: FontWeight.bold)),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
