import { Component, OnInit } from '@angular/core';
import { Workout } from '../models/workout';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-workouts',
  templateUrl: './workouts.component.html',
  styleUrls: ['./workouts.component.css']
})
export class WorkoutsComponent implements OnInit {

  constructor(private http: HttpClient, private router: Router) { }
  add: boolean = false;
  newWorkout: Workout = new Workout();
  listOfWorkouts: any
  ngOnInit(): void {
    this.listOfWorkouts = [
      {
          "id": 1,
          "nickname": "Thursday Abs",
          "ownerId": 2
      },
      {
          "id": 2,
          "nickname": "MondayCardio",
          "ownerId": 2
      }
  ]
    this.newWorkout.ownerId = localStorage.getItem("userId") || ''
    // this.http.get("/api/v1/workout/owner/"+this.newWorkout.ownerId).subscribe((data)=>{
    //   this.listOfWorkouts = Object.values(data)[0]
    //   console.log(data)
    // })
  }
  addNew()
  {
    this.add = true
  }
  addWorkout()
  {
    this.add = false
    this.listOfWorkouts.push(this.newWorkout)
    // this.http.post("/api/v1/workout/", this.newWorkout).subscribe((data)=>{
    //   this.router.navigate(["/workouts"])
    //   console.log(data)
    // },
    // (error)=>{
    //   console.log(error)
    // })
  }
}

