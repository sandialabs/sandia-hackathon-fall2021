/* Copyright 2019 National Technology & Engineering Solutions of Sandia, LLC (NTESS). 
   Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains 
   certain rights in this software.
*/

class UserModel {
  final String username;
  final String password;
  final int id;
  final String firstName;
  final String lastName;
  final String email;
  final int userStatus;

  UserModel(
      {this.username,
      this.password,
      this.id,
      this.firstName,
      this.lastName,
      this.email,
      this.userStatus});

  factory UserModel.fromJson(final json) {
    return UserModel(
        username: json['username'],
        password: json['password'],
        id: json['id'],
        firstName: json['firstName'],
        lastName: json['lastName'],
        email: json['email'],
        userStatus: json['userStatus']);
  }
}
