import {
  fakeAsync,
  TestBed,
  tick
} from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClient} from '@angular/common/http';
// RxJS
import { of } from 'rxjs';
import { AuthService } from './auth.service';
// Credentials
import { CredentialsService, Credentials } from './credentials.service';
import { MockCredentialsService } from './__mocks__/credentials.service.mock';


describe('AuthService', () => {
  let authService: AuthService;
  let credentialsService: MockCredentialsService;

  const http = {
    post: jest.fn()
  };

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule
      ],
      providers: [
        AuthService,
        { provide: CredentialsService, useClass: MockCredentialsService },
        { provide: HttpClient, useValue: http }
      ]
    });

    authService = TestBed.get(AuthService);
    credentialsService = TestBed.get(CredentialsService)
    credentialsService.credentials = null;

  });

  describe('Login', () => {
    test('Should return user information', fakeAsync(() => {
      // nothing should post yet
      expect(http.post).not.toHaveBeenCalled();
      // mocked data
      const data = {
        username: 'cheeta',
        password: '1234'
      };
      // wait...
      tick();
      // mock url
      let argUrl: string;
      // mock url post
      http.post.mockImplementation(
        (url) => { argUrl = url; return of([]);
      });
      // subscribe to mocked data...
      authService.login(data).subscribe();
      // expect post to been called one time.
      expect(http.post).toHaveBeenCalledTimes(1);
      // mock url should contain login...
      expect(argUrl).toContain('login/');
    }));
    test('Should Authenticate user', fakeAsync(() => {
      expect(credentialsService.isAuthenticated()).toBe(false);

      const spy = jest.spyOn(credentialsService, 'setCredentials');
      const isAuthenticated = credentialsService.setCredentials();

      // Act
      const data = {
        username: 'toto',
        password: '123',
      };
      tick();

      authService.login(data).subscribe();

      expect(credentialsService.isAuthenticated()).toBe(true);
      expect(credentialsService.credentials).not.toBeNull();
      // expect((<Credentials>credentialsService.credentials).token).toBeDefined();
      // expect((<Credentials>credentialsService.credentials).token).not.toBeNull();
      // Assert
      // request.subscribe(() => {

      // });
    }))
  });
});
