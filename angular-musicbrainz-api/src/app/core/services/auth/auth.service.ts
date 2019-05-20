// Angular
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
// RxJS
import { Observable, Subject, of} from 'rxjs';
import { map, tap } from 'rxjs/operators';
// Services
import {
  CredentialsService,
  Credentials
} from '@core/services/auth/credentials.service';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

const backend = 'http://localhost:8000/api-auth/';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  authToken: string;
  usernameSub: Subject<string> = new Subject<string>();
  usernameStr: string;

  constructor(
    private credentialsService: CredentialsService,
    private http: HttpClient,
    private router: Router
    ) { }

  loadCreds() {
    let creds = this.credentialsService.credentials;
    if (creds) {
      this.setUserName(creds.username);
      this.authToken = creds.token;
    }
  }

  login(userInfo): Observable<any> {
    const data = {
      username: userInfo.username,
      password: userInfo.password,
    };
    return this.http.post<Credentials>(backend + 'login/', data, httpOptions)
      .pipe(
        map(res => {
          this.authToken = res.token;
          this.setUserName(userInfo.username);
          this.credentialsService.setCredentials(res, userInfo.remember);
        }),
        tap(() => this.credentialsService.isAuthenticated())
      );
  }

  private setUserName(name: string) {
    this.usernameStr = name;
    this.usernameSub.next(name);
  }

}
