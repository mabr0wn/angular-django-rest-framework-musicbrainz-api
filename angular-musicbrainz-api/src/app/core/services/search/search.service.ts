// Angular
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
// RxJs
import { Observable } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';
// Services
import { ErrorHanlderService } from '../error-handler/error-hanlder.service';



@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor() { }
}
