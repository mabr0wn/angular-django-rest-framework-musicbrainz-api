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

  login(userInfo): Observable<any> {
    const data = {
      username: userInfo.username,
      password: userInfo.password,
    };
    return this.http.post<Credentials>(backend + 'login/', data, httpOptions)
      .pipe(
        map(res => {
          this.authToken = res.token;
          this.setUsername(userInfo.username);
          this.credentialsService.setCredentials(res, userInfo.remember);
        }),
        tap(() => this.credentialsService.isAuthenticated())
      );
  }

  private setUsername(name: string) {
    this.usernameStr = name;
    this.usernameSub.next(name);
  }

  /**
   * Logs out the user and clear credentials.
   * @return True if the user was logged out successfully.
   */
  logout(): Observable<boolean> {
    this.authToken = null;
    this.setUsername(null);
    this.router.navigate(['/']);
    this.credentialsService.setCredentials();
    return of(true);
  }
}
