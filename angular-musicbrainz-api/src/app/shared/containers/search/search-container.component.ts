/* tslint:enable */
import {
  Component,
  OnInit,
  ChangeDetectionStrategy
} from '@angular/core';
// RxJS
import {
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
import { SearchParams } from '@shared/search-params';
import { Album } from '@core/models/album';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-search-container',
  template: `
    <app-search-component (search)="search()">
      [results]="results | async"
    </app-search-component>
  `
})
/* tslint:disable */
export class SearchContainer implements OnInit {
  /* tslint:enable */
  private ngUnsubscribe: Subject<any> = new Subject();
  searchTerms: Subject<SearchParams> = new Subject<SearchParams>();
  albums: Observable<Album[]>;
  queryString: string;
  searchType: string;


  constructor(private searchService: SearchService) { }

  // Not tested yet...
  ngOnInit(): void {
    this.searchType = 'release';
    this.searchTerms.pipe(
      distinctUntilChanged((params1, params2) => params2.equals(params1)),
      switchMap(
        (params) => this.searchService.searchAlbums(params.term, params.type))
    ).subscribe((albums) => {
      console.log(albums);
    });
  }

  // Push a search term into the observable stream.
  // Not Tested...
  search(): void {
    this.searchTerms.next(new SearchParams(this.queryString, this.searchType));
  }
}
