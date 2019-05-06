import { Album } from './album';

export class List {
  id?: number;
  name?: string;
  albums: Album[];
  created?: string;
  lastUpdate?: string;
}
