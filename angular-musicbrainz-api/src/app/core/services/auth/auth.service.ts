// Angular
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
// RxJS
import { Observable, Subject} from 'rxjs';

interface AuthResponse {
  token: string
}

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  authToken: string;
  usernameSub: Subject<string> = new Subject<string>();
  usernameStr: string;
  isLoggedIn: boolean = false;

  constructor(private http: HttpClient, private router: Router) { }

  loadCreds() {
    let creds = JSON.parse(localStorage.getItem('userCreds'));
    if (creds) {
      // ..
    }
  }

  logIn(): Observable<any> {
    return null;
  }

  getUsername() {

  }

  sendUsername() {

  }

  private setUserName() {

  }

  getAuthToken() {

  }

  logOut() {
    
  }

}
