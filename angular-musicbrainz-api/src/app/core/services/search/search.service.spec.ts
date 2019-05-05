import { TestBed, inject } from '@angular/core/testing';
import { HttpClient, HttpParams } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing'


import { of } from 'rxjs';

import { SearchService } from './search.service';
import { ErrorHanlderService } from '../error-handler/error-hanlder.service';
import { Album } from '../../models/album';

describe('SearchService', () => {  
  let service: SearchService;
  let http: HttpClient;
  let spy: any;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers:[
        SearchService,
        { provide: HttpClient, useValue: { get: jest.fn() } },
        {provide: ErrorHanlderService }
      ]
    })
    http = TestBed.get(HttpClient);
    service = TestBed.get(SearchService);

    // Mock implementation of console.error to
    // return undefined to stop printing out to console log during test
    jest.spyOn(console, 'error').mockImplementation(() => undefined)
  });

  it('should create an instance successfully', () => {
    expect(service).toBeDefined();
  });

  describe('',() => {
    it('calls external api with supplied query value and field', inject([SearchService], (service: SearchService) => {
      expect(http.get).not.toHaveBeenCalled();

      let argUrl: string;
      let argOptions: {params: HttpParams};
      spy = spyOn(service,'searchAlbums').and.callFake(
        (url, options) => { argUrl = url; argOptions = options; return of([])
      });
      const testValue = 'testValue';
      const testField = 'testField';
      service.searchAlbums(testValue, testField).subscribe();
    }))
  })
});
