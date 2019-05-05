import { TestBed, inject } from '@angular/core/testing';

import { ErrorHanlderService } from './error-hanlder.service';

describe('ErrorHanlderService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    providers: [ErrorHanlderService]
  }));

  it('should be created', inject([ErrorHanlderService], (service: ErrorHanlderService) => {
    expect(service).toBeTruthy();
  }));
});
