import { TestBed } from '@angular/core/testing';

import { ErrorHanlderService } from './error-hanlder.service';

describe('ErrorHanlderService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ErrorHanlderService = TestBed.get(ErrorHanlderService);
    expect(service).toBeTruthy();
  });
});
