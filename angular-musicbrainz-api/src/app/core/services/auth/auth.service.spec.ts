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
import { CredentialsService } from './credentials.service';
import { MockCredentialsService } from './mocks/credentials.service.mock';


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
    credentialsService = TestBed.get(CredentialsService);
    credentialsService.credentials = null;

  });

  afterEach(() => {
    jest.resetModules()
  })

  describe('Login', () => {
    test('Should mock http post for user login', fakeAsync(() => {
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
        (url) => { argUrl = url; return of(data);
      });
      // subscribe to mocked data...
      authService.login(data).subscribe(() => {
        // expect post to been called one time.
        expect(http.post).toHaveBeenCalledTimes(1);
        // mock url should contain login...
        expect(argUrl).toMatchSnapshot('login/');
      });
    }));
    test('Should Authenticate user', fakeAsync(() => {
      expect(credentialsService.isAuthenticated()).toBe(false);
      // Mock
      const data = {
        username: 'cheeta',
        password: '1234',
      };
      tick();

      authService.login(data).subscribe(() => {
        expect(credentialsService.isAuthenticated()).toMatchSnapshot(true);
        expect(credentialsService.credentials).not.toBeNull();
      });
    }));
    test('Should obtain credentials for the session', fakeAsync(() => {
      const spy = jest.spyOn(credentialsService, 'setCredentials');
      const isAuthenticated = credentialsService.setCredentials;
      // Mock
      const data = {
        username: 'cheeta',
        password: '1234'
      };
      tick();

      authService.login(data).subscribe(() => {
        expect(isAuthenticated).toMatchSnapshot();
        expect(spy.mock.calls[0][0]).toMatchSnapshot();
      });
    }));
    test('should obtain and remember credentials across session', fakeAsync(() => {
      const spy = jest.spyOn(credentialsService, 'setCredentials');
      const isAuthenticated = credentialsService.setCredentials;
      // Mock
      const data = {
        username: 'cheeta',
        password: '1234',
        remember: true
      };
      tick();

      authService.login(data).subscribe(() => {
        expect(isAuthenticated).toMatchSnapshot();
        expect(spy.mock.calls[0][1]).toMatchSnapshot(true);
      });
    }));
    test('should remove user authentication', fakeAsync(() => {

      // Mock
      const data = {
        username: 'cheeta',
        password: '1234',
      };
      tick();

      authService.login(data).subscribe(() => {
        expect(credentialsService.isAuthenticated()).toBe(true);

        const request = authService.logout();
        tick();

        request.subscribe(() => {
          expect(credentialsService.isAuthenticated()).toMatchSnapshot(false);
          expect(credentialsService.credentials).toBeNull();
        });
      });
    }));
  });
});
