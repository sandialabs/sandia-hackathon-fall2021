import { Component } from '@angular/core';
import { Login } from '../models/login';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';
import { isNumber } from 'util';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
    login: Login = new Login();
    invalido?: boolean;
    constructor(private http: HttpClient, private router: Router)
    {

    }
    ngOnInit()
    {
      this.invalido = false;
    }
    autenticar()
    {
      this.invalido = false
      let body = {
        "username": this.login.username,
        "password": this.login.password
      }
      this.http.post("/api/v1/user/login", body).subscribe((data)=>{
        let val = Object.values(data)[0]
        if(typeof val === "number")
        {
          this.invalido = false
          localStorage.setItem("userId", val.toString())
          this.router.navigate(["/workouts"])
        }
        else
          this.invalido = true
        console.log(val)

      },
      (error)=>{
        this.invalido = true
        console.log(error)
      })
    }
}
