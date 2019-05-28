// Angular
import {
  Component,
  OnInit,
  OnDestroy,
  ChangeDetectionStrategy
 } from '@angular/core';
 // RxJs
import {
  Subject
} from 'rxjs';
import {
  switchMap,
  distinctUntilChanged
} from 'rxjs/operators';
// Model
import { Album } from '@core/models/album';
// Local
import { SearchParams} from '@shared/search/search-params';
// Services
import { SearchService } from '@core/services/search/search.service';
@Component({
  selector: 'app-search-component',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SearchComponent implements OnInit, OnDestroy {
  searching: boolean;
  query: string;
  searchType: string;
  
  result: Album[];

  searchTerms$: Subject<SearchParams> = new Subject();
  private destroy: Subject<any> = new Subject();

  constructor(private searchService: SearchService) { }

  ngOnInit(): void {
    this.queryResults();
  }

  queryResults() {
    this.searching = false;
    this.searchType = 'release';
    this.searchTerms$.pipe(
        // only emit when the current value is different than the last.
        distinctUntilChanged((params1, params2) => params2.equals(params1)),
        switchMap(
          (params) => this.searchService.queryAlbums(params.term, params.type)),
      )
      .subscribe((albums) => {
        // Log the albums for debugging purposes
        console.log(albums, 'albums[]');
        this.result = albums;
    });
  }

  searchFor(): void {
    if (this.query) {
      this.searching = true;
      this.searchTerms$.next(new SearchParams(this.query, this.searchType));
    }
  }

  ngOnDestroy(): void {
    this.destroy.next();
    this.destroy.complete();
    this.searchTerms$.complete();
  }
}
