import { Artist } from './artist';

export class Album {
  id: string;
  title: string;
  artistCredit: Artist[];
  image?: string;
}