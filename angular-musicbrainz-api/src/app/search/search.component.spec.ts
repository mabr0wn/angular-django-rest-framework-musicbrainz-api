// Angular Testing
import {
  async,
  ComponentFixture,
  TestBed
} from '@angular/core/testing';
// Components
import { SearchComponent } from './search.component';
// Pipe
import { BoldPipe } from '../core/pipe/bold.pipe';
// Modules
import {
  MatAutocompleteModule,
  MatFormFieldModule
} from '@angular/material';
import {
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';


describe('SearchComponent', () => {
  let component: SearchComponent;
  let fixture: ComponentFixture<SearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        MatAutocompleteModule,
        MatFormFieldModule,
        FormsModule,
        ReactiveFormsModule
      ],
      declarations: [
        BoldPipe,
        SearchComponent
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create search component', () => {
    expect(component).toBeTruthy();
  });

  it('should filter new sample results array',(() => {
    component.results = [
      'What\'s the weather in San Francisco?',
      'did you see the game?'
    ];
    expect(component.filterResults('What\'s the weather in San Francisco?').length).toBe(1);
    expect(component.filterResults('did you see the game?').length).toBe(1);
    expect(component.filterResults('').length).toBe(0);
  }))
});
