// Angular Testing
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
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

describe('SearchContainer', () => {
  let component: SearchContainer;
  let fixture: ComponentFixture<SearchContainer>;

  beforeEach(async(() => {

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

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchContainer);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should', () => {
    expect('').toEqual('');
  })
});
