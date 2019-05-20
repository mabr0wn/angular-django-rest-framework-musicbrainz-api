// Angular Testing
import {
  fakeAsync,
  TestBed,
} from '@angular/core/testing';
// Services
import { SearchService } from '@core/services/search/search.service';
// Local
import { SearchContainer } from './search-container.component';
import { SearchComponent } from '@shared/search/component/search.component';
// Pipe
import { BoldPipe } from '@core/pipe/bold.pipe';
// Modules
import {
  MatAutocompleteModule,
  MatFormFieldModule
} from '@angular/material';
import {
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { Subject } from 'rxjs';

describe('SearchContainer', () => {
  let container: SearchContainer;
  let destroy: Subject<void> = new Subject();

  beforeEach((() => {
    const searchService = {
      searchAlbums: jest.fn()
    };

    TestBed.configureTestingModule({
      imports: [
        MatAutocompleteModule,
        MatFormFieldModule,
        FormsModule,
        ReactiveFormsModule
      ],
      declarations: [
        BoldPipe,
        SearchContainer,
        SearchComponent
      ],
      providers: [
        {provide: SearchService, useValue: searchService},
      ]
    })
    .compileComponents();
  }));

  test('', fakeAsync(() => {
    expect('').toEqual('');
  }));
});
