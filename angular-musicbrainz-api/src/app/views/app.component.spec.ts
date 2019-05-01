// Angular testing
import {
  TestBed,
  async
} from '@angular/core/testing';
// Components
import { AppComponent } from './app.component';
import { SearchComponent } from '../search/search.component';
// pipe
import { BoldPipe } from '../core/pipe/bold.pipe';
// Modules
import {
  MatAutocompleteModule,
  MatFormFieldModule
} from '@angular/material';
import {
  FormsModule,
  ReactiveFormsModule
} from '@angular/forms';

describe('AppComponent', () => {
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
        AppComponent,
        SearchComponent
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });
});
