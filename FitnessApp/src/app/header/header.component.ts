import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  role: any;

  constructor(private router: Router)
  {

  }
  ngOnInit()
  {
  }
  ngAfterViewChecked()
  {
    
    this.role = localStorage.getItem("role")
  }
  isLoggedIn()
  {
    if(localStorage.getItem("userId"))
      return true
    return false
  }
  logout()
  {
    localStorage.removeItem("userId")
    this.router.navigate(["/login"])
  }
}
