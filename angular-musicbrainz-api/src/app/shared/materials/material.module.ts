// Angular
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
// Materials
import {
  MatAutocompleteModule,
  MatFormFieldModule,
  MatInputModule,
  MatGridListModule,
  MatListModule
} from '@angular/material';

export const MatModules = [
  MatAutocompleteModule,
  MatFormFieldModule,
  MatInputModule,
  MatGridListModule,
  MatListModule
];

@NgModule({
  declarations: [],
  imports: [CommonModule, ...MatModules],
  exports: [...MatModules],
})
export class MaterialModule { }
