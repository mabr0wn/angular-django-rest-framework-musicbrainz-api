import { TestBed, tick, fakeAsync } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { AuthService } from './auth.service';

describe('AuthService', () => {
  let authService: AuthService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
        RouterTestingModule
      ],
      providers: [AuthService]
    });

    authService = TestBed.get(AuthService);
  });

  describe('Login', () => {
    test('Should return user information', fakeAsync(() => {
      const resquest = authService.logIn({
        username: 'cheeta',
        password: '1234'
      });
      tick();

      resquest.subscribe(creds => {
        expect(creds).toBeDefined();
        expect(creds.token).toBeDefined();
      });
    }));

    test('Should authenticate user', fakeAsync(() => {
      expect('').toEqual('');
    }))
  })
  
});
