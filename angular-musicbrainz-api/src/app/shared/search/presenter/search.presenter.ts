// RxJs
import { Subject } from 'rxjs';
// Local
import { SearchParams } from '@shared/search/search-params';

export class SearchPresenter {
  searchTerms: Subject<SearchParams> = new Subject();



  search(term): void {
    // Log the term for debugging purposes
    // console.log(term, '@presenter');
    this.searchTerms.next(term);
  }
}
