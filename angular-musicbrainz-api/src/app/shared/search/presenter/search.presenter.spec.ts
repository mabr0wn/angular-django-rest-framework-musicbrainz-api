import { fakeAsync,  tick } from '@angular/core/testing';
import { Subscription } from 'rxjs';


import { SearchPresenter } from './search.presenter';

describe(SearchPresenter.name, () => {
    let presenter: SearchPresenter;


    beforeEach(() => {
        presenter = new SearchPresenter();
    });

    describe('emit search terms', () => {
        let searchTermsSubscription: Subscription;
        const searchTerm = {
            searchTerm: jest.fn((term) => `${term}`)
        };

        beforeEach(() => {
          searchTermsSubscription = presenter.searchTerms
            .subscribe(searchTerm.searchTerm);
        });

        afterEach(() => {
            searchTermsSubscription.unsubscribe();
        });

        test('it will descibe an album search', fakeAsync(() => {
            const tupac = 'tupac';

            presenter.search(tupac);

            expect(searchTerm.searchTerm).toHaveBeenCalledTimes(1);
            expect(searchTerm.searchTerm).toMatchSnapshot(tupac);
        }));
    });
});
