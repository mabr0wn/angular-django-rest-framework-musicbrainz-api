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

describe('AuthService', () => {
  let authService: AuthService;

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
        { provide: HttpClient, useValue: http }
      ]
    });

    authService = TestBed.get(AuthService);
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
      authService.logIn(data).subscribe();
      // expect post to been called one time.
      expect(http.post).toHaveBeenCalledTimes(1);
      // mock url should contain login...
      expect(argUrl).toContain('login/');
    }));
  });
});
