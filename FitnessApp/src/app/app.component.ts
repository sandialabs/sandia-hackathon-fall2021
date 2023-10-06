import { Component } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'applicacion-final';

  constructor(private http: HttpClient)
  {
    // const params = new HttpParams().set('username', 'admin').set('password', 'admin123');
    // const httpOptions = {
    //   headers: new HttpHeaders({
    //     'Content-Type':  'application/json',
    //     'Authorization': 'Basic ' + btoa('coordinador:coordinador123')
    //   })
    // };
    // this.http.get("/api/v1/libros", httpOptions).subscribe((data)=>{
    //   console.log(data)
    // })
  }

  //Registration page as a student
  
}
