/* tslint:enable */
import {
  Component,
  OnInit,
  ChangeDetectionStrategy
} from '@angular/core';
// RxJS
import {
  Subject
 } from 'rxjs';
 import { 
   switchMap,
   distinctUntilChanged 
  } from 'rxjs/operators';
// Services
import { SearchService } from '@core/services/search/search.service';
// Local
import { SearchParams } from '@shared/search/search-params';

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-search-container',
  template: `
    <app-search-component
    (search)="search($event)"></app-search-component>
  `
})
/* tslint:disable */
export class SearchContainer implements OnInit{
  /* tslint:enable */
  searchTerms: Subject<SearchParams> = new Subject();

  queryString: string;
  searchType: string;

  constructor(private searchService: SearchService) { }

  // Not tested yet...
  ngOnInit(): void {
    this.searchType = 'release';
    this.searchTerms.pipe(
      // only emit when the current value is different than the last.
      distinctUntilChanged((params1, params2) => params2.equals(params1)),
      switchMap(
        (params) => this.searchService.searchAlbums(params.term, params.type))
    )
    .subscribe((albums) => {
      // Log the albums for debugging purposes
      console.log(albums, 'albums');
    });
  }

  // Push a search term into the observable stream.
  search(): void {
    // Assigned static string for `this.queryString` until bug is located.
    this.queryString = this.queryString ? this.queryString.trim() : 'tupac';
    // Log the `this.query` for debugging purposes
    console.log(this.queryString, '@container');
    this.searchTerms.next(new SearchParams(this.queryString, this.searchType))   
  }
}
