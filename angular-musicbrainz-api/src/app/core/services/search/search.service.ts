// Angular
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
// RxJs
import { Observable } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';
// Services
import { ErrorHanlderService } from '../error-handler/error-hanlder.service';
// Model
import { Album } from '../../models/album';


@Injectable({
  providedIn: 'root'
})
export class SearchService {

  readonly url = 'https://musicbrainz.org/ws/2/release-group';

  constructor(
    private http: HttpClient,
    private errorService: ErrorHanlderService
  ) { }

  private 


  searchAlbums(value:string, field: string): Observable<Album[]> {
    const options = {
      params: new HttpParams()
                  .set('query', `${field}:${value}`)
                  .set('fmt', 'json')
                };
    return this.http.get<any>(this.url, options)
      .pipe(
        map(data => this.processData(data)),
        retry(3),
        catchError(this.errorService.handle<Album[]>('searchAlbums', []))
      )
  }

  private processData(raw: any):Album[] {
    let processed = [];
    for (let group of raw['release-groups']) {
      let id = group.id;
      let title = group.title;
      let artistCredit = [];
      for (let credit of group['artist-credit']) {
        let artist = {};
        artist['id'] = credit.artist.id;
        artist['name'] = credit.artist.name;
        artistCredit.push(artist);
      }
      processed.push({id, title, artistCredit});
    }
    return processed;
  }
}
