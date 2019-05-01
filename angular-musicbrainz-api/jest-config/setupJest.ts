import 'jest-preset-angular';
import './jestGlobalMocks';

jest.spyOn(global.console, 'warn').mockImplementation(() => jest.fn());