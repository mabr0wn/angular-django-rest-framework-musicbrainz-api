// Angular Testing
import {
  async,
  ComponentFixture,
  TestBed
} from '@angular/core/testing';
// RxJs
import { of } from 'rxjs';
// Components
import { SearchComponent } from './search.component';
// Pipe
import { BoldPipe } from '@core/pipe/bold.pipe';
// Services
import { SearchService } from '@core/services/search/search.service';
// Models
import { Album } from '@core/models/album';
// Modules
import {
  MatAutocompleteModule,
  MatFormFieldModule
} from '@angular/material';
import {
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { MDBBootstrapModule } from 'angular-bootstrap-md';


describe('SearchComponent', () => {
  let component: SearchComponent;
  let fixture: ComponentFixture<SearchComponent>;
  let dummyResult: Album[];
  const searchService = {
    queryAlbums: jest.fn()
  };

  beforeEach(async(() => {

    dummyResult = [
      {id: '1', title: 'title1', artistCredit: [], image: 'image1'},
      {id: '2', title: 'title2', artistCredit: [], image: 'image2'},
    ];

    TestBed.configureTestingModule({
      imports: [
        MDBBootstrapModule,
        MatAutocompleteModule,
        MatFormFieldModule,
        FormsModule,
        ReactiveFormsModule
      ],
      declarations: [
        BoldPipe,
        SearchComponent
      ],
      providers: [
        {provide: SearchService, useValue: searchService},
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  describe('Should run "searchFor" method', () => {
    const mockQueryString = 'testQuery';
    let setUp = () => {
      searchService.queryAlbums.mockReturnValueOnce(of(dummyResult));
      component.query = mockQueryString;
    }
    test('calls searchService.queryAlbums with queryString', () => {
      setUp();
      expect(searchService.queryAlbums).not.toHaveBeenCalled();

      component.searchFor();
      expect(searchService.queryAlbums).toMatchSnapshot(mockQueryString, component.searchType);
    });
  });
});
