import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { User } from '../models/user';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  newUser: User = new User();
  invalido?: boolean;
  constructor(private http: HttpClient, private router: Router)
  {

  }
  ngOnInit()
  {
    this.invalido = false;
  }
  register()
  {
    this.invalido = false
    let body = {
      "username": this.newUser.username,
      "password": this.newUser.password,
      "firstName": this.newUser.firstName,
      "lastName":  this.newUser.lastName,
      "email":  this.newUser.email
    }
    this.http.post("/api/v1/user/", body).subscribe((data)=>{
      // localStorage.setItem("username", this.login.username)
      // localStorage.setItem("password", this.login.password)
      
      console.log(data)

    },
    (error)=>{
      this.invalido = true
      console.log(error)
    })
  }

}
