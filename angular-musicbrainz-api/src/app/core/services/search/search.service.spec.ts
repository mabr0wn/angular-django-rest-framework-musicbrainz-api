import { TestBed, inject } from '@angular/core/testing';
import { HttpClient, HttpParams, HttpClientModule } from '@angular/common/http';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing'


import { of } from 'rxjs';

import { SearchService } from './search.service';
import { ErrorHanlderService } from '../error-handler/error-hanlder.service';
import { Album } from '../../models/album';

describe('SearchService', () => {  
  const http = {
    get: jest.fn() 
  }

  beforeEach(() => {

    TestBed.configureTestingModule({
      providers: [
        SearchService,
        ErrorHanlderService,
        {provide: HttpClient, useValue: http}
      ]
    });
    
    // Mock implementation of console.error to
    // return undefined to stop printing out to console log during test
    jest.spyOn(console, 'error').mockImplementation(() => undefined)
  });
  describe('"searchAlbums" method', () => {
    it('calls external api with supplied query value and field', inject([SearchService], (service: SearchService) => {
      expect(http.get).not.toHaveBeenCalled();

      let argUrl: string;
      let argOptions: {params: HttpParams};
      http.get.mockImplementation(
        (url, options) => { argUrl = url; argOptions = options; return of([])
      });
      const testValue = 'testValue';
      const testField = 'testField';
      service.searchAlbums(testValue, testField).subscribe();

      expect(http.get).toHaveBeenCalledTimes(1);
      expect(argUrl).toContain('https://musicbrainz.org/');
    }));
  })
});
