// Angular
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormsModule, 
  ReactiveFormsModule
} from '@angular/forms';
// Local
import { SearchComponent } from './search/component/search.component';
import { SearchContainer } from './search/container/search-container.component';
// Modules
import { CoreModule } from '../core/core.module';
import { MaterialModule } from './materials/material.module';

@NgModule({
  declarations: [SearchComponent, SearchContainer ],
  imports: [
    CommonModule,
    CoreModule,
    FormsModule,
    MaterialModule,
    ReactiveFormsModule,
    
  ],
  exports: [SearchComponent, SearchContainer]
})
export class SharedModule { }
