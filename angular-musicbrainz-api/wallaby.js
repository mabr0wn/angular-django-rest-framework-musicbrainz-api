const ngxWallabyJest = require('ngx-wallaby-jest');

module.exports = (wallaby) => {
    return {
        files: [
            'src/**/*.+(ts|html|json|snap|css|less|sass|scss|jpg|jpeg|gif|png|svg)',
            '!src/**/*.spec.ts',
          ],

        tests: ['src/**/*.spec.ts'],

        env: {
            type: 'node',
            runner: 'node'
        },
        compilers: {
            '**/*.ts?(x)': wallaby.compilers.typeScript({
              module: 'commonjs',
              getCustomTransformers: () => {
                return {before: [require('jest-preset-angular/InlineHtmlStripStylesTransformer').factory({compilerModule: require('typescript')})]};
              }
            }),
            '**/*.html': file => ({
              code: require('ts-jest').process(file.content, file.path, {globals: {'ts-jest': {stringifyContentPathRegex: '\\.html$'}}}),
              map: {version: 3, sources: [], names: [], mappings: []},
              ranges: []
            })
          },
      
        preprocessors: {
            // This translate templateUrl and styleUrls to the right implementation
            // For wallaby
            'app/**/*.component.ts': ngxWallabyJest,
        },

        setup: function(wallaby) {
          let jestConfig = require("./package.json").jest;
          delete jestConfig.preset;
          jestConfig = Object.assign(require("jest-preset-angular/jest-preset"), jestConfig);
          jestConfig.transformIgnorePatterns.push("instrumented.*\.(jsx?|html)$");
          wallaby.testFramework.configure(jestConfig);
        },
        testFramework: 'jest'
    }
}