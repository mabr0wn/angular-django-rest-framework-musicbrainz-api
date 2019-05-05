// Angular
import { Injectable } from '@angular/core';
// RxJs
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ErrorHanlderService {

  constructor() { }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  handle<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.log('error occured while executing ' + operation);
      console.error(error);
      return of(result as T); // keep app running by returning an empty result.
    };
  }
}
