import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchComponent } from './components/search/search.component';
import { MatAutocompleteModule, MatFormFieldModule} from '@angular/material';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {CoreModule } from '../core/core.module';
import { SearchContainer } from './containers/search/search-container.component';
@NgModule({
  declarations: [SearchComponent, SearchContainer],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatAutocompleteModule,
    CoreModule
  ],
  exports: [SearchComponent, SearchContainer]
})
export class SharedModule { }
