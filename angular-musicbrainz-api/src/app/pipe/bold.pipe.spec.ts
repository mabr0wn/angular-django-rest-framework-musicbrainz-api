import {BoldPipe} from './bold.pipe';

describe('Pipe: Bold', () => {
    let pipe: BoldPipe;
    let search: string;

    beforeEach(() => {
        pipe = new BoldPipe();
    });

    it('should be instanciated', () => {
        expect(BoldPipe).toBeDefined();
    })
    // text from sample-results.ts
    it('providing text search returns bold pattern', () => {
        expect(pipe.transform('what', 'time is it'))
            .toBe('<b>what</b>', 'time is it');
    });
    // random text...
    it('should allow searching against any test', () => {
        expect(pipe.transform('fee', 'fi fo fum')).toBe('<b>fee</b>', 'fi fo fum');
    })
});