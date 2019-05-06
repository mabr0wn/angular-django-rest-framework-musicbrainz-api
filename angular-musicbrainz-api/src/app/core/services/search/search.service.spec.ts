// Angular Testing
import { TestBed, inject } from '@angular/core/testing';
import { HttpClient, HttpParams } from '@angular/common/http';
// RxJS
import { of } from 'rxjs';
// Local
import { SearchService } from './search.service';
import { ErrorHanlderService } from '../error-handler/error-hanlder.service';

describe('SearchService', () => {
  let service: SearchService

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
    service = TestBed.get(SearchService)


    // Mock implementation of console.error to
    // return undefined to stop printing out to console log during test
    jest.spyOn(console, 'error').mockImplementation(() => undefined)
  });

  it('should create an instance successfully', () => {
    expect(service).toBeDefined()
  })

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
      expect(argOptions.params.get('query')).toContain(testValue);
      expect(argOptions.params.get('query')).toContain(testField);
    }));
  })
});
