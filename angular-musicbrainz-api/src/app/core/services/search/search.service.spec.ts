// Angular Testing
import { TestBed } from '@angular/core/testing';
import { HttpClient, HttpParams } from '@angular/common/http';
// RxJS
import { of } from 'rxjs';
// Local
import { SearchService } from './search.service';
import { ErrorHanlderService } from '../error-handler/error-hanlder.service';

describe('SearchService', () => {
  let service: SearchService;

  const http = {
    get: jest.fn()
  };

  beforeEach(() => {

    TestBed.configureTestingModule({
      providers: [
        SearchService,
        ErrorHanlderService,
        {provide: HttpClient, useValue: http}
      ]
    });
    service = TestBed.get(SearchService);


    // Mock implementation of console.error to
    // return undefined to stop printing out to console log during test
    jest.spyOn(console, 'error').mockImplementation(() => undefined);
  });

  test('should create an instance successfully', () => {
    expect(service).toBeDefined();
  });

  describe('"searchAlbums" method', () => {
    test('calls external api with supplied query value and field', () => {
      expect(http.get).not.toHaveBeenCalled();

      let argUrl: string;
      let argOptions: {params: HttpParams};
      http.get.mockImplementation(
        (url, options) => { argUrl = url; argOptions = options; return of([]);
      });
      let testValue = 'testValue';
      let testField = 'testField';
      service.searchAlbums(testValue, testField).subscribe();

      expect(http.get).toHaveBeenCalledTimes(1);
      expect(argUrl).toContain('https://musicbrainz.org/');
      expect(argOptions.params.get('query')).toContain(testValue);
      expect(argOptions.params.get('query')).toContain(testField);
    });

    test('returns only "id", "title" and "artistCredit" from each album in response', () => {
      const artist1 = {id: 'a1', name: 'one'};
      const artist2 = {id: 'a2', name: 'two'};
      const rg1: any = {
        id: '1',
        title: 'first',
        'artist-credit': [{artist: artist1}],
        someOtherField: 'something else'
      };
      const rg2: any = {
        id: '2',
        title: 'second',
        'artist-credit': [{artist: artist2}],
        anotherField: 123456,
        yetAnotherField: {
          moreStuff: ['a', 'b', 'c']
        },
        aBool: true
      };
      http.get.mockReturnValueOnce(of({'release-groups': [rg1, rg2]}));
      let returned: any[];
      service.searchAlbums('value', 'field').subscribe(data => returned = data);

      expect(returned.length).toBe(2);
      expect(returned[0].id).toBe(rg1.id);
      expect(returned[0].title).toBe(rg1.title);
      expect(returned[0].artistCredit).toEqual([artist1]);
      expect(returned[0]).not.toBe(rg1);
      expect(returned[0]).not.toEqual(rg1);
      expect(returned[0].someOtherField).toBeUndefined();

      expect(returned[1].id).toBe(rg2.id);
      expect(returned[1].title).toBe(rg2.title);
      expect(returned[1].artistCredit).toEqual([artist2]);
      expect(returned[1]).not.toBe(rg2);
      expect(returned[1]).not.toEqual(rg2);
      expect(returned[1].anotherField).toBeUndefined();
      expect(returned[1].yetAnotherField).toBeUndefined();
      expect(returned[1].aBool).toBeUndefined();
    });
  });
});
