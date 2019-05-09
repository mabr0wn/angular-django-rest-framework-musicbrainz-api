import { 
  Observable, 
  Subject 
} from 'rxjs';
import { 
  debounceTime, 
  distinctUntilChanged 
} from 'rxjs/operators';
import { SearchParams } from '@shared/search-params';

export class SearchPresenter {
  private searchTerms: Subject<SearchParams> = new Subject<SearchParams>();
  searchTerms$: Observable<SearchParams> = this.searchTerms;
    // search vars
    queryString: string;
    searching: boolean;
    searchType: string;
  search(): void {
    this.searchTerms.next(new SearchParams(this.queryString, this.searchType));
  }


}
