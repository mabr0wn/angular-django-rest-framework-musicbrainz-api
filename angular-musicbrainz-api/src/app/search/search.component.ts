import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs/Observable';
import { SAMPLE_RESULTS } from '../sample-results';
import { map, startWith } from 'rxjs/operators';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent {
  searchControl: FormControl;

  filteredResults$: Observable<string[]>;

  results = SAMPLE_RESULTS;

  constructor() {
    this.searchControl = new FormControl('');
    this.filteredResults$ = this.searchControl.valueChanges.pipe(
      startWith(''),
      map(val => this.filterResults(val)),
      map(val => val.slice(0, 4)));
  }

  private filterResults(val: string): string[] {
    return val ? this.results.filter(v => v.toLowerCase().indexOf(val.toLowerCase()) === 0) : [];
  }

}
