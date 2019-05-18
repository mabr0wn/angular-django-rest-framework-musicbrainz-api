import { Injectable } from '@angular/core';

export interface Credentials {
  username: string;
  token: string;
}

const credentialKey = 'credentials';

@Injectable({
  providedIn: 'root'
})
export class CredentialsService {

  private _credentials: Credentials| null = null;

  constructor() { 
    const savedCredentials = sessionStorage.getItem(credentialKey) || localStorage.getItem(credentialKey);
    if (savedCredentials) {
      this._credentials = JSON.parse(savedCredentials);
    }
  }


  get credentials() {
    return this._credentials || null;
  }
}


