// Angular
import {
  Component,
  OnInit,
  OnDestroy,
  Output,
  EventEmitter,
  ChangeDetectionStrategy,
  Input
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
import { SearchParams} from '@shared/search-params';
import { SearchPresenter } from '@shared/presenters/search.presenter';
export class SearchP {
  term: string;
  type: string;
}
@Component({
  selector: 'app-search-component',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [SearchPresenter],
})
export class SearchComponent implements OnInit, OnDestroy {
  @Input() albums: Album[];
  @Input() queryString: string;
  @Output() search: EventEmitter<SearchParams> = new EventEmitter();

  private ngUnsubscribe: Subject<any> = new Subject();
  filteredResults$: Observable<string[]>;
  searchControl: FormControl;

  results = SAMPLE_RESULTS;
  searchType: string;

  constructor(private presenter: SearchPresenter) {}

  ngOnInit(): void {
    this.searchControl = new FormControl('');
    this.filteredResults$ = this.searchControl.valueChanges.pipe(
      startWith(''),
      map(val => this.filterResults(val)),
      map(val => val.slice(0, 4)));
    this.presenter.searchTerms.pipe(
      // complete when component is destroyed
      takeUntil(this.ngUnsubscribe),
    ).subscribe(_ => this.search.emit(new SearchParams(this.queryString, this.searchType)));
  }

  ngOnDestroy(): void {
    this.ngUnsubscribe.next();
    this.ngUnsubscribe.complete();
  }

  searchFor(term): void {
    // Log the term for debugging purposes
    console.log(term, '@component');
    this.presenter.search(term);
  }

  filterResults(val: string): string[] {
    return val ? this.results.filter(v => v.toLowerCase().indexOf(val.toLowerCase()) === 0) : [];
  }
}
