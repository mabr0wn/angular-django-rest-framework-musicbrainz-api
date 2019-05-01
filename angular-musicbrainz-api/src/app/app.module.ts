// Angular
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatAutocompleteModule, MatFormFieldModule} from '@angular/material';
// Local
import { AppComponent } from './views/app.component';
import { AppRoutingModule } from './app-routing.module';
import { SearchComponent } from './search/search.component';
import { BoldPipe } from './search/bold.pipe';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    BoldPipe
  ],
  imports: [
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    MatFormFieldModule,
    MatAutocompleteModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
