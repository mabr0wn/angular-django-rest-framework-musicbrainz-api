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

    it('providing text search returns bold pattern', () => {
        expect(pipe.transform('what', ''))
            .toBe('what');
    });

    it('should allow searching against any test', () => {
        expect(pipe.transform('fee', 'fi fo fum')).toBe('<b>fee</b>', 'fi fo fum');
    })
});