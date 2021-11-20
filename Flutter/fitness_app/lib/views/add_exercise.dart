/* Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
   Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
   certain rights in this software.
*/
import 'dart:convert';
//import 'dart:html';
//import 'package:fitness_app/UserModel.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'signup.dart';
import 'exercises.dart';
import 'dart:developer';
import 'navigation.dart';
import 'Plans.dart';
import '../globals.dart' as global;

// Controllers
TextEditingController nameController = new TextEditingController();
TextEditingController descriptionController = new TextEditingController();
String impact;
String intensity;
String category;

class AddState extends StatefulWidget {
  @override
  State<AddState> createState() => _AddExercises();
}

class _AddExercises extends State<AddState> {
  TextStyle style = TextStyle(fontFamily: 'Montserrat', fontSize: 20.0);

  @override
  Widget build(BuildContext context) {
    final nameField = TextField(
      controller: nameController,
      obscureText: false,
      style: style,
      decoration: InputDecoration(
          contentPadding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
          hintText: "Name of Exercise",
          border:
              OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))),
    );
    final descriptionField = TextField(
      controller: descriptionController,
      obscureText: false,
      style: style,
      decoration: InputDecoration(
          contentPadding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
          hintText: "Describe the Exercise",
          border:
              OutlineInputBorder(borderRadius: BorderRadius.circular(32.0))),
    );
    final impactField = DropdownButton<String>(
      value: impact,
      icon: const Icon(Icons.arrow_downward),
      iconSize: 24,
      elevation: 16,
      style: const TextStyle(color: Colors.deepPurple),
      underline: Container(
        height: 2,
        color: Colors.deepPurpleAccent,
      ),
      onChanged: (String newValue) {
        setState(() {
          impact = newValue;
        });
      },
      items: <String>['Low', 'Medium', 'High']
          .map<DropdownMenuItem<String>>((String value) {
        return DropdownMenuItem<String>(
          value: value,
          child: Text(value),
        );
      }).toList(),
    );
    final intensityField = DropdownButton<String>(
      value: intensity,
      icon: const Icon(Icons.arrow_downward),
      iconSize: 24,
      elevation: 16,
      style: const TextStyle(color: Colors.deepPurple),
      underline: Container(
        height: 2,
        color: Colors.deepPurpleAccent,
      ),
      onChanged: (String newValue) {
        setState(() {
          intensity = newValue;
        });
      },
      items: <String>['Low', 'Medium', 'High']
          .map<DropdownMenuItem<String>>((String value) {
        return DropdownMenuItem<String>(
          value: value,
          child: Text(value),
        );
      }).toList(),
    );
    final categoryField = DropdownButton<String>(
      value: category,
      icon: const Icon(Icons.arrow_downward),
      iconSize: 24,
      elevation: 16,
      style: const TextStyle(color: Colors.deepPurple),
      underline: Container(
        height: 2,
        color: Colors.deepPurpleAccent,
      ),
      onChanged: (String newValue) {
        setState(() {
          category = newValue;
        });
      },
      items: <String>['strength', 'flexibility', 'endurance']
          .map<DropdownMenuItem<String>>((String value) {
        return DropdownMenuItem<String>(
          value: value,
          child: Text(value),
        );
      }).toList(),
    );
    final addButon = Material(
      elevation: 5.0,
      borderRadius: BorderRadius.circular(30.0),
      color: Color(0xff01A0C7),
      child: MaterialButton(
        minWidth: MediaQuery.of(context).size.width,
        padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
        onPressed: () {
          getLogin(context);
        },
        child: Text("AddExercise",
            textAlign: TextAlign.center,
            style: style.copyWith(
                color: Colors.white, fontWeight: FontWeight.bold)),
      ),
    );

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
                SizedBox(
                  height: 155.0,
                  child: Image.asset(
                    "assets/logo.png",
                    fit: BoxFit.contain,
                  ),
                ),
                SizedBox(height: 20.0),
                nameField,
                SizedBox(height: 20.0),
                descriptionField,
                SizedBox(
                  height: 20.0,
                ),
                SizedBox(height: 20.0),
                Text("Impact"),
                impactField,
                SizedBox(height: 20.0),
                Text("Intensity"),
                intensityField,
                SizedBox(
                  height: 20.0,
                ),
                Text("Category"),
                categoryField,
                SizedBox(
                  height: 20.0,
                ),
                addButon,
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

getLogin(BuildContext context) async {
  var queryParameters = {
    'name': nameController.text,
    'description': descriptionController.text,
    'impact': impact,
    'intensity': intensity,
    'category': category
  };
  final Uri url = Uri.http(global.serverUrl, "/api/v1/exercises/");
  log(url.toString());
  http.post(url,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      body: jsonEncode(queryParameters));
}
