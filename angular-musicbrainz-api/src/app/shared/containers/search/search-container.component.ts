/* tslint:enable */
import { 
  Component, 
  OnInit, 
  ChangeDetectionStrategy
} from '@angular/core';
// RxJS
import {
  of,
  Observable,
  Subject
 } from 'rxjs';
 import { 
   switchMap,
   distinctUntilChanged 
  } from 'rxjs/operators';
// Services
import { SearchService } from '@core/services/search/search.service';
// Local
import { SearchParams } from './search-params';
import { Album } from '@core/models/album';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-search-container',
  template: `
    <app-search-component>
      [results]="results | async"
    </app-search-component>
  `
})
/* tslint:disable */
export class SearchContainer implements OnInit {
  /* tslint:enable */
  albums: Observable<Album[]>;

  // search vars
  queryString: string;
  searching: boolean;
  searchType: string;
  results: Observable<Album[]>;
  search: Subject<SearchParams> = new Subject<SearchParams>();

  private ngUnsubscribe: Subject<any> = new Subject();

  constructor(private searchService: SearchService) { }

  ngOnInit() {
    this.searching = false;
    this.searchType = 'release';
    this.search.pipe(
      distinctUntilChanged((params1, params2) => params2.equals(params1)),
      switchMap(
        (params) => this.searchService.searchAlbums(params.term, params.type),
        (_params, albums, _outerIdx, _innerIdx) => of(albums)
       )
    ).subscribe((albums) => {
      this.results = albums;
      this.searching = false;
    });
  }

}
