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

  isAuthenticated(): boolean {
    return !!this.credentials;
  }

  get credentials() {
    return this._credentials || null;
  }

  setCredentials(credentials?: Credentials, remember?: boolean) {
    this._credentials = credentials || null;

    if (credentials) {
      const storage = remember ? localStorage : sessionStorage;
      storage.setItem(credentialKey, JSON.stringify(credentials));
    } else {
      sessionStorage.removeItem(credentialKey);
      localStorage.removeItem(credentialKey);
    }
  }
}


