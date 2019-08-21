// Angular
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormsModule,
  ReactiveFormsModule
} from '@angular/forms';
// Local
import { SearchComponent } from './search/component/search.component';
// Modules
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { CoreModule } from '../core/core.module';
import { MaterialModule } from './materials/material.module';
@NgModule({
  declarations: [SearchComponent],
  imports: [
    MDBBootstrapModule.forRoot(),
    CommonModule,
    CoreModule,
    FormsModule,
    MaterialModule,
    ReactiveFormsModule,
  ],
  exports: [SearchComponent ],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class SharedModule { }
