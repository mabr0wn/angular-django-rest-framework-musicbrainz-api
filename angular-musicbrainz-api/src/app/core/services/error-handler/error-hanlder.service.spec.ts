import { ErrorHandler, ReflectiveInjector } from '@angular/core';
import { TestBed, inject } from '@angular/core/testing';

import { ErrorHanlderService } from './error-hanlder.service';

describe('ErrorHanlderService', () => {
  let handler: ErrorHanlderService;

  beforeEach(() => TestBed.configureTestingModule({
    providers: [
      { provide: ErrorHandler, useClass: ErrorHanlderService }
    ]
  }));

  it('should be created', inject([ErrorHanlderService], (service: ErrorHanlderService) => {
    expect(service).toBeTruthy();
  }));
});
