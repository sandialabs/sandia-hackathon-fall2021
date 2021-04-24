/* Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
   Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
   certain rights in this software.
*/

import 'dart:developer';
import 'package:flutter/material.dart';
import '../globals.dart' as global;

class Exercises extends StatelessWidget {
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
                Text("Exercises",
                    textAlign: TextAlign.center,
                    style: TextStyle(fontWeight: FontWeight.bold)),
                SizedBox(
                  height: 20.0,
                ),
                SizedBox(
                    height: 150.0,
                    child: GestureDetector(
                      onTap: () {
                        log("TEST");
                      },
                      /*child: Image.asset('assets/muscle.jpg',
                            fit: BoxFit.contain)*/
                    )),
                Text("Strength",
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
                      /*child: Image.asset('assets/stretch.png',
                            fit: BoxFit.contain)*/
                    )),
                Text("Flexibility",
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
                      /*child: Image.asset('assets/cardio.jpg',
                            fit: BoxFit.contain)*/
                    )),
                Text("Endurance",
                    textAlign: TextAlign.center,
                    style: TextStyle(fontWeight: FontWeight.bold)),
                SizedBox(
                  height: 15.0,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
