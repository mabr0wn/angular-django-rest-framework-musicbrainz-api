export class SearchParams {
    term: string
    type: string
    constructor(term, type) {
      this.term = term;
      this.type = type;
    }
  
    equals(params: SearchParams): boolean {
      return this.term === params.term && this.type === params.type;
    }
  }