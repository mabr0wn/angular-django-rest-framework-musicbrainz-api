// Angular
import {
  Component,
  OnInit,
  OnDestroy,
  Output,
  EventEmitter,
  ChangeDetectionStrategy
 } from '@angular/core';
import { FormControl } from '@angular/forms';
// RxJs
import { 
  Observable, 
  Subject
} from 'rxjs';
import {
  map,
  startWith, 
  takeUntil 
} from 'rxjs/operators';
// Dummy data
import { SAMPLE_RESULTS } from '../../../sample-results';
// Model
import { Album } from '@core/models/album';
// Local
import { SearchParams} from '../../containers/search/search-params';
import { SearchPresenter } from '../../presenters/search.presenter';

@Component({
  selector: 'app-search-component',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [SearchPresenter],
})
export class SearchComponent implements OnInit, OnDestroy {
  @Output() search: EventEmitter<SearchParams> = new EventEmitter<SearchParams>();
  private ngUnsubscribe: Subject<any> = new Subject();
  //
  queryString: string;
  searching: boolean;
  searchType: string;
  searchTerms: Subject<SearchParams> = new Subject<SearchParams>();
  //
  searchControl: FormControl;
  filteredResults$: Observable<string[]>;
  results = SAMPLE_RESULTS;


  constructor(private presenter: SearchPresenter) { }

  // ngOnInit(): void {
  //   this.searchControl = new FormControl('');
  //   this.filteredResults$ = this.searchControl.valueChanges.pipe(
  //     startWith(''),
  //     map(val => this.filterResults(val)),
  //     map(val => val.slice(0, 4)));
  // }

  ngOnInit(): void {
    this.presenter.searchTerms$.pipe(
      // complete when component is destroyed
      takeUntil(this.searchTerms),
    ).subscribe(() => this.search.emit());
  }

  searchFor(): void {
    this.queryString = this.queryString ? this.queryString.trim() : null;
    if (this.queryString) {
      this.searching = true;
      this.presenter.search();
      this.queryString = null;
    }
  }

  filterResults(val: string): string[] {
    return val ? this.results.filter(v => v.toLowerCase().indexOf(val.toLowerCase()) === 0) : [];
  }

  ngOnDestroy() {
    this.ngUnsubscribe.next();
    this.ngUnsubscribe.complete();
    this.searchTerms.next();
    this.searchTerms.complete();
  }

}
