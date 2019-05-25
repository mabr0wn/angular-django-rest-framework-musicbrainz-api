import { Album } from '@core/models/album'

export const MOCKALBUMS: Album[] = [
  {
    image: 'http://testurl1/',
    title: 'Test title 1',
    id: 'Test id 1',
    artistCredit: [
      {artist: 'test artist artist 1', id: 'test artist id 1'},
      {artist: 'test artist artist 2', id: 'test artist id 2'}
    ]
  },
  {
    image: 'http://testurl2/',
    title: 'Test title 2',
    id: 'Test id 2',
    artistCredit: [
      {artist: 'test artist artist 3', id: 'test artist id 3'}
    ]
  },
  {
    image: 'http://testurl3/',
    title: 'Test title 3',
    id: 'Test id 3',
    artistCredit: [
      {artist: 'test artist artist 4', id: 'test artist id 4'}
    ]
  }
];