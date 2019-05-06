import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchContainer } from './search-container.component';

describe('SearchContainer', () => {
  let component: SearchContainer;
  let fixture: ComponentFixture<SearchContainer>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchContainer ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchContainer);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
