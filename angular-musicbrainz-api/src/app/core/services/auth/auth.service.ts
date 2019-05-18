// Angular
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
// RxJS
import { Observable, Subject} from 'rxjs';
import { tap } from 'rxjs/operators';

import { CredentialsService, Credentials } from '@core/services/auth/credentials.service';

interface AuthResponse {
  token: string
}

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

const auth = 'http://localhost:8000/api-auth/'

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  authToken: string;
  usernameSub: Subject<string> = new Subject<string>();
  usernameStr: string;
  isLoggedIn: boolean = false;

  constructor(
    private credentialsService: CredentialsService,
    private http: HttpClient, 
    private router: Router
    ) { }

  loadCreds() {
    let creds = this.credentialsService.credentials
    // let creds = JSON.parse(localStorage.getItem('userCreds'));
    if (creds) {
      this.setUserName(creds.username);
      this.authToken = creds.token;
    }
  }

  logIn(userInfo): Observable<any> {
    const data = {
      username: userInfo.username,
      password: userInfo.password
    }
    return this.http.post<Credentials>(auth + 'login/', data, httpOptions)
      .pipe( 
        tap(res => {
          this.authToken = res.token;
          this.setUserName(userInfo.username);
          if (userInfo.remember) {
            localStorage.setItem('userCreds', JSON.stringify({
              username: userInfo.username,
              token: res.token
            }));
          }
          this.isLoggedIn = true;
        })
      )
  }

  getUsername() {

  }

  sendUsername() {

  }

  private setUserName(name: string) {
    this.usernameStr = name;
    this.usernameSub.next(name);
  }

  getAuthToken() {

  }

  logOut() {

  }

}
